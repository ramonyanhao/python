# 获取用户输入的数字
num = int(input("请输入一个数字: "))
factorial = 1
fa=[]
# 查看数字是负数，0 或 正数
if num < 0:
    print("抱歉，负数没有阶乘")
elif num == 0:
    print("0 的阶乘为 1")
else:
    for i in range(1, num + 1):
        factorial *= i#factorial值是1，这里表示1*i,i的值是1,2,3到num+1,num值是3，这里表示1*1*2*3=6,最终3的阶乘就是6
        fa.append(factorial)
    print("%d 的阶乘为 %d" % (num, factorial))
    print(fa)

from functools import reduce
i=int(input("请输入一个数字: "))
sum=reduce(lambda x,y:x*y,range(1,i+1))#reduce()函数会对参数序列中元素进行累积，函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
# 用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
print(sum)


def factorial(n):
    if n > 1:#n=5，这里条件ifn>1，通过下面的while True循环中的调用函数x=factorial(n),n的值为2,3,4,5形成递归factorial(n)
        return n*factorial(n-1)#当n=5时，5*(5-1)*（4-1）*（3-1）*（2-1）当n的值为1时条件ifn>1不成立，退出
    return 1
while True:
    try:
        n = input("请输入一个数字(输入 q 退出):")
        if n == "q":
            break
        n = int(n)
        if n < 1:
            raise ValueError
        x = factorial(n)
        print(x)
    except ValueError:
        print("不是一个正数")

#最简单的方式计算阶乘：math库自带阶乘函数math.factorial
import math
num = int(input("请输入一个数字："))
if num < 0:
    print("负数是没有阶乘的！")
else:
    print("{0} 的阶乘为 {1}".format(num, math.factorial(num)))