class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __repr__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self,other):
        if other.__class__ is Vector:
            print(type(other),type(other.a),type(self.a))
            return Vector(self.a + other.a, self.b + other.b)
        elif other.__class__ is int:
            print(type(other),type(self.a))#type(other)就是other.__class__
            #print(self.__class__.__name__)#__class__就是type()查看对象类型，如果使用self.__class__.__name__就是类的名称
            return Vector(self.a+other,self.b+other)

    def __radd__(self,other):
        """反向算术运算符的重载
        __add__运算符重载可以保证V+int的情况下不会报错，但是反过来int+V就会报错，通过反向运算符重载可以解决此问题
        """

        if other.__class__ is int or other.__class__ is float:
            #print(type(other))
            return Vector(self.a+other,self.b)
        else:
            raise ValueError("值错误")

    def __iadd__(self,other):
        """复合赋值算数运算符的重载
        主要用于列表，例如L1+=L2,默认情况下调用__add__，会生成一个新的列表，
        当数据过大的时候会影响效率，而此函数可以重载+=，使L2直接增加到L1后面
        """

        if other.__class__ is Vector:
            return Vector(self.a + other.a, self.b + other.b)
        elif other.__class__ is int:
            return Vector(self.a+other,self.b)
v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)#使用v1+v2代表__add__的参数other类型为Vector
print (v1+4)#如果使用v1+4代表__add__的参数other类型为int,所以__add__中使用if，elif语句控制这里的输出
print (6+v2)#使用int+实例就需要有__radd__
