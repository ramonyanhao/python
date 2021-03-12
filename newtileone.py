outerVar = "this is a global variable"


def test():
    innerVar = "this is a Local variable"
    print(outerVar)# 函数里面没有，就去外边找


    return (innerVar,n,10//2)
n = 10


#a=test()如果这里也执行了和if__name__=='__main__'一样的代码，则这段代码会在结果中出现两次
#print(a)所以建议把需要执行的代码最好写入if__name__=='__main__'下面

def test1():
    innerVar = "this is a Local variable"
    return innerVar
#print(test1())#return的返回值在脚本中需要用print才可以显示出来
    #return (innerVar,n)#没有return返回值为none
    #return test1()如果return返回函数自己将造成死循环
    #return test()#可以返回前面自定义创建的函数

if __name__ == '__main__':#这里很重要，可以把最终想要执行的代码写在这里，如果在上面也写入了同样需要执行的代码，则这段代码会执行两次
   # a=test()#给函数变量，脚本模式中函数return必须通过print才可以调用出来，交互模式不需要
    print(test())#调用函数时，函数内部必须用return有返回值才可以调用，否则没有return函数时，调用结果返回none和函数内部可执行的命令如print



