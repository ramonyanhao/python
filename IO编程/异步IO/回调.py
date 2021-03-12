import time
import asyncio
import queue
from threading import Thread
# 把协程动态添加到事件循环中
def start_loop(loop):
    # 一个在后台永远运行的事件循环
    asyncio.set_event_loop(loop)
    loop.run_forever()
# loop.run_forever最大作用就是保持loop一直运行，如果遇到从其他线程回调函数到当前循环时使用，例如这里定义了一个新的线程t,并通过start_loop函数使new_loop这个事件循环一直运行
# 这时new_loop使用call_soon_threadsafe函数从另一个线程调用do_sleep函数到new_loop这个事件循环中运行
# loop.run_until_complete()当前循环中如果所有task都运行完成，循环就会退出
# call_soon方法用于在协程中执行一些普通函数，在执行的时候需要使用run_forever方法，而不是使用run_until_complete方法因为该方法不是协程方法
def do_sleep(x, queue, msg=""):
    time.sleep(x)
    queue.put(msg)
'''
q.put(item,block=True,timeout=None)  #将item放入Queue尾部，item必须存在，

      block默认为True，表示当队列满的时候，等待有位置在放入。为Flase，当队列满的时候，继续put会报错。

      timeout设置，等待放入超时则报错,如果想一只等待这就传递timeout=None，当block=True时才设置timeout参数

q.get(block=True,timeout=None) #移除并返回队列头部的一个值，

       block默认为True，表示获取数值的时候，如果队列为空，则阻塞。为False，则不阻塞，如果为空，异常。

       timeout，表示会阻塞设置的时间，如果超时获取不到数据报错,如果想一直等待这就传递timeout=None,当block=True时才设置timeout参数
'''

#  queue模块还提供了两个二次封装了的函数，
#  q.put_nowait(23) 相当于q.put(23, block=False)
#  q.get_nowait() 相当于q.get(block=False)
que = queue.Queue()
new_loop = asyncio.new_event_loop()

# 定义一个线程，并传入一个事件循环对象
t = Thread(target=start_loop, args=(new_loop,))
t.start()
print(time.ctime())

# 动态添加两个协程
# 这种方法，在主线程是同步的
new_loop.call_soon_threadsafe(do_sleep, 6, que, "第一个")  # call_soon_threadsafe 方法则是线程安全的方法比如在在多线程中需要对同一个变量进行操作就可以使用该方法,可以不用线程锁
new_loop.call_soon_threadsafe(do_sleep, 3, que, "第二个")
# task.add_done_callback是在任务运行完成后执行的回调函数，并且可以通过回调函数参数future.result()获取协程执行的结果，loop.call_soon代表下一次事件循环运行的回调函数
'''
def callback(future):
    print(future.result())
'''

while True:
    try:
        msg = que.get(timeout=7)
        print("msg {} 协程运行完..".format(msg))
        print(time.ctime())
    except BaseException as e:  # 如果不用timeout和try以及except检查除timeout错误，while True会一直循环，不会运行下面的代码
        print(e)
        break

# 重点是由于time.sleep是同步阻塞的，总共耗时6+3=9秒.

def start_loop1(loop):
    # 一个在后台永远运行的事件循环
    asyncio.set_event_loop(loop)
    loop.run_forever()

async def do_sleep1(x, queue, msg=""):
    await asyncio.sleep(x)
    queue.put(msg)

queue1 = queue.Queue()

new_loop1 = asyncio.new_event_loop()

# 定义一个线程，并传入一个事件循环对象
t1 = Thread(target=start_loop1, args=(new_loop1,))
t1.start()
print(time.ctime())

# 动态添加两个协程
# 这种方法，在主线程是异步的
asyncio.run_coroutine_threadsafe(do_sleep1(3, queue1, "第一个"), new_loop1)  # run_coroutine_threadsafe将协程提交到给定的事件循环
asyncio.run_coroutine_threadsafe(do_sleep1(6, queue1, "第二个"), new_loop1)

while True:
    try:
        msg1 = queue1.get(timeout=9)
        print("msg1 {} 协程运行完..".format(msg1))
        print(time.ctime())
    except BaseException as e:
        break
# 重点是由于asyncio.sleep(x)异步的，所以总共耗时6秒.
# new_loop.call_soon_threadsafe方法用于把别的线程的回调函数拉到当前事件循环中运行
# asyncio.run_coroutine_threadsafe(coroutine,new_loop)方法把协程提交到执行的事件循环中运行,和call_soon_threadsafe方法相反
