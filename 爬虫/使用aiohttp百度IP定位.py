import json,time
import aiohttp
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
        params = self._params.copy()
        async with aiohttp.ClientSession() as session:
            async with session.get(self._url, params=params) as resp:
                if self._ip:
                    params.update(ip=self._ip)
                    async with session.get(self._url, params=params) as resp1:
                        print(resp1.url)
                        if resp1.status == 200:
                            self.address = (await resp1.json())['content']['address']  # resp.text()为str格式，使用resp.json()转为字典格式，可以通过['content']['address']获取值
                            print(self.address, time.ctime())
                            return self.address
                        else:
                            print('Error Output!')
                            return resp1.status
                else:
                    if resp.status == 200:
                        print(resp.url)
                        self.address = (await resp.json())['content']['address']
                        print(self.address, time.ctime())
                        return self.address
                    else:
                        print('Error Output!')
                        return resp.status

    async def https_ip(self):
        '''使用 https 请求数据'''
        params = self._params.copy()
        async with aiohttp.ClientSession() as session:
            async with session.get(self._url, params=params) as resp:
                if self._ip:
                    params.update(ip=self._ip)
                    async with session.get(self._url, params=params) as resp1:
                        if resp1.status == 200:
                            print(resp1.url)
                            self.address = (await resp1.json())['content']['address']
                            print(self.address, time.ctime())
                            return self.address
                        else:
                            print('Error Output!')
                            return resp1.status
                else:
                    if resp.status == 200:
                        print(resp.url)
                        self.address = (await resp.json())['content']['address']
                        print(self.address, time.ctime())
                        return self.address
                    else:
                        print('Error Output!')
                        return resp.status

if __name__ == '__main__':
    fin_ip = Fip('220.181.171.195')
    non_ip = Fip()  # 如果没有在请求中指定ip,则默认为当前发送过来的IP进行地址定位
    task = [fin_ip.http_ip(), fin_ip.https_ip(), non_ip.http_ip(), non_ip.https_ip()]
    loop = asyncio.get_event_loop()
    group = asyncio.gather(*task)
    result = loop.run_until_complete(group)  # loop.run_until_complete会自动把协程函数封装成任务，所以不用asyncio.ensure_future创建任务
    print(result, group.result())
    loop.close()