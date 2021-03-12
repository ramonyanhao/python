class A():
    def __init__(self):
        print('enter A')
        print('leave A')


class B(A):
    def __init__(self):
        print('enter B')
        A.__init__(self)
        print('leave B')


class C(A):
    def __init__(self):
        print('enter C')
        A.__init__(self)
        print('leave C')


class D(B, C):
    def __init__(self):
        print('enter D')
        B.__init__(self)
        C.__init__(self)
        print('leave D')
d = D()
print()
#避免构造函数被调用两次，使用super()函数代替
#super()是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。
#super()会查找所有的超类，以及超类的超类，直到找到所需的特性为止,而使用父类名只会查找上一级的超类
class A():
    def __init__(self):
        print('enter A')
        print('leave A')


class B(A):
    def __init__(self):
        print('enter B')
        super().__init__()
        print('leave B')


class C():
    def __init__(self):
        print('enter C')
        super().__init__()
        print('leave C')


class D(C,B):#如果在子类C中没有继承父类A，那这里就不会输出C类的值，只会输出B,A,D
    def __init__(self):
        print('enter D')
        super().__init__()#这里的super()查找B和C两个方法
        print('leave D')


d = D()
