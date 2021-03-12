#为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加
class Student(object):
    count = 0# 类属性，可以被下面所有的方法访问，如果使用self.count代表类实例化对象中的属性,例如下面的bart和lisa就是self，使用Student.count代表类本身的属性

    def __init__(self, name):
        self.name = name# self代表类的实例化对象,例如这里的self就是下面给类实例化后的对象bart和lisa
        self.count += 1#这里是实例化对象属性，区别就是self.count是属于每个实例化对象中的属性例如:bart.count和lisa.count，self.count只在每个实例对象中计算
        Student.count+=1#这里是类属性count，每增加一个实例化对象，这个属性就增加1，Student.count是属于整个类的属性
        print('self.count:',self.count,'Student.count:',Student.count)
# 直接使用类属性(Student.count)测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
Student.count=0# 把类属性归零
# 使用实例属性(self.count)测试：
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if bart.count != 1:#这里就是和上面的区别，在比对的时候这里使用的是实例化对象属性bart.count,类属性只是用Student.count就可以了
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if lisa.count != 2:#这里就是和上面的区别，在比对的时候这里使用的是实例化对象属性lisa.count
            print('测试失败!')
        else:
            print('实例化对象中的lisa.count:', lisa.count,'实例化对象中的bart.count:',bart.count)
#bart是第一个实例对象，所以bart.count的值是1，lisa是第二个实例对象，lisa.count的值是2，所以Student.count和self.count区别就是self.count是根据实例化对象来计算的，而Student.count是整个类的通用属性
            print('测试通过!')