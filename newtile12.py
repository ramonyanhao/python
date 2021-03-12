import sys
def mye( level ):
    if level < 1:
        raise Exception("Invalid level!",level)
        # 触发异常后，后面的代码就不会再执行
try:
    mye(0)            # 触发异常
except Exception as err :#这里就相当于给上面的raise主动触发异常的字段("Invalid level!",level)加变量err
    print (err)
    print (sys.exc_info())#如果使用这个函数可以去掉上面的as err语句，直接处理异常
    print (sys.exc_info()[1])#使用sys.exc_info()[1]代替err变量也可以得到相同结果
else:
    print (2)
finally:#如果一个异常在 try 子句里（或者在 except 和 else 子句里）被抛出，而又没有任何的 except 把它截住，那么这个异常会在 finally 子句执行后被抛出
    print('最终结果') # 所以finally不管前面有任何异常或者没有异常，finally结果和前面的异常都会在这里执行出来
#sys.exc_info()返回的值是一个元组，其中第一个元素，exc_type是异常的对象类型，exc_value是异常的值，exc_tb是一个traceback对象，对象中包含出错的行数、位置等数据。
