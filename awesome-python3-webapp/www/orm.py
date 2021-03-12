import asyncio, logging

import aiomysql
def log(sql, args=()):
    logging.info('SQL: %s' % sql)

async def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )

async def select(sql, args, size=None):
    log(sql, args)
    global __pool
    async with __pool.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:  # aiomysql.DictCursor使返回的结果形式为字典
            await cur.execute(sql.replace('?', '%s'), args or ())  # 把sql语句中的?转换成%s，%s的参数就是args
            if size:
                rs = await cur.fetchmany(size)
            else:
                rs = await cur.fetchall()  # cur.execute执行后使用fetchall返回执行后的结果值
        logging.info('rows returned: %s' % len(rs))
        return rs

async def execute(sql, args, autocommit=True):
    log(sql)
    async with __pool.acquire() as conn:
        if not autocommit:
            await conn.begin()
        try:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                await cur.execute(sql.replace('?', '%s'), args)
                affected = cur.rowcount
            if not autocommit:
                await conn.commit()
        except BaseException as e:
            if not autocommit:
                await conn.rollback()
            raise
        return affected

def create_args_string(num):
    L = []
    for n in range(num):
        L.append('?')
    return ', '.join(L)

class Field(object):

    def __init__(self, name, column_type, primary_key, default):
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.default = default

    def __str__(self):
        return '<%s, %s:%s>' % (self.__class__.__name__, self.column_type, self.name)

class StringField(Field):  # 使用继承类Field的目的是为了把StringField中的__init__默认值传入到实例中，否则只用Field，每次创建实例都需要传入相应的参数
# 在实际使用中例如User(Model)就可以修改默认参数为实际需要的参数：id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    def __init__(self, name=None, primary_key=False, default=None, ddl='varchar(100)'):
        super().__init__(name, ddl, primary_key, default)  # 在实际使用中，实例不能使用ddl,需要使用基类中的属性column_type例如：string=StringField(),string.ddl会报错，使用string.column_type
    '''
    如果不用super().__init__，就需要给每个参数传参，例如：
        self.name = name
        self.primary_key = primary_key
        self.default = default
        self.column_type = ddl
    '''

class BooleanField(Field):

    def __init__(self, name=None, default=False):
        super().__init__(name, 'boolean', False, default)

class IntegerField(Field):

    def __init__(self, name=None, primary_key=False, default=0):
        super().__init__(name, 'bigint', primary_key, default)

class FloatField(Field):

    def __init__(self, name=None, primary_key=False, default=0.0):
        super().__init__(name, 'real', primary_key, default)

class TextField(Field):

    def __init__(self, name=None, default=None):
        super().__init__(name, 'text', False, default)

