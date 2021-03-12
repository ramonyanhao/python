import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
        print('before') # 捕获到bar('0')报错，程序跳到except中执行，跳过了print(before)
    except Exception as e:
        print(e)
        logging.exception(e) # 输出错误堆栈好排查问题,如果没有logging，最后输出的只是捕获的错误e,不会有错误跟踪，在第几条语句产生错误
    print('end') # 捕获错误后end还是会输出，如果没有捕获错误，程序执行到bar('0')就会报错，后面end就不会输出
main()

# 如果没有捕获异常，程序报错后就会终止，捕获异常后程序执行到错误的地方报错然后继续往下执行,需要注意的地方在try里如果有错误被捕获了，try从出错的地方往下的语句都不会执行，程序会跳到符合捕获错误条件的地方执行
def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise # 把错误又原样抛给了foo函数执行，最终打印出foo的raise语句：ValueError: invalid value: 0
        # raise语句如果不带参数，就会把当前错误再原样抛出
bar()
# 在except中raise一个Error，还可以把一种类型的错误转化成另一种类型，例如:
try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!') # 把ZeroDivisionError错误类型通过raise转化为ValueError错误类型

# 启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态
# 在命令行运行python -m pdb base.py
# pdb.set_trace()相当于pycharm的断点，可以用在程序会出错的地方，例如：
import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)