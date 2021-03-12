# 如果没有__call__方法，类的实例对象是不可调用的，有了__call__方法，类的实例对象就可以像函数那样直接调用，并且调用时指定的参数就是__call__中的参数，例如下面的类实例对象my
class myclass:
    def __init__(self,size,x,y):
        self.x,self.y=x,y
        self.size=size
        print('类在这里',size,x,y)
    def __call__(self,x,y):#call方法可以修改类参数,__call__就是把类的实例对象改为可调用对象，像函数那样
        self.x,self.y=x,y
        print('call在这里',self.size,self.x,self.y)
    def __str__(self):
        return "str作用是只要通过print打印类，都会自动执行str的返回值，例如print(my)" # 重要的一点就是str和repr返回的必须是字符串类型，不能返回整数，元组，列表之类的
    def __repr__(self):
        return "repr作用时通过执行类的实例，自动指定repr返回值，例如直接执行my"# repr作用和str一样，两个函数同时存在，优先执行__str__函数
    def speak(self):
        print('speak func is here!',self.x,self.y,self.size)
my=myclass(1,2,3)#类实例化把1,2,3传参给size,x,y
print(my)#通过str方法这里打印的是str的返回值，如果没有str,这里打印的是myclass的内存地址<__main__.myclass object at 0x000001772C3C1488>
my#通过repr方法这里打印的是repr的返回值，如果没有repr,这里打印的是myclass的内存地址<__main__.myclass object at 0x000002B242F95808>
my(10,20)#把上面的2,3通过call再调用my实例改变为10,20.而且call可以直接调用类实例，不需要像下面类名.函数名一样调用,需要注意call的参数只有x,y，所以这里之更改了x,y的值
my.speak()#call可以把类变为函数那样来调用，如果没有call,类的实例化对象是不可调用的
from functools import wraps
#类装饰器
#当前目录下会生成一个日志文件:out.log,内容就是最下面函数名+was called
class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)#wraps作用是当运行myfunc1.__name__时，返回值为wrapped_function,这样容易引起混乱，使用wraps返回值就是myfunc1
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile并写入
            with open(self.logfile, 'a') as opened_file:
                # 现在将日志打到指定的文件
                opened_file.write(log_string + '\n')
            self.notify()#这里目前什么都不做，和下面的notify函数对应，内容为pass,表示先占用这块位置，以后如果需要再添加内容
            return func(*args, **kwargs)#func这个参数就是下面的myfunc1函数

        return wrapped_function

    def notify(self):#以后这里可以添加把这个日志发送邮件给管理员
        pass
@logit()#类装饰器，相当于执行了logit(myfunc1),类中的call函数func参数就变成了myfunc1函数
def myfunc1():
    pass
myfunc1()#通过call函数直接调用类实例化，执行myfunc1()就等于执行了myfunc1=logit.__call__(myfunc1)
 # call可以用在装饰器，当执行myfunc1()时就是在执行call
@logit(logfile='func2.log')#可以改变类参数,生成一个func2.log的日志文件，内容为myfunc2 was called
def myfunc2():
    pass
myfunc2()