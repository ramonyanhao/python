import time
import asyncio
import redis
# 用协程方式代替多线程，程序初始化就创建若干个协程，实现类似多线程的效果
now = lambda : time.time()

def get_redis():
    connection_pool = redis.ConnectionPool(host='192.168.43.128',port=6379, db=3)
    return redis.Redis(connection_pool=connection_pool)

rcon = get_redis()
rcon.lpush('queue','ok')
async def worker():
    print('Start worker')
    rcon.lpush('queue', 1)
    rcon.lpush('queue', 2)
    while True:
        start = now()
        task = rcon.rpop("queue")
        if not task:
            break
        print('Wait ', int(task))
        await asyncio.sleep(int(task))
        print('完成用时%.2f s' % (now() - start))

def main():
    start_time = now()
    task1 = asyncio.ensure_future(worker())  # 多启动几个worker来监听队列。一样可以到达多线程效果
    task2 = asyncio.ensure_future(worker())
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(asyncio.gather(*[task1,task2]))  # 2个任务，每个任务中有2个协程，一个需要1秒一个需要2秒，由于同步执行协程任务，所以每个任务执行时间为2秒，2个任务共用时4秒
        # loop.run_forever() run_forever和run_until_complete区别run_forever会无限循环运行,run_until_complete只要把事件循环中的任务运行完就结束
    except KeyboardInterrupt as e:
        print(asyncio.gather(*asyncio.Task.all_tasks()).cancel())  # 输出所有被取消的任务
        loop.stop()
        loop.run_forever()
    finally:
        loop.close()
        print('总计用时%.2f s' % (now() - start_time))


if __name__ == '__main__':
    main()