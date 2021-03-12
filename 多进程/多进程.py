from multiprocessing import Process # threading是多线程用的模块，multiprocessing是多进程用的模块
import os
# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',)) # 通过Process创建子进程
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

from multiprocessing import Pool
import os, time, random
# 如果要启动大量的子进程，可以用进程池Pool的方式批量创建子进程
def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4) # 通过Pool创建进程池，进程池中最多有4个子进程，如果执行的进程超过4个需要等待进程池中的进程执行完后再执行
    for i in range(5): # 共有5个进程需要执行
        p.apply_async(long_time_task, args=(i,)) # 把这5个进程写入进程池中
    print('Waiting for all subprocesses done...')
    p.close() # close代表关闭进程池，也就是进程池中只能有4个进程，不能再写入多余的进程
    p.join() # 等待所有子进程执行完毕
    print('All subprocesses done.') # 最终的执行结果是最后一个进程要等待进程池中的4个进程的某一个执行完毕后再执行，如果把Pool(4)改为5就可以把5个进程全部写入进程池了

# 进程间通信
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value) # 其实就相当于multiprocessing.Queue().put()
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True) # 其实就相当于multiprocessing.Queue().get()
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()