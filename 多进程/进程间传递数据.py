# 由于进程之间数据是不共享的，所以不会出现多线程GIL带来的问题。多进程之间的通信通过Queue()或Pipe()来实现
# 在windows中创建进程由于没有fork()创建进程, 所以是通过重载自身模块来创建的, 如果多进程Process()或者Manager()放在if __name__ == "__main__"外部, 就会进行无限递归循环
# 所以重点是在windows中所有的多进程程序执行时都必须放在if __name__ == "__main__"里，如果是linux则不用
from multiprocessing import Process, Queue
def f(q):
    q.put([42, None, 'hello'])
if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())  # print "[42, None, 'hello']"
    p.join()

'''Pipe的本质是进程之间的数据传递，而不是数据共享，这和socket有点像。pipe()返回两个连接对象分别表示管道的两端，每端都有send()和recv()
方法。如果两个进程试图在同一时间的同一端进行读取和写入那么，这可能会损坏管道中的数据。
'''
from multiprocessing import Pipe

def fun(conn):
    conn.send([42, None, 'hello'])
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=fun, args=(child_conn,))
    p.start()
    print(parent_conn.recv())  # print "[42, None, 'hello']"
    p.join()

from multiprocessing import Manager
# Manager()返回的manager对象会通过一个服务进程，来使其他进程通过代理的方式操作python对象

def fund(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.append(1) # 使其他进程通过manager对象往列表l中添加1
    # 如果没有manager对象，返回的列表l结果一共10个列表，每个列表都是[0, 1, 2, 3, 4, 1],重点是因为进程之间的数据是拷贝的并且进程间不能通信，所以每个进程的结果都是一样的
    print(d,l)

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(5))
        p_list = []
        for i in range(10):
            p = Process(target=fund, args=(d, l))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()
        print(d)
        print(l)