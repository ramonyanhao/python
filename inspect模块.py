import inspect
'''
inspect模块主要提供了四种用处：

　　1.对是否是模块、框架、函数进行类型检查

　　2.获取源码

　　3.获取类或者函数的参数信息

　　4.解析堆栈
'''
def add(x:int,y:list,z:str) -> tuple:  # ->tuple代表这个函数最后预计的返回值类型为元组，可以通过__annotation__来查看
    pass
print(add.__annotations__)  # annotations是字典类型，存储了函数中所有的被注解的形参名，“值”为注解的内容
sig=inspect.signature(add)  # inspect.signature 获取签名对象，包括函数名，参数等
print(sig)
param=sig.parameters  # 获取签名中的参数,返回有序字典
print(param)
for k,v in param.items():
    print(k,v)
print(sig.return_annotation)
import newtile10
print(inspect.getsource(newtile10.Person))  # inspect.getsource查看源代码
print(inspect.getsourcelines(add))