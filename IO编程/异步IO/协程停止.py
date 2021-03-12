import asyncio

import time

now = lambda: time.time()

async def do_some_work(x):
    print('Waiting: ', x)

    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)

async def main():
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(2)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]
    done, pending = await asyncio.wait(tasks)
    for task in done:
        print('done Task ret: ', task.result())

start = now()

loop = asyncio.get_event_loop()
task = asyncio.ensure_future(main())  # ensure_future使用asyncio,ensure_future 除了接受 coroutine 作为参数，还接受 future 作为参数，推荐使用
task1 = loop.create_task(main())  # create_task使用loop事件循环，也可以在协程函数中使用await asyncio.create_task,否则会报错coroutine 'main' was never awaited
try:
    loop.run_until_complete(task)  # 运行循环，直到所有任务完成

except KeyboardInterrupt as e:  # 在循环事件运行时按ctrl+c取消会报KeyboardInterrupt错误
    print(asyncio.Task.all_tasks())  # 返回事件循环的所有任务的集合
    print(asyncio.gather(*asyncio.Task.all_tasks()).cancel())  # 输出事件循环中被取消的任务
    loop.stop()  # 停止循环
    loop.run_forever()  # loop stop之后还需要再次开启事件循环，最后在close，不然会抛出异常，run_forever运行事件循环直到stop()被调用。
finally:
    loop.close()  # 关闭循环
print('%.2f s' %(now()-start))