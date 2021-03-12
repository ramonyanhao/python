def gcd(x, y): # very fast
   return x if y == 0 else gcd(y, x%y)
print(gcd(11,55))

#如果y的值为0，函数gcd直接返回x的值，否则gcd函数x的值改为y,y的值改为x%y,这样形成循环一直到y的值为0，返回x的值就是x,y的最大公约数
#例如x值为5，y的值为10,y不等于0，运行gcd(10,5%10)得到x的值为10，y的值为5，y还不等于0，继续运行gcd(5,10%5)得到x的值为5，y的值为0，最后得出最大公约数5


def gcd1(a,b):
    if a%b == 0:#这里的条件a%b==0的话，a肯定大于b,而且可以除净那b肯定就是a和b的最大公约数，如果a小于b这里a%b得出的结果就不是0，而是a的值
        return b
    else :#否则b大于a
        return gcd1(b,a%b)#如果b大于a的情况下，返回a=b,b=a%b,得出的结果就是a变成b的值，b变成a(如果a小于b，a%b=a),这个逻辑理论有点像a,b=b,a+b斐波那契数列

#math模块的gcd函数可以直接算出两个数的最大公约数
import math

print(math.gcd(10,20))

def hcf(x, y):
    """该函数返回两个数的最大公约数"""

    # 获取最小值
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i

    return hcf


# 用户输入两个数字
num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))

print(num1, "和", num2, "的最大公约数为", hcf(num1, num2))
