import json,time
import requests
import asyncio
import threading
from multiprocessing import Process
class Address:
    def __init__(self, address=None, location=None):
        self._addr = address
        self._location = location
        self._url = 'http://api.map.baidu.com'
        self._params = {'output':'json','ak':'wiw57wInUncbNdFGuZz5sPRc1UEqiTyO'}
        self._component = None  # 返回数据中的result

    @property
    async def city(self):  # 城市
        await self.get_addr()
        print(time.ctime())
        return self._component['addressComponent']['city']

    @property
    async def province(self):  # 省份
        await self.get_addr()
        print(time.ctime())
        return self._component['addressComponent']['province']


    @property
    async def district(self):  # 区
        await self.get_addr()
        print(time.ctime())
        return self._component['addressComponent']['district']

    @property
    async def addr(self):
        print(time.ctime())
        return await self.get_addr()

    @property
    async def location(self):
        print(time.ctime())
        return self._location if self._location else await self.get_location()


    async def get_location(self):
        '''根据地址获取坐标'''
        func_url = '/geocoding/v3'
        params = self._params.copy()
        params.update(address=self._addr)
        result = requests.get(self._url + func_url, params=params)
        jdata = json.loads(result.text)
        if jdata['status'] == 0:
            lng = jdata['result']['location']['lng']
            lat = jdata['result']['location']['lat']
            return lng, lat  # lat<纬度>,lng<经度>
        else:
            print("Error output!:")
            return jdata['status']


    async def get_addr(self):
        '''根据坐标获取地址'''
        func_url = '/reverse_geocoding/v3'
        params = self._params.copy()
        params.update(location=",".join(map(str, self._location)))  # 把location这个元组参数改为字符串例如：'31.225696563611,121.49884033194'
        res = requests.get(self._url + func_url, params=params)
        jdata = json.loads(res.text)
        if jdata['status'] == 0:
            self._addr = jdata['result']['formatted_address']
            self._component = jdata['result']
            return self._addr
        else:
            print("Error output!:")
            return jdata['status']

if __name__ == '__main__':
    addr = Address(address='北京市海淀区五道口地铁站')
    addr1 = Address(location=(31.225696563611,121.49884033194))
    loop = asyncio.get_event_loop()
    task = [asyncio.ensure_future(i) for i in [addr1.addr, addr.location]]
    task1 = [asyncio.ensure_future(i) for i in [addr1.city, addr1.province, addr1.district]]
    loop.run_until_complete(asyncio.gather(*[asyncio.gather(*task), asyncio.gather(*task1)]))
    res = [i.result() for i in asyncio.Task.all_tasks()]
    print(res)
    loop.close()
