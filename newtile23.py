def hi(name="yasoob"):
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "yasoob":
        return greet#记住这里返回函数后面没有加(),返回greet的内存地址
    else:
        return welcome#如果加了()返回welcome函数的运行结果
print(hi)#返回hi的内存地址
print(hi())#这里应该返回hi的运行结果，可是函数return返回的是greet没有加(),所以这里得到的结果是greet的内存地址
a=hi()
print (a)#这里同样得到greet的内存地址，主要是hi函数有默认参数name=yasoob,所以根据if条件得到返回greet
print(hi(name='test'))#如果把hi默认参数更改，根据条件返回welcome
print(hi()())#一个函数里返回的是另外一个函数，就可以用两个括号，通过hi()函数返回greet()函数
def a(a_func):
    print("before func")
    a_func()
    print("after func")
def b():
    print("remove")
a(b)#在a函数里使用参数返回b函数的代码，但是这样会有一个短板，就是在调用的时候必须使用a(b)才可以调用
c=a(b)#如果使用变量的话只可以调用一次，然后这个变量就会返回none，原因是变量值占用的内存地址就是函数a(b)的内存地址
#如果改成这样
def a(a_func):
    def b():
        print("before func")
        a_func()
        print("after func")
    return b
@a#@a相当于c=a(b),最后执行c()调用函数，函数c和a都会运行
def c():
    print("remove")
c()#c()函数调用多少次都可以，原因是a函数嵌套了b函数，调用时变量c占用的是a函数内存地址，实际代码都在b函数中，所以不会有冲突


