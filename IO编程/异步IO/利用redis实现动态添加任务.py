import time
import redis
import asyncio
from queue import Queue
from threading import Thread
# 通过往redis中添加键值，然后在do_sleep协程中消费这些键值
def start_loop(loop):
    # 一个在后台永远运行的事件循环
    asyncio.set_event_loop(loop)
    loop.run_forever()  # 运行事件循环直到loop.stop()被调用

async def do_sleep(x, queue):
    await asyncio.sleep(x)
    queue.put("ok")

def get_redis():
    connection_pool = redis.ConnectionPool(host='192.168.43.128',port=6379, db=0)
    return redis.Redis(connection_pool=connection_pool)

def consumer():
    rcon.lpush('queue', 1)  # 给redis服务器添加键queue,值为1
    rcon.lpush('queue', 3)
    while True:
        task = rcon.rpop("queue")  # 移除键queue的最后一个元素，返回值为移除的元素
        # _, task1 = rcon.brpop('queue')   brpop移出并获取列表的最后一个元素， 如果列表没有元素会阻塞列表直到等待超时或发现可弹出元素为止
        # 返回一个含有两个元素的列表，第一个元素是被弹出元素所属的key赋值给变量_,第二个元素是被弹出元素的值赋值给变量task1，使用brpop会一直阻塞直到有queue由数据传入或者设定timeout直到超时
        if not task:  # 因为brpop会阻塞线程，所以如果使用brpop就不需要这里的判断条件
            time.sleep(1)
            continue
        asyncio.run_coroutine_threadsafe(do_sleep(int(task), queue), new_loop)  # 把do_sleep协程函数提交到new_loop事件循环中,通过run_forever运行do_sleep协程函数


if __name__ == '__main__':
    print(time.ctime())
    new_loop = asyncio.new_event_loop()
    # 定义一个线程，运行一个事件循环对象，用于实时接收新任务
    loop_thread = Thread(target=start_loop, args=(new_loop,))
    loop_thread.setDaemon(True)  # 给子线程设置setDaemon守护模式，当主线程退出时子线程也会退出
    loop_thread.start()
    # 创建redis连接
    rcon = get_redis()
    queue = Queue()

    # 子线程：用于消费队列消息，并实时往事件对象容器中添加新任务
    consumer_thread = Thread(target=consumer)
    consumer_thread.setDaemon(True)
    consumer_thread.start()
    try:
        while True:
            msg = queue.get()
            print("协程运行完..",msg)
            print("当前时间：", time.ctime())
    except KeyboardInterrupt as e:  # 如果按ctrl+c，会抛出KeyboardInterrupt错误
        print(e)
        new_loop.stop()