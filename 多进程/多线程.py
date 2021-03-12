import threading # threading是多线程用的模块，multiprocessing是多进程用的模块
import time
# 多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响
# 而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了,所以需要锁threading.Lock()
class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开启线程： " + self.name)
        threadLock.acquire()  # 获取锁，用于线程同步,同时开启两个线程thread1和thread2,thread1获取锁优先运行，运行完毕后释放锁，然后再运行thread2
        print_time(self.name, self.counter, 3)  # 已经获取锁了可以随便修改全局变量，如果没有锁多线程可能会同时修改全局变量会引起混乱
        # 在多线程环境下，每个线程都有自己的数据。一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，不会影响其他线程，而多线程修改全局变量必须加锁
        threadLock.release()  # 释放锁，开启下一个线程

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

threadLock = threading.Lock()
threads = []

# 创建新线程，任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程
thread1 = myThread(1, 'myThread1', 1)  # 线程ID是1，当前线程名字，系统休眠1秒后输出
thread2 = myThread(2, 'myThread2', 2)  # 线程ID是2，当前线程名字，系统休眠2秒后输出
if __name__ == "__main__":
    # setDaemon()方法与join方法相反，setDaemon()方法把主线程变为守护线程，如果主线程运行结束，主线程中的子线程一起结束，setDaemon()方法放在start前面
    # 开启新线程
    # thread1.setDaemon(True)
    thread1.start()
    thread2.start()

    # 添加线程到线程列表
    threads.append(thread1)
    threads.append(thread2)

    # 等待所有线程完成
    for t in threads:
        t.join()  # join用来阻塞主线程，主线程等待子线程运行完，主线程继续运行剩下的代码直至主线程结束
    print ("退出主线程")