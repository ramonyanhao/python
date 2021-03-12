'''
一个楼梯有20个台阶，按规定上楼梯只能跨上1个或2个台阶
从地面到最上面，有多少种不同的方法？
'''
def f(n):
    if n == 1 or n == 0:
        return 1
    return f(n-1)+f(n-2)
print(f(20))
def fab(n):
    a,b=0,1
    while n>0:
        a,b=b,a+b
        n-=1
    return b
print(fab(20))
def outer(a):
    n,m=0,1
    def inner():
        nonlocal a,n,m
        while a>0:
            n,m=m,n+m
            a-=1
        return m
    return inner
ou=outer(20)
print(ou())


