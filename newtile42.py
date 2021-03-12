class A():
    def b(self):
        self.b1=123
    def c(self):
        self.b()#类中不同方法互相调用函数，需要先引入这个方法，例如self.b()在方法c中引入方法b,再调用方法b中的函数self.b1
        c1=self.b1+5
        print (c1,self.b1)#如果这里是return不是print,那在调用这个类时注意需要使用print(类实例名.方法名)
a=A()
a.c()
class A():
    def __init__(self):#或者直接在类的__init__下指定self.b1这个函数，在其他方法中就可以直接调用self.b1
        self.b1=123
    def b(self):
        return self.b1
    def c(self):
        c1=self.b()+5#self.b()代表上面的b方法，由于b方法有返回值self.b1,所以这里可以写self.b()也可以写__init__下定义的self.b1
        print (c1,self.b1)
a=A()
a.c()
def a():
    m=10
    return m
def b():
    n=a()+1#如果不是在类中，不同函数互相调用直接引用函数名+()，如果在类中需要加self.函数名()
    print(n)
b()
#在不同类中互相调用方法
class p():
    def opq(self):
        print('这是第一步')
class o():
    def __init__(self):
        self.p=p()#引入另一个类
    def pq(self):
        self.p.opq()#执行另一个类中的方法
        print('这是第二部')
pp=o()
pp.pq()
#也可以使用继承类，例如
class r():
    def opq(self):
        print('这是第一步')
class m(r):
    def pq(self):
        super().opq()#也可以使用p().opq()
        print('这是第二部')
po=m()
po.pq()
class n():
    def __init__(self,ff):
        self.f=ff
    def __call__(self):#如果使用类装饰器，调用函数时必须用到__call__方法
        print('这时第一步')
        self.f()#注意self.f就等于pq(),因为下面@n可以理解成pq=n(pq),然后再init里有ff参数，ff就相当于pq,所以self.f=ff,执行self.f()就相当于执行pq()

@n
def pq():
    print('这是第二部')
pq()
class Demo(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def my_print(self,):
        print("a = ", self.a, "b = ", self.b)
#__call__将类的对象demo当作函数直接调用,demo()就等于__call__()
    def __call__(self, *args, **kwargs):
        self.a = args[0]
        self.b = args[1]
        print("call: a = ", self.a, "b = ", self.b)
demo=Demo(10,20)
demo.my_print()
demo(50,60,70)