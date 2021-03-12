# 使得线程等待，只有满足某条件时，才释放n个线程
# wait()线程进入等待状态，等待被其他线程用notify唤醒,如果没有获得锁就执行wait,将引发 RuntimeError 异常
# 通过notify(n)唤醒n个处于等待本条件变量的线程，如果调用本方法的线程并没有获得锁，将引发 RuntimeError 异常
# notify_all()唤醒正在等待本条件变量的所有线程。
# 条件变量对象允许多条线程保持等待状态直到接收另一条线程的通知，这样就可以用于主线程控制其他线程的执行
import threading
import time

def fun(cndition):
    time.sleep(1) # 休眠一秒，确保先运行t2

    # 获得锁
    cndition.acquire()
    print('thread1 acquires lock.')
    # 唤醒t2
    cndition.notify()
    # 进入等待状态，等待其他线程唤醒
    cndition.wait()
    print('thread1 acquires lock again.')
    # 释放锁
    cndition.release()


def fun2(cndition):
    # t2先获得锁
    cndition.acquire()
    print('thread2 acquires lock.')
    # 进入等待状态，等待其他线程唤醒
    cndition.wait()
    print('thread2 acquires lock again.')
    # 唤醒t1
    cndition.notify()
    # 释放锁
    cndition.release()


if __name__ == '__main__':
    cndition = threading.Condition()
    t1 = threading.Thread(target=fun, args=(cndition,))
    t2 = threading.Thread(target=fun2, args=(cndition,))
    t1.start()
    t2.start()
