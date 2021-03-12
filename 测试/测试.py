def func_dec(func):
    def wrapper(*args):
        if len(args) == 2:
            func(*args)#相当于运行add_sum函数
        else:
            print('Error! Arguments = %s'%list(args))
    return wrapper

@func_dec
def add_sum(*args):
    print(sum(args))

# add_sum = func_dec(add_sum)
args = range(1,3)
add_sum(*args)
class TASKS:
    class FUNC:
        def __init__(self,a,b):
            self.a = a
            self.b = b
        def Add(self):
            x = self.a + self.b
            return x
        def Sub(self):
            y = self.a - self.b
            return y

    @staticmethod
    def tsk1():#静态方法可以调用类中的属性和方法
        PrintObj1 = TASKS.FUNC(10,20)
        print(PrintObj1.Add())

    def tsk2(self):
        PrintObj2 = self.FUNC(100,50)
        print(PrintObj2.Sub())
TASKS.tsk1()
obj = TASKS()
obj.tsk2()
obj.tsk1()
