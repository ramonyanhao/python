def fib(n):    # 定义到 n 的斐波那契数列
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()#换行
fib(1000)#这样指定参数n的值代表斐波那契数列共运行到n停止，不会运行n次斐波那契数列
def fib2(n): # 返回到 n 的斐波那契数列
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
print(fib2(100))

import sys,os
os.chdir(r'C:\\Users\\ramon\\AppData\\Local\\Programs\\Python\\Python37')
print(os.getcwd())
print(os.listdir())
print(open('二次方程.py', 'r').read(), end='\n')#这样写比较简单，省略了打开后读取的麻烦，直接一行代码，最后结果还是格式化输出end='\n'
#如果文件打开模式不是二进制模式打开，seek只允许从文件头开始计算相对位置，从文件尾计算时就会引发异常，可以把打开选项r改为rb
#还可以通过迭代一个文件对象读取
with open('二次方程.py', 'r') as f:
    for ff in f:#这里也可以使用f.readlines()函数，把数据读取成一个列表，然后for遍历这个列表，输出结果一样
        print(ff,end='')
