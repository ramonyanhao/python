'''
一个函数内部，嵌套了函数，这个内部函数对（非全局作用域）外部作用域的变量进行引用，那么这个内部函数称为闭包。闭包每次运行是能记住引用的外部作用域的变量的值。
而普通函数运行完一次后，内部的变量就会被丢弃，闭包的变量则会保存在内存中，例如：
def a():
    p=0
    p+=1
    return p
运行a()输出p的变量值1,再次运行a()还是输出1，原因就是函数a()返回p的值：1，但是这个值只能暂存给对象a()，运行完一次就丢弃了，如果改为这样:
def a():
    p=0
    def b():
        nonlocal p
        p+=1
        return p
    return b
运行a=a(),第一次运行a()输出1，第二次a()输出2，第三次a()输出3,原因就是每次运行a(),变量p当前的值保存在闭包a()的__closure__属性中,再次调用a()不会创建新的实例，而是检查__closure__属性,将现有的实例返给它,然后根据现有的实例再进行计算得出第二次运行a()的值为2
闭包作为对象被返回时，它的引用变量就已经确定（已经保存在它的__closure__属性中），不会再被修改。闭包函数将函数的唯一实例保存在它内部的__closure__属性中，
在再次创建函数实例时，闭包检查该函数实例已存在自己的属性中，不会再让他创建新的实例，而是将现有的实例返给它。
闭包在被返回时，它的所有变量就已经固定，形成了一个封闭的对象，这个对象包含了其引用的所有外部、内部变量和表达式。当然，闭包的参数例外，闭包的参数由调用这个闭包时提供多少当前执行就是多少
'''
# 常用的__code__的用法
# func.__code__.co_cellvars：用于闭包中，返回外部函数中被内嵌函数调用的参数，这里注意，一定是被调用的。
# func.__code__.co_argcount：返回函数的参数个数
# func.__code__.co_freevars:用于闭包中，返回内部函数中引用外部函数参数。
# func.__code__.co_varnames:将函数所有局部变量以元组的形式返回。
#查看“闭包”--__closure__属性返回的是一个元组对象，包含了闭包引用的外部变量。
def line_conf():
    a = 1
    b = 2
    def line(x):
        print(a * x + b)
        return a*x+b
    return line
print(line_conf().__code__.co_cellvars)
print(line_conf().__code__.co_freevars)# 输出a,b,内部函数引用的外部函数参数
print(line_conf().__code__.co_argcount)# 1个参数x
print(line_conf().__code__.co_varnames)# 输出局部变量的名字x
L = line_conf()
#闭包作为对象被返回时，它的引用变量就已经确定（已经保存在它的__closure__属性中），不会再被修改,如果函数外部定义b=20,执行line_conf函数时b还是2
print(L.__closure__)
for i in L.__closure__:
    print(i.cell_contents)#结果为1,2，就是变量a和b的值
#若主函数内的闭包不引用外部变量，就不存在闭包，主函数的_closure__属性永远为None;若主函数没有return子函数，就不存在闭包，主函数不存在_closure__属性
#循环体内定义的函数是无法保存循环执行过程中的不停变化的外部变量的，即普通函数无法保存运行环境,例如：
fs=[]
for i in range(3):
    def fun(a):
        return i+a
    fs.append(fun)
fs1, fs2, fs3 = fs
print(fs1,fs2,fs3)
for f in fs:#通过for循环产生了3个fun函数，三个函数都赋值给变量f,下面输出f(1)计算三个函数的值，也可以直接使用fs1, fs2, fs3 = fs
    print(f(1))#输出[3,3,3],如果想要输出[1,2,3],使用闭包，例如下面：
_list = []
for i in range(3):
    def func(i):
        def f_closure(a):
            return i + a # 0+1,1+1,2+1

        return f_closure


    _list.append(func(i))  # 1,2,3

for f in _list:
    print(f(1))#1,2,3
#利用闭包改变输出环境
def my_func():
     fs=[]
     def my():
         for i in range(3):
             fs.append(i*i)
         return fs
     return my#这里很重要，如果使用my()返回的结果是计算过的函数，也就是返回[0,1,4]，如果使用my,调用这个函数的时候再计算，返回的就是[0,1,4,0,1,4]，调用一次返回结果叠加一次
m=my_func()
print(m())
print(m())
#闭包函数的实例
# outer是外部函数 a和b都是外函数的临时变量
def outer( a ):
    b = 10
    # inner是内函数
    def inner():
        nonlocal a,b#这里注意要修改b的值,如果变量b是局部变量，定义在outer函数内，可以用nonlocal,如果定义在全局变量，就是定义在outer函数外，使用global b
        #这里闭包变量a可以通过下面demo=outer(5)实参传递进来的，如果不修改变量b的值，就不需要nonlocal和global,在函数中直接使用
        #在内函数中 用到了外函数的临时变量b,如果没有b+=1，就是不改b的值，就不需要执行nonlocal b，可以直接print(b,a+b)输出结果
        a+=b
        return a
    # 重点：不管主函数outer下面嵌套了多少个函数，这些函数都在其作用域内，都可以在outer作用域内被调用,例如：
    o=inner()
    def ner():
        nonlocal o
        o+=1
        return o
    return ner # 如果把这里改为return inner,后面输出的结果就是a=a+b的值，运行一次加一次
if __name__ == '__main__':
    # 在这里我们调用外函数传入参数5
    # 此时外函数两个临时变量 a是5 b是10 ，并创建了内函数，然后把内函数的引用返回存给了demo
    # 外函数结束的时候发现内部函数将会用到自己的临时变量，这两个临时变量就不会释放，会绑定给这个内部函数
    demo = outer(5)
    # 我们调用内部函数，看一看内部函数是不是能使用外部函数的临时变量
    # demo存了外函数的返回值，也就是inner函数的引用，这里相当于执行inner函数
    print(demo(),demo()) # 5+10+1=16
    demo2 = outer(7)
    print(demo2(),demo2(),demo2())# 7+10+1=18