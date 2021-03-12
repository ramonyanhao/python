'''
实例方法

    定义：第一个参数必须是实例对象，该参数名一般约定为“self”，通过它来传递实例的属性和方法（也可以传类的属性和方法）；

    调用：只能由实例对象调用。

类方法

    定义：使用装饰器@classmethod。第一个参数必须是当前类对象，该参数名一般约定为“cls”，通过它来传递类的属性和方法（不能传实例的属性和方法）；

    调用：类对象或实例对象都可以调用。

静态方法

    定义：使用装饰器@staticmethod。参数随意，没有“self”和“cls”参数，但是方法体中不能使用实例方法的任何属性和方法；

    调用：类对象或实例对象都可以调用。
'''
class ClassTest(object):#类方法是将类本身作为对象进行操作的方法
    __num = 0

    @classmethod
    def addNum(cls):
        cls.__num += 1

    @classmethod
    def getNum(cls):
        return cls.__num

    # 这里我用到魔术方法__new__，主要是为了在创建实例的时候调用累加方法。
    def __new__(cls):
        ClassTest.addNum()
        return super().__new__(cls)


class Student(ClassTest):
    def __init__(self):
        self.name = ''

a = Student()
b = Student()
print(ClassTest.getNum())
#----------------------------------------------------------------------
class ClassTest(object):#也可以使用实例方法，通过这两种方法可以看出实例方法和类方法基本一样，只不过类方法传递的时类属性，实例方法传递的实例化以后的属性
    __num = 0

    def addNum(self):
        self.__num += 1


    def getNum(self):
        return self.__num

    # 这里我用到魔术方法__new__，主要是为了在创建实例的时候调用累加方法。
    def __new__(cls):
        ClassTest.addNum(cls)
        return super().__new__(cls)


class Student(ClassTest):
    pass

a = Student()
b = Student()
print(a.getNum())
#通过实例定义的变量只能被实例方法访问，而直接在类中定义的静态变量(如本例的name变量)即可以被实例方法访问，也可以被静态方法和类方法访问。
# 实例方法不能被静态方法和类方法访问，但静态方法和类方法可以被实例方法访问。
#例如
import time

class TimeTest(object):
    a=1
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @staticmethod
    def showTime():#这个showTime函数和类其他函数或者属性都不挨着，所以它是个独立的个体，也可以在类外面写这个函数，但是这样不利于维护
        print(TimeTest.a)#静态方法和类方法中想要访问类中的变量使用类名.属性名就可以，例如变量a(注意静态方法和类方法不可以访问实例方法中的变量__init__下的或者self.变量）
        return time.strftime("%H:%M:%S", time.localtime()) # 静态方法返回值和类TimeTest完全没关系，不是类中的参数，就是返回当前时间


print(TimeTest.showTime())
t = TimeTest(2, 10, 10) # 传入参数2,10,10
nowTime = t.showTime() # 其实这个静态方法showTime放在类外面运行也可以，只不过这样不好维护
print(nowTime) # 最后执行的结果还是当前时间，和之前传入的2,10,10完全没关系