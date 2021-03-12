#元类就是通过类或者函数创建类，如下例子通过type创建一个类，type就是一个元类
myclass=type('my',(),{'name':'harmon'})#相当于class my(): name='harmon'，类名是my,中间的()就是继承父类用的(),后面的name就是类的方法名称,后面的值可以指定为其他的类或函数
print(myclass.name,myclass)#输出harmon和<class '__main__.my'>，注意类名是my
#通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class
# 自定义一个元类，运行这个元类可以创建另一个类
class UpperAttrMetaClass(type):
    def __new__(cls, class_name, class_parents, class_attr):#也可以通过函数创建类，不同的地方就是函数不需要__new__,def upper_attr(class_name, class_parents, class_attr)
        # class_name 会保存类的名字 Foo
        # class_parents 会保存类的父类 object
        # class_attr 会以字典的方式保存所有的类属性
        # 遍历属性字典，把不是__开头的属性名字变为大写
        if class_name=='Foo':
            return type.__new__(cls,class_name,class_parents,class_attr)
        new_attr = {}
        print(class_name,class_parents,class_attr)
        for name, value in class_attr.items():
            if not name.startswith("__"):# startswith检查字符串是否以__开头
                new_attr[name.upper()] = value#如果不是以__开头，把name改为name.upper()并添加到new_attr字典中
                print(new_attr)
        # 调用type来创建一个类，这里是重点，UpperAttrMetaClass这个类通过type返回一个新类，这个新类修改了一些属性和方法，例如new_attr
        return type.__new__(cls,class_name, class_parents, new_attr)

class Foo(dict, metaclass=UpperAttrMetaClass): # metaclass=UpperAttrMetaClass就是设置Foo类的元类为UpperAttrMetaClass
    bar = 'bip'#通过元类UpperAttrMetaClass修改了Foo类属性bar为大写BAR,这样做的意义就是如果有许多的类都需要修改一些属性，那这需要修改这个自定义的元类就可以了，不用一个个修改

class te(Foo):
    ok='ko'
'''如果是python2的写法，这里改为:
class Foo(object):
    __metaclass__ = UpperAttrMetaClass
    bar = 'bip'
'''
#注意这里的类变量bar不能使用了，通过元类的修改只能使用BAR

'''单例模式就是确保一个类只有一个对象实例，这样做会节省内存资源
比如，某个服务器程序的配置信息存放在一个文件中，客户端通过一个 AppConfig 的类来读取配置文件的信息。如果在程序运行期间，有很多地方都需要使用配置文件的内容，
也就是说，很多地方都需要创建 AppConfig 对象的实例，这就导致系统中存在多个 AppConfig 的实例对象，而这样会严重浪费内存资源，尤其是在配置文件内容很多的情况下。
事实上，类似 AppConfig 这样的类，我们希望在程序运行期间只存在一个实例对象。'''
#Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码
class Singleton(object):
    def foo(self):
        pass
sing = Singleton()#直接在文件中实例化这个类，然后在别的地方导入这个文件的实例，注意不是导入这个类，导入这个类的实例sing:from a import sing
# 这样在其他的地方这个类的实例内存地址就是这个文件中类的实例内存地址
# 简单的方式实例单例模式：
class danli:
    _ins=None # 这里需要设置类属性，如果没有将会报错，如果把下面的if条件改为:if not hasattr(danli,"_ins")就可以不用赋值_ins这个类属性
    def __new__(cls, *args, **kwargs):
        if not cls._ins: # 通过这里做拦截
            cls._ins=super().__new__(cls)    # 如果发现类属性是空的或者None时，把当前实例化出的对象赋值给这个类属性
        return cls._ins    # 如果发现类属性不是空的则直接返回这个类属性，从而所有实例出的对象都是用一个类实例的内存地址
danli1=danli()
danli2=danli()
print(id(danli1),id(danli2))# 两个类实例使用的同一个内存地址
import threading
class Singleton(object):
    _instance_lock = threading.Lock()#因为多线程下的单例模式容易引起内存混乱，主要因为多个实例使用同一个内存地址，如果同时有两个以上的实例占用这个内存地址就会出现冲突，所以这里使用线程锁
#在这里没有给_instance赋值，原因是在if判断语句使用hasattr,如果把if not hasattr(Singleton,"_instance")改为if not cls._instance,那么就需要给_instance赋值None
    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):# hasattr检查Singleton类中有没有_instance这个属性，有返回True,否则返回False
            with Singleton._instance_lock:# 如果Singleton没有_instance这个属性，加入线程锁，with加入线程锁运行完会自动解锁
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = super().__new__(cls)# 如果没有_instance，这里给类属性_instance赋值为super().__new__(cls),super().__new__(cls)就是实例化出来的对象
        return Singleton._instance# 修改了__new__方法的返回值为赋值过的类实例,这样通过if判断如果检查到有这个类实例，如obj1,那么直接返回这个类实例，否则重新赋值类实例为obj1
obj1=Singleton()
obj2=Singleton()
print(id(obj1),id(obj2))
def task(arg):
    obj = Singleton()
    print(id(obj))

for i in range(10):
    t = threading.Thread(target=task,args=[i,])
    t.start()#通过多线程看到所有的类实例使用的都是同一个内存地址