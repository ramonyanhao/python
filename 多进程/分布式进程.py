# 在Thread和Process中，应当优选Process，因为Process更稳定，而且，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上
# Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上
import random
from multiprocessing.managers import BaseManager
from multiprocessing import Queue
# 发送任务的队列:
task_queue = Queue()
# 接收结果的队列:
result_queue = Queue()

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass
def gettask():
    return task_queue
def getresult():
    return result_queue
def dotask():
    # 把两个Queue都注册到网络上, callable参数关联了Queue对象,这里注意Windows下在注册任务队列和结果队列时不支持lambda表达式，需要使用函数gettask和getresult代替
    # QueueManager.register('get_task_queue', callable=lambda: task_queue)
    # QueueManager.register('get_result_queue', callable=lambda: result_queue)
    QueueManager.register('get_task_queue', callable=gettask) # 由于QueueManager管理的不止一个Queue，所以，要给每个Queue的网络调用接口起个名字，比如get_task_queue
    QueueManager.register('get_result_queue', callable=getresult)
    # 绑定端口5000, 设置验证码'abc':
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    # 启动Queue:
    manager.start()
    # 获得通过网络访问的Queue对象:
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 放几个任务进去:
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n) # 把n这个从0到10000的随机数传到task这个传送任务的队列中，客户端通过task队列取出这些数据再进行计算，然后把计算结果传送到result队列中
    # 从result队列读取结果:
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=10) # 从result队列中取出客户端计算过的结果
        print('Result: %s' % r)
    # 关闭:
    manager.shutdown()
    print('master exit.')
if __name__ == '__main__':
    dotask()
# 这就是一个简单但真正的分布式计算，把代码稍加改造，启动多个worker，就可以把任务分布到几台甚至几十台机器上
