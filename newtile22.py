#函数也可以以一个函数为其参数:

def hello () :
  print ("Hello, world!")

def execute(f):
  "执行一个没有参数的函数"
  f()#执行函数excute里的参数f,通过执行f()把参数f变为函数

execute(hello)#execute函数里执行的代码是f(),所以这里hello不用加()就可以执行了
hello()
print(execute.__doc__)#__doc__打印出函数里三个引号注释的内容
def log(pr):#将被装饰函数传入
    def wrapper():
        print("**********")
        return pr()#执行被装饰的函数
    return wrapper#将装饰完之后的函数返回（返回的是函数名）
@log#相当于pr=log(pr),@xxxx的作用，就是执行XXXX(并将下面的函数作为参数)
def pr():
    print("我是小小洋")
pr()
print(pr.__name__)#这里显示名称应该是pr，但是结果是wrapper,这是因为pr=log(pr),在log函数里有嵌套了wrapper函数，log函数return返回的也是wrapper,所以这里查看名字结果就是wrapper
#这个问题可以用wraps解决
from functools import wraps
def log(pr):#将被装饰函数传入
    @wraps(pr)#wraps函数可以保留原有函数的名称和文档字符串(就是通过三引号注释过的文字）
    def wrapper():
        print("**********")
        return pr()#执行被装饰的函数
    return wrapper#将装饰完之后的函数返回（返回的是函数名）
@log#相当于pr=log(pr),@xxxx的作用，就是执行XXXX(并将下面的函数作为XXXX的参数)
def pr():
    print("我是小小洋")
pr()
print(pr.__name__)
