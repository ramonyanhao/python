def fib_loop(n):
  a, b = 0, 1
  for i in range(n + 1):
    a, b = b, a + b#斐波那契数列，先计算等号右边的值，然后再把结果赋值给左边变量。如：a,b=0,1 a,b=b,a+b相当于a,b=1,0+1,结果为a,b=1,1
#然后赋值给左边，a=1,b=1,再计算，a,b=1,1+1,赋值给左边a=1,b=2，再计算,a,b=2,2+1这里注意现在a还是等于1,结果赋值给左边a,b=2,3赋值后a才等于2，b等于3
#再依次计算，a,b=3,2+3赋值a=3,b=5
  return a
for i in range(20):
  print(fib_loop(i), end=' ')
print()

def F(n):
    if n <= 1:
      return 1#这里等于n的值小于等于1时返回1，得到n的值在下面for循环i是0和1时n都等于1
    else:
      return F(n - 1) + F(n - 2)#注意这里F(n-1)代表F函数的n-1的值加上F函数n-2的值，通俗讲就是把当前n的值往前退一步加当前n的值往前退两步
#举例:可以写成F(n-1)+F(n-2))这样就代表需要往前推2个n值相加得出下一个n值，可以理解这里n的值不是实际函数的值，是当前执行的步数往前推几步
#例如F(5)，n的值为5，那这里带入这个函数，F(5-1)+F(5-2)就是从当前往前推1步+往前推2步，当n<=1时函数都return 1,所以前两步的值都是1
#第三步开始计算第一步的值1+第二步的值1等于2，从0开始那第三步就是i=2时得出的n值是2，第四步就是计算前两步的值相加，第三步的值为2，第二步的值为1
#2+1=3，所以第四步的值为3，第5步计算前两步的值，第四步的值为3，第三步的值为2，3+2=5，第5步的值为5，第六步计算第5步+第四步的值，5+3=8，第六步的值为8，以此类推
#结论就是return F(n-1)+F(n-2)不是计算函数n的值，这个公式计算函数F前一步n的值+前两步n的值，F(n-1)代表前一次递归下来的值+F(n-2)代表前两次递归下来的值
print('this is',F(5))
for i in range(10):
  print(i, "-->", F(i))#这里当i=0或1时，return 1，当i=2时，F(2-1)+F(2-2)得出F(1)+F(0),i=0和1时都返回1，所以第三步就是1+1=2


def fib_loop_while(max):
  a, b = 0, 1
  while max > 0:
    a, b = b, a + b
    max -= 1
    yield a#yield: 好处：1.不会将所有数据取出来存入内存中；而是返回了一个对象；可以通过对象获取数据；用多少取多少，可以节省内容空间。
#2.yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator
# 调用 fib_recur(5) 不会执行fib_recur函数，而是返回一个 iterable(迭代） 对象！
# 在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，执行到 yield a 时，fab 函数就返回一个迭代值
# 下次迭代时，代码从 yield a 的下一条语句继续执行，而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，直到再次遇到 yield。
for i in fib_loop_while(10):
  print(i,end=" ")