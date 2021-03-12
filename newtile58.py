n = int(input('输入斐波那契数列的目标数字：'))
def fibo2(n):#这个函数计算有n个斐波那契数列
    a,b = 0,1
    arr = []
    while n>0:
        arr.append(a+b)
        a, b =b, a+b
        n-=1
    return arr
print(fibo2(n))

n = int(input('输入斐波那契数列的目标数字：'))
def fibo2(n):#这个函数计算不超过n这个值的斐波那契数列
    a,b = 0,1
    arr = []
    while 1:
        if a+b<=n:
            arr.append(a+b)
            a, b =b, a+b
        else:
            break
    return arr
print(fibo2(n))
