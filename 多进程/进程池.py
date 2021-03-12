'''由于进程启动的开销比较大，使用多进程的时候会导致大量内存空间被消耗。为了防止这种情况发生可以使用进程池
（由于启动线程的开销比较小，所以不需要线程池这种概念，多线程只会频繁得切换cpu导致系统变慢，并不会占用过多的内存空间）
进程池中常用方法：
map(函数，列表)
将列表中的元素依次提取出来作为参数传入Foo函数中，创建一个个进程，放进进程池中
apply()
同步执行（串行）
apply_async()
异步执行（并行）
terminate()
立刻关闭进程池
join()
主进程等待所有子进程执行完毕。必须在close或terminate()
之后。
close()
等待所有进程结束后，才关闭进程池。
'''
from multiprocessing import Pool
import time


def Foo(i):
    time.sleep(2)
    return i + 100


def Bar(arg):
    print('-->exec done:', arg)
# 重点在windows中, 创建进程由于没有fork()创建进程, 所以是通过重载自身模块来创建的, 如果Pool放在if __name__ == "__main__"外部, 就会进行无线递归模块
if __name__ == '__main__':
    p = Pool(5)  # 允许进程池同时放入5个进程

    for i in range(10):

        p.apply_async(func=Foo, args=(i,), callback=Bar)  # func子进程执行完后，才会执行callback，否则callback不执行（而且callback是由父进程来执行了）
        # pool.apply(func=Foo, args=(i,))
    print(p.map(Foo, [1, 2, 3]))  # pool.map将列表中的每个元素提取出来当作Foo函数的参数，创建一个个进程，放进进程池中
    # 第一个参数是函数，第二个参数是一个迭代器，将迭代器中的数字作为参数依次传入Foo函数中,作用：这是多进程的创建，应用在爬虫中主要目的是提高爬取的效率，实现秒爬
    print('end')
    p.close()
    p.join()  # 主进程等待所有子进程执行完毕。必须在close()或terminate()之后。
# 进程池内部维护一个进程序列，当使用时，去进程池中获取一个进程，如果进程池序列中没有可供使用的进程，那么程序就会等待，直到进程池中有可用进程为止。
# 在上面的程序中产生了10个进程，但是只能有5同时被放入进程池，剩下的都被暂时挂起，并不占用内存空间，等前面的五个进程执行完后，再执行剩下5个进程。
