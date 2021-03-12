def test1():
    print('test1-1')
    print('num')
    print('test2-2')
def test2():
    print('test2-1')
    test1()
    print('test2-2')
def test3():
    try:
        print('test3-1')
        test1()
        print('test3-2')
    except Exception as result:
        print('检测出异常{}'.format(result))
    print('test3-2')
test3()#执行test3函数，再test3中首先打印test3-1,然后调用test1函数，先打印除test1-1.然后再test1中发现异常，没有找到num变量，然后打印出test3-2
print('-------------')
test2()#执行完test3再执行test2函数，打印出test2-1,然后再test2里发现需要再执行test1函数，打印出test1-1后发现错误没有找到num变量，但是由于test2里没有try和except所以不会处理异常，程序结束