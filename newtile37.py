#类的第一个参数self 代表的是类的实例，代表当前对象的地址，而 self.__class__ 则指向类
class Test:
    def prt(self):
        print(self)
        print(self.__class__)

#注意self不是关键字，可以用其他任何字符串代替
t = Test()
t.prt()
#__init__() 方法可以有参数，参数通过 __init__() 传递到类的实例化操作上
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
print(x.r, x.i)   # 输出结果：3.0 -4.5
#在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例
# 类定义
class people:
    # 定义基本属性,就是类属性，类属性在所有类实例中共享，类属性定义在类中，方法之外，例如在每增加一个实例化类时，类属性count增加1
    count=0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w
        people.count+=1

    def speak(self):
        print("%s 说: 我 %d 岁。有%d人" % (self.name, self.age,people.count))
# 实例化类
p = people('runoob', 10, 30)
p.speak()
e=people('ramon',20,50)
e.speak()