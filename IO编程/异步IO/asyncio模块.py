import asyncio
import time
# 用asyncio提供的@asyncio.coroutine可以把一个generator标记为coroutine类型，然后在coroutine内部用yield from调用另一个coroutine实现异步操作。
async def wget(host):  # 使用async代替了@asyncio.coroutine装饰器
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)  # connect就是一个coroutine(协程),然后把这个协程放到await中实现异步操作
    reader, writer = await connect  # 使用await代替了yield from,注意await后面必须是通过async转变的协程函数或者asyncio包中的协程函数
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host  # header 是发送给服务器的消息，意为获取页面的 header 信息
    writer.write(header.encode('utf-8'))
    await writer.drain()
    # 这是一个与底层 IO 输入缓冲区交互的流量控制方法
    # 当缓冲区达到上限时，drain() 阻塞，待到缓冲区回落到下限时，写操作恢复
    # 当不需要等待时，drain() 会立即返回，例如上面的消息内容较少，不会阻塞
    # 这就是一个控制消息的数据量的控制阀
    # 给服务器发送消息后，就等着读取服务器返回来的消息
    while True:
        line = await reader.readline()
        # line就是服务器返回结果每一行的数据
        if line == b'\r\n':
            # 数据接收完毕，会返回空字符串 \r\n ，退出 while 循环，结束数据接收
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))  # 接收的数据是二进制数据，转换为 UTF-8 格式并打印，rstrip 方法删掉字符串的结尾处的空白字符，也就是 \n
    # Ignore the body, close the socket
    writer.close()

new_loop=asyncio.new_event_loop()  # 创建一个新的事件循环对象。
asyncio.set_event_loop(new_loop)   # 将new_loop设置为当前OS线程的当前事件循环
loop = asyncio.get_event_loop()    # 获取当前事件循环。其实loop就是new_loop
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
tasks1 = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks,return_when = 'ALL_COMPLETED'))  # wait和gather都是在协程需要并发的时候使用，wait会阻塞直到参数return_when达到指定的条件为止
# return_when有三个参数，FIRST_COMPLETED代表第一个完成的任务将写进done集合中，后面没完成的写入pending集合.FIRST_EXCEPTION如果引发异常结束时，返回done和pending,没有异常和ALL_COMPLETED参数一样都把已经完成的任务写进done集合，pending集合为空
group1 = asyncio.gather(*tasks)  # gather除了多任务外，还可以对任务进行分组。优先使用gather
group2 = asyncio.gather(*tasks1)
group2.cancel()  # 如果取消某一个gather分组,需要设置gather参数return_exceptions为True，否则会报错
loop.run_until_complete(asyncio.gather(group1,group2,return_exceptions = True))  # 只运行group1，不运行group2
loop.close()
async def main():
    task=asyncio.ensure_future(wget('www.sina.com.cn'))  # 不用事件循环机制loop，可以直接创建协程并使用asyncio.run运行
    task1=asyncio.ensure_future(wget('www.sohu.com'))  # ensure_future 除了接受 coroutine 作为参数，还接受future作为参数
    task2 = asyncio.create_task(wget('www.163.com'))   # create_task和ensure_future都可以创建task,但是create_task只接受coroutine作为参数
    await task,task1,task2
asyncio.run(main())


#  asyncio.Task.all_tasks 方法可以获得事件循环中的任务集合
#  asyncio.as_completed 方法即时获取任务结果

async def wget(host):
    print('wget {}'.format(host))
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: {}\r\n\r\n'.format(host)
    writer.write(header.encode())
    await writer.drain()
    async for line in reader:
        print('{} header > {}'.format(host,
            line.decode('unicode_escape').rstrip()))
    return 'Host: {}'.format(host)

def main():
    '''
    host_list = ['www.shiyanlou.com', 'www.zhihu.com', 't.tt']  # 主机列表
    loop = asyncio.get_event_loop()                             # 事件循环
    coroutines = [wget(host) for host in host_list]             # 协程列表
    tasks = asyncio.wait(coroutines)                            # 任务收集器
    # 之前的文档中讲到过 asyncio.Task.all_tasks 方法可以获得事件循环中的任务集合
    # 事件循环的 run_until_complete 方法的返回值是二元元组
    # 元组的第一个元素也是任务集合
    # 任务本身是一个协程函数，函数的 return 值可以通过任务的 result 方法获得
    result = loop.run_until_complete(tasks)
    print(result)
    for task in result[0]:
        print(task.result())
    '''
    # 任务在结束时才会产生 result 值
    # 上面的写法只能等事件循环停止后一并获取全部任务的 result 值
    # 如果要随时获得任务的 result 值，可以使用 asyncio.as_completed 方法
    # 这样的话需要创建一个主任务并加入到事件循环，事件循环首先运行主任务
    # 在主任务中使用 asyncio.ensure_future 方法创建新的子任务
    # 这些子任务会自动加入到事件循环
    # 随后在主任务中使用 asyncio.as_completed 方法获取已经完成的任务
    async def main_task():
        tasks = []
        host_list = ['www.shiyanlou.com', 'www.zhihu.com', 't.tt']
        for host in host_list:
            tasks.append(asyncio.ensure_future(wget(host)))
        # 这里为什么不使用 asyncio.Task.all_tasks 方法获取任务集合呢？
        # 像这样：asyncio.as_completed(asyncio.Task.all_tasks())
        # 因为任务集合中包含主任务和子任务，虽然二者在事件循环中是并列关系
        # 但是 for 循环会阻塞在这里，主任务永远完不成
        for task in asyncio.as_completed(tasks):
            print(await task)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main_task())
    loop.close()

if __name__ == '__main__':
    main()
