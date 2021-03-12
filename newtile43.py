class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):#打印一个实例化对象时，打印的是一个对象的地址,而通过__str__()函数就可以帮助我们打印对象中具体的属性值
        return 'Vector (%d, %d)' % (self.a, self.b)
#python中调用print()打印实例化对象时会调用__str__()如果__str__()中有返回值，就会打印其中的返回值
    def __add__(self, other):#__add__让自定义的类生成的对象(实例)能够使用运算符进行操作
        print(type(other),type(other.a),type(self.a))
        return Vector(self.a + other.a, self.b + other.b)
v1 = Vector(2,10)#这里的参数2,10,5,-2,10,20代表的都是__init__下的a和b
v2 = Vector(5,-2)#但是在__add__下有一个参数other,这样就有另一层关系other.a和other.b
#在__add__返回值中定义了self.a+other.a,self.b+other.b，所以在运算时2+5+10和10-2+20可以把2看成a,5和10看成other.a,10看成b,-2和20看成other.b
print (v1 + v2)#如果没有__str__这里输出的是一个内存地址，有__str__这里输出的是str下面的返回值,__str__叫函数重载
class Classname:
    @staticmethod#静态方法可以没有参数，可以直接使用类名调用
    def fun():
        print('静态方法')

    @classmethod#默认有个 cls 参数，可以被类和对象调用
    def a(cls):
        print('类方法')

    # 普通方法，默认有个self参数，且只能被对象调用
    def b(self):
        print('普通方法')
Classname.fun()
Classname.a()
aa=Classname()#实例化类给一个对象aa,或者直接使用Classname().b()也可以
aa.b()