class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        tableName = attrs.get('__table__', None) or name
        logging.info('found model: %s (table: %s)' % (name, tableName))
        mappings = dict()
        fields = []
        primaryKey = None
        for k, v in attrs.items():  # 注意这里attrs的key是字段名，value是字段实例，不是字段的具体值
            if isinstance(v, Field):  # 如果传入的属性属于Field中的子类，例如：StringField,主要用来找出数据库字段属性并放在mappings中，把不需要的属性排除，例如：__table__=users
                logging.info('  found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
                if v.primary_key:  # v就是Field类下面的子类的实例，例如StringField(Field)，所以可以通过访问类中的属性primary_key来获取值
                    # 找到主键:
                    if primaryKey:
                        raise Exception('Duplicate primary key for field: %s' % k)
                    primaryKey = k  # 数据表中的id主键就是k
                else:
                    fields.append(k)
        if not primaryKey:
            raise Exception('Primary key not found.')
        for k in mappings.keys():
            attrs.pop(k)  # 把attrs传入的所有数据库键值删除并放到mappings中，然后把mappings指定为attrs其中的一个值，方便管理
        escaped_fields = list(map(lambda f: '`%s`' % f, fields))  # 把fields改为['`email`', '`passwd`', '`admin`', '`name`', '`image`', '`created_at`'],给列表中每个元素都加反引号
        attrs['__mappings__'] = mappings  # mappings存放了数据库中所有的键和值，例如{'id': <orm.StringField object at 0x0000020EDE447F88>}
        attrs['__table__'] = tableName
        attrs['__primary_key__'] = primaryKey  # 主键属性名
        attrs['__fields__'] = fields  # fields列表存放了除了主键以外的所有键，例如['email', 'passwd', 'admin', 'name', 'image', 'created_at']
        attrs['__select__'] = 'select `%s`, %s from `%s`' % (primaryKey, ', '.join(escaped_fields), tableName)  # 通过join把escaped_fields改为`email`, `passwd`, `admin`, `name`, `image`, `created_at`
        # 这里注意primaryKey就是主键id,通过`%s`把它转化为`id`,从而和escaped_fields一样的格式
        attrs['__insert__'] = 'insert into `%s` (%s, `%s`) values (%s)' % (tableName, ', '.join(escaped_fields), primaryKey, create_args_string(len(escaped_fields) + 1))
        attrs['__update__'] = 'update `%s` set %s where `%s`=?' % (tableName, ', '.join(map(lambda f: '`%s`=?' % (mappings.get(f).name or f), fields)), primaryKey)
        attrs['__delete__'] = 'delete from `%s` where `%s`=?' % (tableName, primaryKey)
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):
    # 继承了dict类self就变成了一个字典，并且设定了getattr和setattr方法，例如:u = User(name='Test3', email='test3@example.com', passwd='1234567890', image='about:blank')
    # self就是User类的实例化对象u,其中的参数name,email,passwd,image就是self这个字典中的键，他们的值就是字典中的值，如果没有__getattr__和__setattr__，这个self就是一个空字典，但是可以使用self.__dict__来获取传入的参数
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


    def getValue(self, key):  # 从当前实例中获取key的值
        return getattr(self, key, None)

    def getValueOrDefault(self, key):  # getValueOrDefault函数用来从实例化参数中获取key的值，如果key没有值，就从__mappings__中获取默认值
# 例如：User(name='Test1', email='test1@example.com', passwd='1234567890', image='about:blank')，只给出了name,email,passwd,image的值，admin，created_at，id的值都需要使用默认值
        value = getattr(self, key, None)  # 这里的key是数据库中的字段名，例如:email,passwd,name，value是字段对应的值,例如：test0@example.com，1234567890，Test0
        '''
        向数据库添加完数据使用save()保存时，调用getValueOrDefault()方法自动获取添加数据时设置的默认值，value是字段类实例化时传入的值，key是字段实例化时的变量，例如：
        key:email value:test18@example.com  u = User(name='Test18', email='test18@example.com', passwd='1234567890', image='about:blank')
        key:passwd value:1234567890
        key:admin value:None  没有传入admin的值，所以这里为None,再从__mappings__[admin]中获取字段类对象BooleanField(),Field子类BooleanFIeld().default默认值为False
        key:name value:Test18
        key:image value:about:blank
        key:created_at value:None  created_at的值也是None,同样从__mappings__[create_at]中获取字段类对象FloatField(),但是在mappings中发现了FloatField()默认值为time.time
        而且默认值time.time还是一个函数，所以用到了value = field.default() if callable(field.default) else field.default
        key:id value:None
        '''
        if value is None:  # 如果没有给key赋值，例如admin没有设置值，通过getattr函数给admin设置默认值None,符合if条件
            field = self.__mappings__[key]  # 由于mappings存放了数据库中所有的键和值，如果实例化时没有给键赋值，这里把对应值为None的键通过__mappings__[key]获取值
