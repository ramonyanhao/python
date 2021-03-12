# 开闭原则：给程序修改，关闭功能时不用修改程序的源代码，例如下面,不符合开闭原则使用了isinstance来判断程序的走向,如果需要新增一个功能，Person就需要增加一条判断语句
# 符合开闭原则创建了各个类中的统一方法transport，使用这个方法就可以不修改Person代码，直接增加功能，只要注意增加的新类里面创建方法时使用Person定义的名称transport就可以
# 老张开车去东北
# 需求变化：坐飞机 | 坐火车 | 骑车
class Person:
    def __init__(self, name):
        self.name = name

    def go_to(self, position, type):
        print('去：' + position)

        # 判断怎么走
        # 如果是飞机就飞,用isinstance()判断该对象是否属于该类
        if isinstance(type, Car):
            type.run()
        # 如果是车就跑
        # 这里修改了代码，违反了面向对象的开闭原则,如果后面需要增加其他的类，这里就需要再增加一个判断条件
        elif isinstance(type, Airplane):
            type.fly()


# 这个类只有一个run功能，满足设计原则：类的单一职责，一个类有且只有一个改变它的原因
class Car:
    def run(self):
        print('走你~')


# 添加坐飞机的类，属于加功能，不违反开闭原则，开发时一个类为一个单元
class Airplane:
    def fly(self):
        print('嗖~')


c01 = Car()
lz = Person('老张')
lz.go_to('东北', c01)  # 打印出  '去：东北'  '走你~'

a01 = Airplane()
lz.go_to('东北', a01)  # 打印出 '去，东北'  '嗖~'
# 修改这个程序，符合开闭原则
class Person:
    def __init__(self, name):
        self.name = name

    def go_to(self, position, type):
        print('去：' + position)
        type.transport(position)  # 符合开闭原则：对修改关闭,增加新功能，不改变原有代码，原因是这里的transport为下面各类中的方法，只要在新增的类中定义这个方法就可以不用修改Person下的代码了
class Car():
    # 继承，对父类的方法进行重写
    def transport(self, position):
        print('开车到', position)


# 对扩展开放
class Airplane:
    # 继承，对父类的方法进行重写
    def transport(self, position):
        print('飞到', position)


# 之后要使用什么交通工具，只要写该交通工具的类就行了,例如：
class Bike:# 如果使用的静态语言(例如java),这里必须要有继承父类，否则无法调用transport方法，而python属于动态语言，所以这里可以不用继承父类，只需要确定有transport这个方法就可以
    def transport(self, position):
        print('骑车到', position)

c01 = Car()
a01 = Airplane()
b01 = Bike()
lz = Person('老张')
lz.go_to('东北', a01)  # print: '去：东北'  '飞到 东北'
lz.go_to('东北', c01)
lz.go_to('东北', b01)
