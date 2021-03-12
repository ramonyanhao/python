import sys
#使用生成器yield
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        print('%d,%d' % (a,b))
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成

'''while True:#使用while True循环输出
    try:
        print (next(f), end=" ")
    except:
        sys.exit()'''#如果使用sys.exit()会引发一个异常：SystemExit，如果这个异常没有被捕获，那么python解释器将会退出，目前没有捕获，解释器直接退出，后面的代码都不执行
# 如果有捕获此异常的代码，那么这些代码还是会执行。捕获这个异常可以做一些额外的清理工作。0为正常退出，其他数值（1-127）为不正常，可抛异常事件供捕获。


for i in range(11):#结果可以使用for循环输出，for循环不使用变量i，不过也可以循环10次下面的代码
    print(next(f),end=" ")


for i in fibonacci(11):#或者直接使用生成器迭代器循环输出
    print(i,end=" ")
import sys
#不适用生成器yield
def fibonacc(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        #yield a
        a, b = b, a + b
        print('%d,%d' % (a,b))
        counter += 1
ff = fibonacc(10) # f 是一个迭代器，由生成器返回生成

while True:#使用while True循环输出
    try:
        print (next(ff), end=" ")
    except :
        sys.exit()