import json,time
import asyncio
import aiohttp
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
        async with aiohttp.ClientSession() as session:
            async with session.get(self._url + func_url, params=params) as resp:
                assert resp.status == 200
                data = await resp.read()  # 由于获取的内容没有json格式，所以这里只能使用resp.read()读取，然后转换为dict,不可以使用resp.json()和resp.text()读取
                data = eval(str(data, encoding="utf-8"))  # 重点:eval函数可以把list,tuple,dict和string相互转化，例如data=b'{"status":0,"result":{"location":{"lng":116.3054340544974,"lat":39.96548984110075},"precise":0,"confidence":20,"comprehension":100,"level":"\xe5\x8c\xba\xe5\x8e\xbf"}}'
                # 此时的data是bytes格式,通过encoding解码，然后里面的内容是字符串内嵌套了字典格式，通过eval转为字典，如果里面是列表则转为列表
                '''
                eval语法：eval(expression[, globals[, locals]])
                expression ： 表达式。
                globals ： 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
                locals ： 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。
                1、简单表达式
                print(eval('1+2'))
                输出结果：3
                2、字符串转字典
                print(eval("{'name':'linux','age':18}")
                输出结果：{'name':'linux','age':18}
                3、传递全局变量
                print(eval("{'name':'linux','age':age}",{"age":1822}))
                输出结果：{'name': 'linux', 'age': 1822}
                4、传递本地变量
                age=18
                print(eval("{'name':'linux','age':age}",{"age":1822},locals()))
                输出结果：{'name': 'linux', 'age': 18}
                '''
                lng = data['result']['location']['lng']
                lat = data['result']['location']['lat']
                return lng, lat  # lat<纬度>,lng<经度>


    async def get_addr(self):
        '''根据坐标获取地址'''
        func_url = '/reverse_geocoding/v3'
        params = self._params.copy()
        params.update(location=",".join(map(str, self._location)))  # 把location这个元组参数改为字符串例如：'31.225696563611,121.49884033194'
        async with aiohttp.ClientSession() as session:
            async with session.get(self._url + func_url, params=params) as resp:
                assert resp.status == 200
                data = await resp.read()
                data = eval(str(data, encoding="utf-8"))
                self._addr = data['result']['formatted_address']
                self._component = data['result']
                return self._addr

if __name__ == '__main__':
    addr = Address(address='北京市海淀区五道口地铁站')
    addr1 = Address(location=(31.225696563611,121.49884033194))
    loop = asyncio.get_event_loop()
    task = [addr1.addr, addr.location]  # 查询地址和坐标
    task1 = [addr1.city, addr1.province, addr1.district]  # 查询具体的城市，省份，区
    group = asyncio.gather(*[asyncio.gather(*task), asyncio.gather(*task1)])  # 把两个组合并为一个组
    loop.run_until_complete(group)
    res = [i.result() for i in asyncio.Task.all_tasks()]
    print(res)
    loop.close()
