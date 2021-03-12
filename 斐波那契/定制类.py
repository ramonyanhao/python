class Chain(object):
 # 现在很多网站都搞REST API，调用API的URL,如果增加一个API，添加一个类方法或者属性，那得累死，所以这里采用getattr动态调用类，不管怎么更改网站的网址，代码都不需要改任何东西
 # http://api.server/user/friends
 # http://api.server/user/timeline/list
    def __init__(self, path=''):
        self._path = path
        print(self._path)
    def __getattr__(self, path): # path参数相当于在类外面调用Chain中没有定义过的属性，例如:status,user,timeline,list
        return Chain('%s/%s' % (self._path, path)) # 相当于类递归，返回类再运行init中的self._path参数,只要外部调用一次Chain未定义的属性，这里就会重新运行一次类，然后和getattr中的path参数合并

    def __str__(self): # str作用是只要通过print打印类，都会自动执行str的返回值,例如:print(Chain().status.user.timeline.list)则返回self._path的值/status/user/timeline/list
        return self._path
# 需要注意的时__str__和__repr__的返回值格式必须是字符串形式，但是也可以使用'%s'这种形式传入函数值或者其他类型数据
    __repr__ = __str__ # repr作用时通过执行类的实例，自动指定repr返回值,例如直接运行Chain().status.user.timeline.list，不需要用print，返回值也是/status/user/timeline/list
print(Chain().status.user.timeline.list)
# 如果想要在API中插入参数，可以通过call来完成
class Chain(object):
    def __init__(self, path=''):
        self._path = path
        print(self._path)
    def __getattr__(self, path):
        print('使用getattr')
        return Chain('%s/%s' % (self._path, path))

    def __call__(self, path): # __call__就是把类的实例对象改为可调用对象，像函数那样，这里把users的参数michael传入进来并且再做Chain类递归加入到self._path变量中
        print('使用call')
        return Chain('%s.%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().users('michael').ind('harmon').repos)
# 通过Fib函数把斐波那契修改为可以像列表切片那样操作
class Fib(object):
    def __getitem__(self, n):

        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            step = n.step
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L[start:stop:step]
f=Fib()
print(f[:10:5])