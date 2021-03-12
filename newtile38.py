# 类定义
#情况一：子类需要自动调用父类的方法：子类不重写__init__()方法，实例化子类后，会自动调用父类的__init__()的方法。
#情况二：子类不需要自动调用父类的方法：子类重写__init__()方法，实例化子类后，将不会自动调用父类的__init__()的方法。
#情况三：子类重写__init__()方法又需要调用父类的方法：使用super关键词或者父类名+self参数
class A:
    def add(self, x):
        y = x + 1
        print(y)


class B(A):
    def add(self, x):
        super().add(x)#或者A.add(self,x)，python2.x使用super(子类名,self).add(x)


b = B()
b.add(2)  # 3
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 单继承示例
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        people.__init__(self, n, a, w)# 调用父类的构函，这里使用的是父类名.__init__,也可以使用super().__init__(self,n,a,w)
        self.grade = g

    # 覆盖父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


# 另一个类，多重继承之前的准备
class speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


# 多重继承
class sample(speaker, student):
    a = ''
#super()是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。
#super()会查找所有的超类，以及超类的超类，直到找到所需的特性为止,而使用父类名只会查找上一级的超类
    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)#这里可以简写成super().__init__(n,t)
test = sample("Tim", 25, 80, 4, "Python")
super(student,test).speak()#用子类对象student调用父类people已被覆盖的方法
test.speak()  # 方法名同，默认调用的是在括号中排前地父类的方法，例子中括号里排前的是speaker,所以这里调用的是speaker类里的speak方法