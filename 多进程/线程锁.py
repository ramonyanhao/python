import threading
# 在多线程环境下，每个线程都有自己的数据。一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，不会影响其他线程，而全局变量的修改必须加锁
# 因此多线程有两种方式，第一种是设置全局变量，然后在线程中需要使用这个全局变量的时候加锁，因为所有线程都会共享这一个全局变量,例如：
# 假定这是你的银行存款:
balance = 0 # 所有线程都会使用这个全局变量balance
lock = threading.Lock() # 如果不加锁最后得出的结果可能不是0，因为有t1和t2两个线程同时使用这个balance,而且t1和t2是交替运行的
def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(1000000):
            # 先要获取锁:
            lock.acquire()
            try:
                # 放心地改吧:
                change_it(n)
            finally:
                # 改完了一定要释放锁:
                lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
# 第二种就是给每个线程设置自己的局部变量，例如下面的local_school.student,t1使用的局部变量local_school.student=Alice,t2使用的局部变量local_school.student=Bob
# 创建全局ThreadLocal对象:
local_school = threading.local()
# 其实threading是一个类，local是类中的方法，local_school就是一个类实例对象

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student  # 还记得之前学习过类实例对象可以随意添加属性吗，例如:std=type('student',(),{'name':'yanhao'})
    # 创建了一个类，名字是student,它的属性有name,并给实例化为std,这时我们可以通过std.age=19给类实例添加属性age,这个例子就和这里一样，给类实例local_school添加属性student
    # 当然这个属性名student可以随意取，但注意如果类中有__slots__限制属性名这种方法时，就不可以动态添加类实例化属性了
    print('Hello, %s (in %s)\n' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal实例的student:
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
'''
全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。你可以把local_school看成全局变量

但每个属性如local_school.student都是线程的局部变量，可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。

可以理解为全局变量local_school是一个dict，不但可以用local_school.student，还可以绑定其他变量，如local_school.teacher等等。

ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。

小结
一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
'''