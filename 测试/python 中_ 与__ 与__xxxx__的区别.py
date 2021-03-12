'''
_代表私有属性，表示只能再函数内部可以访问这个属性，但是实际上外部也可以访问，不会报错，只是不符合标准语法
__双下划线代表私有属性，只能再函数内部访问，函数外部不能访问，会报错，其实主要作用是避免再类继承时子类重写父类方法，例如
下面的函数中，类B继承类A，运行时类A可以直接通过a=a()实例化，然后a.run运行a here，注意__a函数只能在类A中调用，而且不可以通过实例化a.__a()来调用
需要在类中创建另一个函数run来调用这个__a,私有属性也是一样，比如__pri,想要在函数内部调用这个私有属性，需要使用self.__pri,在外部或者继承的子类也不可以访问父类__pri
'''
class A():
    __pri='私有属性'#只能在A类内部通过self.__pri调用，不能再子类或外部调用这个属性
    def __a(self):
        print('a here')
    def run(self):
        print(self.__pri)
        return self.__a()
class B(A):
    def __a(self):
        print('b here')
    def run(self):#如果在子类中创建函数run来运行__a,这样B类就不会继承A类,run函数和__a就可以看成为B类自己的方法，不是从A类继承过来的
        self.__a()#如果B类没有run,使用从父类A继承过来的run方法,B类里的__a是不允许覆写父类A里的__a,也包括不允许访问父类A里的__pri
class C(A):
    def __a(self):
        print('c here')
if __name__ == "__main__":
    a=A()
    a.run()
    b=B()
    b.run()#B类通过使用自己的run方法，输出b here
    c=C()
    c.run()#C类通过使用从A继承过来的run方法,不允许覆写父类A中的__a，最后输出还是a here
'''
__name__双下划线开头和结尾属于魔法方法，当看到这种类型的方法时不要调用它，因为它是通过python来调用的，例如
'''
class number():
    def __init__(self,n):#__init__当类number()被实例化时，python自动调用__init__里面的属性
        self.n=n
    def __add__(self,other):#当使用num+5时，python自动调用__add__,不用写成num.__add__(5)
        return self.n+other
    def __sub__(self,other):
        return self.n-other
num=number(10)
print(num.__add__(5))
print(num-5)
class A(object):

    def __init__(self, x):
        self.__a = -2
        self.x = x
    def __call__(self,a):#如果外部想要访问或者更改内部私有属性a，可以使用call方法，例如外部执行a(10)直接使用类实例化对象a传参10给call中的变量a就可以更改私有属性
        self.__a=a
    def get_a(self):#除了使用call方法更改私有属性a的值，还可以创建自定义方法，返回私有属性a的值,例如:a=A(10),a.get_a返回私有属性__a的值为-2
        return self.__a
    def set_a(self,a):#或者创建自定义方法更改私有属性a的值,例如:a=A(10),a.set_a(2)更改私有属性__a的值为2
        self.__a=a
    def __b(self):#需要注意的地方是只要在init中设置了私有属性的值，外部不管如何更改都是更改的实例化对象中私有属性的值，类中的值还是不变
        # 例如实例化a(10),更改私有属性a的值a.set_a(5)或者a(5)使用call方法更改a的值为5,在实例化对象a中私有属性__a的值是5，但是在类A中__a的值还是-2
        self.x=3
        return self.x
a=A(2)#给类实例化对象并传入x的值
print(a._A__a)#a._A__a访问私有属性的值为-2,如果执行a(10)就会调用call方法，把私有属性a的值改为10，Python解释器对外把__a变量改成了_A__a，所以，仍然可以通过_A__a来访问__a变量
print(a._A__b())#私有属性或私有方法一般不允许外部直接访问或修改，但是可以实例化类后调用，但后面需要跟类名如:实例化名._类名__私有属性或私有方法，例如:a._A__b()访问私有方法
def abc(a=1,b=2,c=3):
    return a,b,c
print(abc())
print(abc()[1])#return返回的是元组，如果想调用a,b,c其中一个参数，可以通过下标来取出b的值
a,b,c=abc()#也可以用3个变量a,b,c去接收返回值
print(a,b,c)
_,b,_=abc()#或者可以使用_代替不需要的值，然后值取b的值,_可以看成是一个变量名字，最后_的值是3，因为最后_替换了第一个_的值
print(_,b,_)
