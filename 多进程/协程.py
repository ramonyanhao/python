'''
线程和进程的操作是由程序触发系统接口，最后的执行者是系统，它本质上是操作系统提供的功能。而协程的操作则是程序员指定的，在python中通过yield，人为的实现并发处理。

协程存在的意义：对于多线程应用，CPU通过切片的方式来切换线程间的执行，线程切换时需要耗时。协程，则只使用一个线程，分解一个线程成为多个“微线程”，在一个线程中规定某个代码块的执行顺序。

协程的适用场景：当程序中存在大量不需要CPU的操作时（IO）。
常用第三方模块gevent和greenlet。（本质上，gevent是对greenlet的高级封装，因此一般用它就行，这是一个相当高效的模块。）
'''
from greenlet import greenlet


def test1():
    print(12) # 先输出12
    gr2.switch()  # 切换到test2中输出56
    print(34) # 再通过test2中的gr1.switch()切换会test1输出34
    gr2.switch() # 再切换到test2中输出78

def test2():
    print(56) # 输出完12切换到这里输出56
    gr1.switch() # 切换到test1中输出34
    print(78) # 再通过test1中的gr2.switch()切换到这里输出78

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch() # greenlet就是通过switch方法在不同的任务之间进行切换。
from gevent import monkey; monkey.patch_all()
import gevent
import requests

def f(url):
    print('GET: %s' % url)
    resp = requests.get(url)
    data = resp.text
    print('%d bytes received from %s.' % (len(data), url))

gevent.joinall([
        gevent.spawn(f, 'https://www.python.org/'),
        gevent.spawn(f, 'https://www.yahoo.com/'),
        gevent.spawn(f, 'https://github.com/'),
])
# 通过joinall将任务f和它的参数进行统一调度，实现单线程中的协程。代码封装层次很高，实际使用只需要了解它的几个主要方法即可
