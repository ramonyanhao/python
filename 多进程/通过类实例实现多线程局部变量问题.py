# 还有第三种方式通过类实例实现多线程使用局部变量，因为每个类实例都可以拥有自己的属性空间，而多线程也需要使用自己线程内部的局部变量，所以这两个性质是一样的
# 例如把ThreadLock.py的第一个事例银行存款的例子从函数改为通过类实例实现多线程局部变量
import threading
class deposit():
    def __init__(self):
        self.balance = 0

    def change_it(self,n):
        # 先存后取，结果应该为0:

        self.balance = self.balance + n
        self.balance = self.balance - n

    def run(self,n):
        for i in range(1000000):
            # 先要获取锁:
            lock.acquire()
            try:
                # 放心地改吧:
                self.change_it(n)
            finally:
                # 改完了一定要释放锁:
                lock.release()
        print(self.balance)
lock=threading.Lock()
t1=threading.Thread(target=deposit().run(5)) # 通过类实例实现两个线程t1和t2都使用自己的局部变量5和8
t2=threading.Thread(target=deposit().run,args=(8,)) # 这里的args其实就是run方法的参数，和5的意思是一样的
t1.start()
t2.start()
t1.join()
t2.join()
print()
# 另一种方法直接通过继承threading.Thread类，修改run方法实现多线程局部变量
class deposit(threading.Thread):
    def __init__(self,n):
        self.balance = 0
        self.n=n
        super().__init__() # 或者使用threading.Thread.__init__(self)
    def run(self):  #  线程被cpu通过start()调度后自动执行线程对象的run方法，如果想自定义线程类，直接重写run方法就行了
        for i in range(1000000):
            # 先要获取锁:
            lock.acquire()
            try:
                # 放心地改吧:
                self.balance = self.balance + self.n
                self.balance = self.balance - self.n

            finally:
                # 改完了一定要释放锁:
                lock.release()
        print(self.balance)
lock=threading.Lock()
t1=deposit(5) # 通过类实例实现两个线程t1和t2都使用自己的局部变量5和8
t2=deposit(8) # 还有一个不同的地方就是不用给类deposit创建类实例，直接运行start()系统自动调用run方法
t1.start()
t2.start()
t1.join()
t2.join()
# 把ThreadLock.py的第二个示例也改为这种方式,简单很多
class process_thread:
    def __init__(self,name):
        self.name=name
        print('Hello, %s (in %s)\n' % (self.name, threading.current_thread().name))
t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()