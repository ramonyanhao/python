class Vector:#这个例子比较清楚一些，修改下面的print会影响__add__中的other类型
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        if other.__class__ is Vector:
            print(type(other),type(other.a),type(self.a))
            return Vector(self.a + other.a, self.b + other.b)
        elif other.__class__ is int:
            print(type(other),type(self.a))
            return Vector(self.a + other, self.b)
v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)#other类型是Vector
print(v1+56)#other类型是int,这样才可以+56得出结果


