# 锁同时只允许一个线程更改数据，而threading.BoundedSemaphore是同时允许一定数量的线程更改数据
import threading
import time


def run(n):
    semaphore.acquire()   #加锁
    time.sleep(1)
    print("run the thread:%s\n" % n)
    semaphore.release()     #释放

semaphore = threading.BoundedSemaphore(5)  # 最多允许5个线程同时运行,但这种方式有风险，有可能会出现不是期望的数据，不过概率非常小

for i in range(22):
    t = threading.Thread(target=run, args=("t-%s" % i,))
    t.start()

while threading.active_count() != 1:
    pass  # threading.active_count()返回当前共有多少个活跃的线程数
else:
    print('-----all threads done-----')