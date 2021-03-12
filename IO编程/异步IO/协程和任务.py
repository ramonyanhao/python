import asyncio
import functools

async def do_some_work(x):
    print('Waiting: ', x)
    return 'Done after {}s'.format(x)

def callback(t, future):
    print('Callback:', t, future.result())  # future.result就是协程do_some_work的return值
coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
task.add_done_callback(functools.partial(callback, 'callback参数t'))  # 绑定回调，如果回调函数有多个参数需要使用functools.partial来把多个参数变为实参再传递给回调函数
loop.run_until_complete(task)
#  协程遇到await，事件循环将会挂起该协程，执行别的协程，直到其他的协程也挂起或者执行完毕，再进行下一个协程的执行，await就是用在耗时的IO操作中，例如网络连接，文件读取
#  asyncio可以运行并发，多任务同时运行，并行需要多进程，在同一时间段运行多个任务，asyncio实现并发，就需要多个协程来完成任务，每当有任务阻塞的时候就await，然后其他协程继续工作
async def main():
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(4)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]
    # 使用as_completed，返回协程的迭代器。可以等待返回的每个协程，以从其余的等待组中获得最早的下一个结果
    for task in asyncio.as_completed(tasks):
        result = await task
        print('as_completed Task ret: {}'.format(result))
    # 使用asyncio.wait
    dones, pendings = await asyncio.wait(tasks)

    for task in dones:
        print('wait Task ret: ', task.result())

    # 使用asyncio.gather
    results = await asyncio.gather(*tasks)

    for result in results:
        print('gather Task ret: ', result)
loop = asyncio.get_event_loop()
done=loop.run_until_complete(main())  # done就是协程main()的执行结果，此时的done结果为None,因为main()没有返回值，如果main中使用return await asyncio.gather(*tasks)，done就是这个返回的结果
#  asyncio.run(main()) 也可以不用loop事件循环机制，直接使用run

