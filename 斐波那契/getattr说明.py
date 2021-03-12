class ObjectDict(dict):
    def __init__(self, *args, **kwargs):
        super(ObjectDict, self).__init__(*args, **kwargs)

    def __getattr__(self, name):
        value = self[name] # self输出为asf={'a': 1}, d=True,self本身就是一个字典，在这个字典中还嵌套了一个字典asf，所以self[name]就是asf和d的值{'a':1}和True
        print('使用getattr',name) # 字典中的key和value都是没有直接定义的，asf,a,d都隐藏在字典中，使用getattr就可以获取没有定义过的属性
        if isinstance(value, dict): # 因为value就是{'a':1}和True两个值，这里就是检查value是否为字典，{‘a':1}为字典类型
            value = ObjectDict(value) # 如果value是字典，通过类递归把value{'a':1}这个字典再传入进类中，value=self[name]经过运算得出value=1,最后返回value的值：1
        return value
# 重点是__getattr__用来动态获取init中没有赋予的属性,在外部调用init中的属性需要在init中指定该属性的值，而在getattr中不用，只需要指定传入的参数和返回值就可以动态解析外部传进来的参数
if __name__ == '__main__':
    od = ObjectDict(asf={'a': 1}, d=True)
    print (od.asf)
    print (od.asf.a)
    print (od.d)
print()
class adaptee(object):
    def foo(self):
        print ('foo in adaptee')
    def bar(self):
        print ('bar in adaptee')
class adapter(object):
    def __init__(self):
        self.adaptee = adaptee() # 指定变量self.adaptee的值为adaptee类

    def foo(self):
        print ('foo in adapter')
        self.adaptee.foo()

    def __getattr__(self, name):
        print ('name',name)  # 下面调用了a.bar(),所以name=bar
        c=getattr(self.adaptee, name) # 可以通过getattr获取对象属性后赋值给变量C
        c() # 通过运行变量c直接调用adaptee().bar()
        return getattr(self.adaptee, name) # 通过self.adaptee找到adaptee类，并传入参数name=bar(),返回adaptee类中的bar函数,getattr(self.adaptee,name)相当于返回adaptee().bar

if __name__ == '__main__':
    a = adapter()
    a.foo()
    a.bar() # 在adapter中没有定义bar方法，也没有继承adaptee类，但是这里就可以找到bar方法，原因就是使用getattr传入进bar()参数，然后通过getattr找到adaptee类中的方法并输出