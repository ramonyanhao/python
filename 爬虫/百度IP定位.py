import json,time
import requests
import asyncio
import threading
from multiprocessing import Process
class Fip:
    def __init__(self, ip=None):
        # 用户上网的IP地址，请求中如果ip为空，会针对发来请求的IP进行定位。
        self._ip = ip
        self._url = 'http://api.map.baidu.com/location/ip'
        self.https_url = 'https://api.map.baidu.com/location/ip'
        self._params = {'ak':'wiw57wInUncbNdFGuZz5sPRc1UEqiTyO'}
        self.address = None

    async def http_ip(self):
        # 如果没有在请求中指定ip,则默认为当前发送过来的IP进行地址定位
        if self._ip:
            params = self._params.copy()
            params.update(ip=self._ip)
            res = requests.get(self._url,params=params)
            data = json.loads(res.text)
            if data['status'] == 0:
                self.address = data['content']['address']
                print(self.address,time.ctime())
                return self.address
            else:
                print('Error Output!')
                return data['status']
        else:
            res = requests.get(self._url, params=self._params)
            data = json.loads(res.text)
            if data['status'] == 0:
                self.address = data['content']['address']
                print(self.address,time.ctime())
                return self.address
            else:
                print('Error Output!')
                return data['status']

    async def https_ip(self):
        '''使用 https 请求数据'''
        if self._ip:
            params = self._params.copy()
            params.update(ip=self._ip)
            res = requests.get(self.https_url,params=params)
            data = json.loads(res.text)
            if data['status'] == 0:
                self.address = data['content']['address']
                print(self.address,time.ctime())
                return self.address
            else:
                print('Error Output!')
                return data['status']
        else:
            res = requests.get(self.https_url, params=self._params)
            data = json.loads(res.text)
            if data['status'] == 0:
                self.address = data['content']['address']
                print(self.address,time.ctime())
                return self.address
            else:
                print('Error Output!')
                return data['status']

if __name__ == '__main__':
    fin_ip=Fip('220.181.171.195')
    non_ip=Fip()  # 如果没有在请求中指定ip,则默认为当前发送过来的IP进行地址定位
    task = [fin_ip.http_ip(),fin_ip.https_ip(),non_ip.http_ip(),non_ip.https_ip()]
    print(task)
    task1 = asyncio.ensure_future(fin_ip.http_ip())  # asyncio.ensure_future创建协程任务
    print(task1)  # task1这个任务没有运行，状态为pending
    loop=asyncio.get_event_loop()
    loop.run_until_complete(task1)  # 循环中运行任务task1,不过通过run_until_complete方法会将协程自动包装成为了一个任务对象,但是去创建一个任务对象task1，有利于我们理解协程的状态:task.result()获取任务结果
    print(task1, task1.result())  # task1任务状态为finished,注意获取任务结果使用任务名称+result()
    group = asyncio.gather(*task)  # 通过asyncio.gather把任务进行分组
    print(group)  # group状态为pending
    loop.run_until_complete(group)
    print(group, group.result())  # 获取任务组的结果
    loop.close()
    async def main():
        t1 = fin_ip.http_ip()
        t2 = fin_ip.https_ip()
        t3 = non_ip.http_ip()
        t4 = non_ip.https_ip()
        tasks = [
            asyncio.ensure_future(t1),
            asyncio.ensure_future(t2),
            asyncio.ensure_future(t3),
            asyncio.ensure_future(t4)
        ]
        for task in asyncio.as_completed(tasks):  # asyncio.as_completed()返回一个可迭代的协程函数值，其实不用asyncio.as_completed()也可以，因为tasks本身也是一个通过ensure_future创建的任务集合
            result = await task  # 返回了任务的结果
            print('task result:',result)
        print('asyncio.wait:',await asyncio.wait(tasks))
        return await asyncio.wait(tasks)  # 使用asyncio.wait返回done和pending的任务列表({<Task finished coro=<Fip.http_ip() done, defined at D:/python/爬虫/百度IP定位.py:15> result='河北省张家口市'>, <Task finished coro=<Fip.https_ip() done, defined at D:/python/爬虫/百度IP定位.py:40> result='河北省张家口市'>, <Task finished coro=<Fip.https_ip() done, defined at D:/python/爬虫/百度IP定位.py:40> result='北京市'>, <Task finished coro=<Fip.http_ip() done, defined at D:/python/爬虫/百度IP定位.py:15> result='北京市'>}, set())
        # return await asyncio.gather(tasks) # 如果使用gather则直接返回结果，例如:result = new_loop.run_until_complete(main())返回:['北京市', '北京市', '河北省张家口市', '河北省张家口市']
    new_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(new_loop)
    # result = new_loop.run_until_complete(main())  # 使用asyncio.gather时只用result接受任务结果，如果使用wait则返回任务列表，使用dones和pendings接收已完成和未完成的任务列表返回结果
    dones,pendings = new_loop.run_until_complete(main())
    print('done:', dones, 'pending:', pendings)
    new_loop.close()