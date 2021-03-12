import time
from multiprocessing.managers import BaseManager
# 注意再客户端中根本没有创建Queue的代码，所以，Queue对象存储在服务器端的进程中
# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass

# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器，也就是运行分布式进程.py的机器:
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
# 端口和验证码注意保持与分布式进程.py设置的完全一致:
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# 从网络连接:
m.connect()
# 获取Queue的对象:
task = m.get_task_queue()
result = m.get_result_queue()
# 从task队列取任务,并把结果写入result队列:
while not task.empty():
    n = task.get(timeout=1) # 从服务器端的task队列中取出所有数据
    print('run task %d * %d...' % (n, n))
    r = '%d * %d = %d' % (n, n, n*n) # 计算从服务器端取出的数据
    time.sleep(1)
    result.put(r) # 再把计算过的结果传送到result队列，服务器端就可以从result队列中取出计算结果
else:
    print('task queue is empty.')
# 处理结束:
print('worker exit.')
# 注意Queue的作用是用来传递任务和接收结果，每个任务的描述数据量要尽量小。
# 比如发送一个处理日志文件的任务，就不要发送几百兆的日志文件本身，而是发送日志文件存放的完整路径，由Worker进程再去共享的磁盘上读取文件
