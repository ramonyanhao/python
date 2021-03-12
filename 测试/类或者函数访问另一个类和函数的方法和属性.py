class A:
    f=100
    print('类下面的属性为全局属性可以直接访问打印')
    def __init__(self):
        self.b=10
    def c(self):
        self.f=20
class AA:#这个AA类下面的属性直接使用，不需要实例化
    a=A()
    print(a.b)#init方法在类被实例化后就可以访问里面的属性了
    a.c()#这里是重点，一定要先执行这个类方法，才能访问里面的变量，执行这个类方法就好比先要给f变量赋值，才可以使用
    print(a.f,A.f)

#还有一种方法是现在类中设置一个变量，然后在下面的方法中使用这个变量,就不需要用self,例如：
class B:
    f=30
    def __init__(self):
        self.b=10
    def c(self):

        b.f=20#就不需要用self直接使用实例化的b来访问这个局部变量
        e=0
        return e
b=B()
print(b.b,b.f)
print(b.c())#这里是重点，一定要先执行这个类方法，才能访问里面的变量，执行这个类方法就好比先要给f变量赋值，才可以使用
print(b.f,B.f)#如果使用实例化的b.f就是方法C中的属性，如果直接使用类B.f就是类下面的变量f
#在不同函数之间调用属性可以通过全局变量global
def num():
    global n#全局变量n
    n=5
def mun():
    num()#执行函数num,从而在这里生成全局变量n
    print('函数调用另一个函数中的变量：',n+1)
mun()
n+=2#在函数外面可以更改全局变量n的值，在函数内部不可以更改
print('外部调用函数局部变量n：',n)
#把一个函数当作另一个函数的参数来调用
def fun(x):
    n=5
    return x+n
def func():
    number=4
    return number
print(fun(func()))
#使用闭包
def fu(f):
    n=5
    def uf():
        nonlocal n,f#可以在局部变量改变外部变量的值
        while f>0:
            n+=1
            f-=1
        return n
    return uf # 如果闭包在这里加()，代表函数fu直接返回函数uf的运行结果，外部不管调用多少次fu()都只会返回一个结果，如果没有(),代表函数fu返回函数uf,外部给fu()实例化后运行一次执行一次uf函数，并把结果固定在__closure__
k=fu(10)
print(k())


