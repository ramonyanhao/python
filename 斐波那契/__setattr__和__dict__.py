# 实例属性管理__dict__:每次实例属性赋值时，都会将属性名和对应值存储到__dict__字典中
class fun:
    def __init__(self):
        self.name='harmon'
        self.age=35
a=fun()
print(a.__dict__) # init中定义的实例属性都赋值再__dict__字典中
# 在类实例的每个属性进行赋值时，都会首先调用__setattr__()方法，并在__setattr__()方法中将属性名和属性值添加到类实例的__dict__属性中
class fun:
    def __init__(self):
        self.name='harmon'
        self.age=35
    def __setattr__(self,key,value):
        pass
b=fun()
print(b.__dict__)

# 由于每次类实例进行属性赋值时都会调用__setattr__()，所以可以重载__setattr__()方法，来动态的观察每次实例属性赋值时__dict__()的变化
class fun:
    def __init__(self):
        self.name='harmon'
        self.age=35
    def __setattr__(self, key, value):
        self.__dict__[key]=value # 必须要加这句，表示把实例属性的键和值添加到dict中
c=fun()
print(c.__dict__)
c.company='memebox'
print(c.__dict__)
class A(object):
    def __init__(self,name='Wang'):
        # 此处的赋值其实是触发了__setattr__
        self.name = name

    # 当对象调用一个不存在的属性，才会触发
    def __getattr__(self, item):
        print('使用getattr',item)
        return self.__dict__

    # 添加和修改属性会触发此方法
    def __setattr__(self, key, value):
        print('使用setattr',key,value)
        self.__dict__[key] = value
        # 不能用下面的方法，因为self.key本身就调用了__setattr__方法，然后无限递归报错
        # self.key = value

a = A()

# 新建一个属性并赋值，调用__setattr__方法
a.hello = 'Hi'
print(a.hello)

# 调用一个不存在的属性，调用__getattr__方法
print(a.world)

