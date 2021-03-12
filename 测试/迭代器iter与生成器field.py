'''
迭代器与生成器的异同：

（1）生成器是一个返回迭代器对象的函数, 调用一个生成器函数，返回的是一个迭代器对象。一边循环一边计算的机制，称为生成器，默认yield通过for循环不会输出函数的return返回值
如果想让yield也输出return的返回值，可以这样:try ...,except StopIteration as e: print(e.value),这里的value就是函数的return返回值


（2）可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator；迭代器是访问集合元素的一种方式，
Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。
可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，迭代器只能往前不会后退
所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算，字符串，列表或元组对象都可用于创建迭代器。
'''
def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成,通过下面while循环中的next(f)输出下一个值
print(f)#两种调用yield方法，for和while
for i in f:
    print(i,end='')
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        break
# 生成器，把return替换成yield,程序每次运行到yield index时暂停并调出上一次的值然后继续运行，到下一轮循环在yield时又暂停再调出这一轮的值
# 通过for循环对一个可迭代对象进行迭代时，for循环内部机制会自动通过调用iter()方法执行可迭代对象内部定义的__iter__()方法来获取一个迭代器，
# 然后一次又一次得迭代过程中通过调用next()方法执行迭代器内部定义的__next__()方法获取下一个元素，当没有下一个元素时，for循环自动捕获并处理StopIteration异常
# 在类中使用生成器和迭代器
class Fibs():# 使用迭代器方法__iter__和__next__
    def __init__(self):
        self.a,self.b=0,1
    def __next__(self):# 返回下一个迭代器对象
        self.a,self.b=self.b,self.a+self.b
        return self.a
    def __iter__(self):# 返回一个迭代器对象
        return self
fibs = Fibs()
for i in fibs:
    print(i)
    if i>100:
        break
class ibs(): # 使用生成器yield
    def __init__(self):
        self.a,self.b=0,1
    def yie(self):
        while True:
            self.a,self.b=self.b,self.a+self.b
            yield self.a# 生成器yield等于替代了上面的__iter__迭代器方法和__next__方法，生成器就是一个数据类型，但是这个数据类型可以自动实现迭代器协议

ibs=ibs()
print(type(ibs.yie()))
for i in ibs.yie():
    print(i)
    if i>100:
        break
# 生成器都是可迭代对象Iterable，但list、dict、str虽然是Iterable，却不是迭代器Iterator，把list、dict、str等Iterable变成Iterator可以使用iter()函数
# Python中 list，tuple，str，dict这些都可以被迭代，但他们并不是迭代器。为什么？
# 因为和迭代器相比有一个很大的不同，list/tuple/map/dict这些数据的大小是确定的，也就是说有多少内容都是可知的。
# 但迭代器不是，迭代器不知道要执行多少次，所以可以理解为不知道有多少个元素，每调用一次next()，就会往下走一步，是惰性的。
'''
send()方法：

send()方法和__next__方法实现的功能类似，都是取出生成器中的值，但send()方法需要传递一个参数，可以将该参数传递给yield并赋值给一个变量
def test():
    f = yield 1
    print(f)
    yield 2

t = test()
print(t.__next__())
t.send("yield一个1")
运行结果：

1

yield一个1
'''
