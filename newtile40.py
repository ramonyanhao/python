class Parent:  # 定义父类
    def myMethod(self):
        print('调用父类方法')


class Child(Parent):  # 定义子类
    def myMethod(self):
        #super().myMethod()#也可以写在这里
        #Parent.myMethod(self)#也可以这样写代替super
        print('调用子类方法')
        super().myMethod()  # 用子类对象调用父类已被覆盖的方法
        Parent().myMethod()#也可以直接调用父类方法

c = Child()  # 子类实例
c.myMethod()  # 子类调用重写方法
super(Child,c).myMethod()#在子类外调用父类被覆盖的方法，需要加子类名称Child和实例对象c