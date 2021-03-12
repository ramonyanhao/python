'''
@log的函数装饰器，使它既支持：

@log
def f():
    pass
又支持：

@log('vokied')
def f():
    pass
'''
def log(*ags):
    print(ags)
    def createFn(fn, *p):
        print(fn,*p) # *p就是@log传入的参数vokied，fn是add函数
        def wrapper(*args, **kw):
            print(args) # 这里的args就是add函数的参数3和5
            if len(p) > 0: # 如果log有传入参数
                print('log传入的参数：%s,函数：%s' %(p[0],fn.__name__))

            else: # 如果log没有传入参数

                print('log没有传入参数，函数名:%s' %fn.__name__)

            res = fn(*args, **kw) # res就是函数add运算过后的值，因为add有多个参数所以这里用*args

            return res

        return wrapper
    # ags[0]如果log有参数传入进来，ags[0]就是传进来的参数vokied，如果没有传入参数ags[0]就是函数add本身，这里的ags就是log参数*ags
    if hasattr(ags[0], '__call__'): # 这句话意思就是判断ags[0]是否为log传进来的参数，如果log传参进来，这里ags[0]就变成参数vokied,这个条件为Flase
        print(ags[0].__call__) # 如果log没有传参进来ags[0]就是函数add，通过hasattr判断ags[0]中包含了__call__属性，这个条件为True,简单说就是如果log传参这里就不运行，如果不传参就运行
        print()
        return createFn(ags[0]) # 如果log不传参，通过这里判断完返回函数createFn并且把add函数当成参数,运行wrapper判断p的数量得出有没有传参,重点是注意这个if条件是放在log下的，和createFn函数同级
    else: # 如果log传参进来，这里创建一个函数decorator,然后通过装饰器@log把函数add传进来当成参数fn,其实这里不写也可以正常运行
        def decorator(fn):

            return createFn(fn, *ags) # 这里返回的*ags就是log传进来的参数vokied,然后传递给createFn函数的*p，wrapper再通过判断p的数量得出有没有传参

        return decorator

@log('vokied')
def add(a, b):

    return a + b

print(add(3, 5))