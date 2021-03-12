#在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)#参数n乘上一次函数fact运算n的值
print(fact(5))
'''
如果我们计算fact(5)，可以根据函数定义看到计算过程如下：

===> fact(5)
===> 5 * fact(4)
===> 5 * (4 * fact(3))
===> 5 * (4 * (3 * fact(2)))
===> 5 * (4 * (3 * (2 * fact(1))))
===> 5 * (4 * (3 * (2 * 1)))
===> 5 * (4 * (3 * 2))
===> 5 * (4 * 6)
===> 5 * 24
===> 120
'''
#尾递归优化:尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况
#上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式,所以就不是尾递归了
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)#仅返回递归函数本身，num - 1和num * product在函数调用前就会被计算，不影响函数调用。
print(fact_iter(5,1))
'''
===> fact_iter(5, 1)
===> fact_iter(4, 5)这里代表num=num-1,product=num*product.当num=5,product=1时，num=5-1,product=1*5,得出fact_iter(4,5),然后继续向下运算
===> fact_iter(3, 20)
===> fact_iter(2, 60)
===> fact_iter(1, 120)
===> 120
'''