# field其实就是值为None的字段名，例如实例化时没有给id字段传值的StringField,没有给admin传值的BooleanField,没有给created_at传值的FloatField，但是这些也是类，所以可以通过类属性default来获取值
# 这里的field是三个value为None的字段类对象：admin，created_at，id，例如created_at：<FloatField, real:None> field.default: <built-in function time> field.name: None
            if field.default is not None:  # field.default也有可能是函数，例如id中的next_id，created_at中的time.time,所以需要通过判断field.default是否为函数
                value = field.default() if callable(field.default) else field.default  # callable判断field.default是否为可调用函数，如果是则执行field.default(),如果不是执行field.default
                logging.debug('using default value for %s: %s' % (key, str(value)))
                setattr(self, key, value)  # 设置key的值为获取的默认值value
        return value

    @classmethod
    async def findAll(cls, where=None, args=None, **kw):
        ' find objects by where clause. '
        sql = [cls.__select__]  # 首先把__select__语句赋值给sql,注意sql是一个列表
        if where:
            sql.append('where `%s`=?' %where)  # 然后给sql添加各种条件，where,limit,orderby等等

        if args is None:  # args就是where,limit条件的值，例如select * from users limit 1
            args = []
        orderBy = kw.get('orderBy', None)
        if orderBy:
            sql.append('order by')
            sql.append(orderBy)
        limit = kw.get('limit', None)
        if limit is not None:
            sql.append('limit')
            if isinstance(limit, int):
                sql.append('?')
                args.append(limit)
            elif isinstance(limit, tuple) and len(limit) == 2:
                sql.append('?, ?')
                args.extend(limit)
            else:
                raise ValueError('Invalid limit value: %s' % str(limit))
        rs = await select(' '.join(sql), args)  # 最后通过select函数把sql列表转换为mysql语句提交给数据库执行
        print(rs)
        return [cls(**r) for r in rs]

    @classmethod
    async def findNumber(cls, selectField, where=None, args=None):
        ' find number by select and where. '
        sql = ['select %s _num_ from `%s`' % (selectField, cls.__table__)]  # _num_是用来替换字段名字的，例如select id as _num_ from users,把字段id暂时替换成_num_
        # 这样查询的结果字段名是_num_,如果不用_num_查询的结果字段名是id,但是id有可能是一个函数，所以使用_num_代替
        if where:
            sql.append('where `%s`=?'%where)
        rs = await select(' '.join(sql), args,1)  # 注意最后的1，select函数中有size参数，这里的1表示只输出一行结果
        if len(rs) == 0:
            return None
        print(rs)
        return rs[0]['_num_']  # rs是一个列表里嵌套了字典，rs[0]['_num_']代表返回这个列表的第一个嵌套字典中_num_的值

    @classmethod
    async def find(cls, pk):
        ' find object by primary key. '
        rs = await select('%s where `%s`=?' % (cls.__select__, cls.__primary_key__), [pk], 1)
        print(rs)
        if len(rs) == 0:
            return None
        return cls(**rs[0])

    async def save(self):
        args = list(map(self.getValueOrDefault, self.__fields__))  # self.__fields__除主键外的所有字段名,args是这些字典对应的值，如果没有对应的值就通过getValueOrDefault函数获取默认值
        print('fields:',self.__fields__)
        print('args:',args)
        args.append(self.getValueOrDefault(self.__primary_key__))  # 因为self.__fields__没有主键，所以这里要添加主键对应的默认值
        print('args:', args)
        rows = await execute(self.__insert__, args)  # 通过insert插入这些值从而达到给数据库添加数据的目的
        if rows != 1:
            logging.warn('failed to insert record: affected rows: %s' % rows)

    async def update(self,key=None):
        args = list(map(self.getValue, self.__fields__))
        args.append(self.getValue(self.__primary_key__))
        rows = await execute(self.__update__, args)
        if rows != 1:
            logging.warn('failed to update by primary key: affected rows: %s' % rows)

    async def remove(self):
        args = [self.getValue(self.__primary_key__)]
        rows = await execute(self.__delete__, args)  # execute函数执行sql语句并把语句中的?替换成args
        if rows != 1:
            logging.warn('failed to remove by primary key: affected rows: %s' % rows)