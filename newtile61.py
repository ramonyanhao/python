while True:#使用filter计算最小公倍数
    try:
        n1=int(input('请输入第一个正整数: '))
        n2=int(input('请输入第一个正整数: '))
        L1=list(filter(lambda x:x%n1==0,range(n1,n1*n2+1)))#filter把range列表里的数拿出来再公式lambda中检验，符合lambda条件的放在列表里
        L2=list(filter(lambda x:x%n2==0,range(n2,n1*n2+1)))#x可以整除n1和n2，代表x就是n1和n2的倍数，x的取值范围是n1和n2到n1,n2乘积之间
        L=list(filter(lambda x:x in L2,L1))#这里表示x同时再L2和L1两个列表中
        print('{0}最小公倍数为{1}'.format((n1,n2),min(L)))#min取出L列表的最小数就是n1和n2的最小公倍数
        break
    except ValueError:
        print('请输入正整数')
#最小公倍数就是两个数的共同倍数，这个共同倍数最大就是两个数的乘积，一般计算公式指定范围就是两个数到他们的乘积之间。或者另一种算法用两个数乘积除两个数的最大公约数得出就是两个数最小公倍数
def lcm(x, y): # very fast
    s = x*y
    while y: x, y = y, x%y#这个公式是计算x,y的最大公约数
    return s//x#用x,y的乘积除x,y的最大公约数可以得出x,y的最小公倍数
print(lcm(120, 123)) #result: 4920

import math#可以使用math.gcd计算a,b的最大公约数，然后a*b/最大公约数得出a,b最小公倍数
a = 54
b = 24
print(a*b//math.gcd(a,b))