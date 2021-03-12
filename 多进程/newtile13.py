import threading  # 多线程模块
from time import ctime,sleep


def music(func):
    for i in range(2):
        print ("I was listening to %s. %s" %(func,ctime()))
        sleep(1)

def move(func):
    for i in range(2):
        print ("I was at the %s! %s" %(func,ctime()))
        sleep(5)

threads = []
t1 = threading.Thread(target=music,args=(u'爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target=move,args=(u'阿凡达',))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)#setDaemon(False)，主线程执行完自己的任务以后，就退出了，此时子线程会继续执行自己的任务，直到自己的任务结束
        #setDaemon(True)方法，设置子线程为守护线程时，主线程一旦执行结束，则全部线程全部被终止执行，可能出现的情况就是，子线程的任务还没有完全执行结束，就被迫停止
        t.start()#进程开始
        t.join()#threading函数里的join(),用作多线程控制，阻塞主线程，等子线程运行完主线程再运行
    print ("all over %s" %ctime())  # 主线程
