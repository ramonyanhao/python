'''
使用这个方法最大的印象就是调用对象的属性可以像字典取值一样使用中括号['key']
使用中括号对对象中的属性进行取值、赋值或者删除时，会自动触发对应的__getitem__、__setitem__、__delitem__方法
'''
#  __getitem__通过[]来操作对象的，__getattr__使用.来操作对象的,下面的例子中两者都是把对象属性保存在__dict__中，如果直接保存在self中就不需要__dict__，主要看在方法中怎么定义
class Foo(object):
    def __init__(self):
        self.name = 'jack'

    def __getitem__(self,item):
        print('使用getitem',self.__dict__,item)
        if item in self.__dict__:       # item = key，判断该key是否存在对象的 __dict__ 里，
            return self.__dict__[item]  # 返回该对象 __dict__ 里key对应的value

    def __setitem__(self, key, value):  # f1['age']=10使用了setitem
        print('使用setitem',key,value)
        self.__dict__[key] = value      # 把实例属性保存在dict中
        # self[key]=value  # 把实例属性保存在self中

    def __delitem__(self, key):
        print('使用delitem删除%s'%key)
        del self.__dict__[key]
    def __getattr__(self, item):        # 一直都没有使用getattr,因为所有的属性都已经被赋值了，如果调用没有赋值的属性就会使用getattr,例如f1.company
        print('使用getattr',item)
        if item in self.__dict__:
            return self.__dict__[item]

    def __setattr__(self, key, value):  # f1.com='memebox'使用了setattr
        print('使用setattr',key,value)
        self.__dict__[key] = value


    def __delattr__(self, item):
        print('使用delattr,删除%s'%item)
        del self.__dict__[item]

f1 = Foo()
print(f1['name'])   # 使用getitem获得值jack
f1['age'] =10
f1.com='memebox' # 注意这里可以使用.来操作对象，因为这里有__setattr__属性和__setitem__属性，__setattr__属性默认存在所有类实力中，而__setitem__属性则需要创建才可以使用
print(f1['age'],f1.age,f1.com,f1['com'])  # 使用print(f1.com)可以打印出结果因为有__getattribute__属性，使用print(f1['age'])可以打印出结果因为有__getitem__属性
print(dir(f1))
f1.company='meme'
del f1.name  # 使用__delattr__
del f1['company']  # 使用__delitem__
print(f1.__dict__)
'''
使用对象取值、赋值或者删除时，会默认的调用对应的__getattr__、__setattr__、__delattr__方法。
对象取值时，取值的顺序为：先从object里__getattribute__中找，第二步从对象的属性中找，第三步从当前类中找，第四步从父类中找，第五步从__getattr__中找，如果没有，直接抛出异常。
'''
class Foo(object):
    def __init__(self):
        self.name = 'jack'

    def __getattr__(self, item):
        print('使用getattr',item)
        if item in self.__dict__:
            return self.__dict__[item]

    def __setattr__(self, key, value):
        print('使用setattr',key,value)
        self.__dict__[key] = value


    def __delattr__(self, item):
        del self.__dict__[item]

c1 = Foo()
print(c1.name)  # jack
c1.age = 18
print(c1.age)   # 18
# c1['com']='memebox' 这里不可以使用[]来操作对象，主要因为这里只创建了__setattr__属性，没有创建__setitem__属性
print(c1.__dict__)
print(dir(c1))
print()
# 如果类继承了dict结果不一样，因为如果继承了dict,类属性包含了getitem,getattr,setitem,setattr属性，例如：
class Dict(dict):
    def __init__(self,**kw):
        super().__init__(**kw)
    def __getattr__(self, key):
        try:
            print('使用getattr',key)
            return self[key]
        except KeyError:
            raise AttributeError("没有找到属性 '%s'" % key)

    def __setattr__(self, key, value):
        print('使用setattr',key,value)
        self[key] = value
d1=Dict()
print(dir(d1))
d1.name='harmon'
d1['age']=35
print(d1.name,d1.age)