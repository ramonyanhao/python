class Test:
    def func(self,message):
        print (message)
object1=Test()#object1=Test()生成一个实例，object1.func返回一个绑定的方法，把实例object1和方法func绑定。
x=object1.func('ok')#如果没有self参数，正常调用类方法为Test.func(object1,'ok'),但是在调用这个方法的时候你不用为self参数赋值，Python会自动绑定self到实例object1
t=Test.func#而Test.func是用类去引用方法，我们得到一个未绑定的方法对象。要调用它就得传一个实例参数，如t(object1,'未绑定的方法对象，需要传递一个实例')
t(object1,'未绑定的方法对象，需要传递一个实例')#这里传入一个实例参数，self就等于object1,后面的字符串就等于message,这里的object1再上面已经赋值object1=Test()
#大多数时候，我们都直接调用方法，所以一般不会注意到方法对象。但是如果开始写通用的调用对象的代码时，需要特别仔细地注意未绑定方法，它们需要地传一个实例参数
class Demo(object):#如果这里加object代表类Demo继承了object模块里的所有方法
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def my_print(self,):
        print("a = ", self.a, "b = ", self.b)

    def __call__(self, *args, **kwargs):#__call__可以让类Demo实例化后再调用，如果没有__call__不能调用实例化类，主要实现的是将类的对象当作函数直接调用
        self.a = args[0]
        self.b = args[1]
        print("call: a = ", self.a, "b = ", self.b)
if __name__ == "__main__":
    demo = Demo(10, 20)
    d=Demo(100,200).my_print()
    d#或者再my_print后面加括号，直接输出d也可以
    demo.my_print()#想要调用类下的函数需要实例化类demo再加.函数名，如果直接用d=Demo(10,20).my_print未绑定方法,输出d()的结果是一样的
    demo(50,60)#输出__call__下面的代码，如果没有__call__,这句报错无法调用'Demo'对象


class Tag:
    def __init__(self):
        self.change = {'python': 'This is python',
                       'php': 'PHP is a good language'}

    def __getitem__(self, item):#按照索引获取值
        print('调用getitem')
        return self.change[item]

    def __setitem__(self, key, value):#按照索引赋值
        print('调用setitem')
        self.change[key] = value


a = Tag()
print(a['php'])
a['php'] = 'PHP is not a good language'
print(a['php'])
