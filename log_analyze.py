import aiohttp
import asyncio
import re
import ujson, json
import aiofiles
from collections import Counter


class system_log:
    def __init__(self):
        self.data_dic = {}
        self.data_list = []
        self.file = 'Site IT_interview_data_set'
        self.now = 0

    async def key_info(self):
        async with aiofiles.open(self.file, 'r') as f:
            return await f.readlines()

    async def log_info(self):
        log_str = ''.join(await self.key_info())  # 字符串格式日志
        r1 = re.compile(r'May \d+ \d+:\d+:\d+\s.*Configuration Notice:\s+.*\s+.*\s')
        log_list = re.findall(r1, log_str)  # 所有多行日志的列表
        return log_list


    async def sep_info(self, line):
        r = re.compile(r'^May \d+ \d+:\d+:\d+')
        try:
            fr = re.match(r, line).group()
            kr = re.split(r, line)[1]
            return [fr, kr]
        except AttributeError:
            log_list = await self.log_info()
            for i in log_list:
                fr = re.match(r, i).group()
                kr = re.split(r, i)[1]
                return [fr, kr]

    async def analyze_info(self, info):

        self.data_dic['deviceName'] = info[1].split(' ')[1] if info[1].split(' ')[1] != '---' else None

        if info[1].split(':')[0].split(' ')[-1].find('[') > 0:
            self.data_dic['processId'] = info[1].split(':')[0].split(' ')[-1][info[1].split(':')[0].split(' ')[-1].find('[')+1:info[1].split(':')[0].split(' ')[-1].find(']')]
            self.data_dic['processName'] = info[1].split(':')[0].split(' ')[-1][:info[1].split(':')[0].split(' ')[-1].find('[')].strip('(')

        elif not re.search(r'\d', info[1].split(':')[0].split(' ')[-1]):
            self.data_dic['processId'] = None
            self.data_dic['processName'] = info[1].split(':')[0].split(' ')[-1].strip('()')


        else:
            self.data_dic['processId'] = info[1].split(':')[0].split(' ')[-1].split('.')[-1][:info[1].split(':')[0].split(' ')[-1].split('.')[-1].find(')')]
            self.data_dic['processName'] = '.'.join(info[1].split(':')[0].split(' ')[-1].split('.')[:-1]).strip('(')


        self.data_dic['timeWindow'] = info[0].split(' ')[2].split(':')[0] + '00'
        self.data_dic['description'] = ''.join(info[1].split(':')[1:]).strip()
        if int(info[0].split(' ')[2].split(':')[0]) > self.now:
            self.now += 1
            self.data_list.clear()
            self.data_list.append(self.data_dic['processName'])
            self.data_dic['numberOfOccurrence'] = Counter(self.data_list)[self.data_dic['processName']]
        else:
            self.data_list.append(self.data_dic['processName'])
            self.data_dic['numberOfOccurrence'] = Counter(self.data_list)[self.data_dic['processName']]

        return self.data_dic


if __name__ == '__main__':
    async def main():
        sys = system_log()
        async with aiohttp.ClientSession(json_serialize=ujson.dumps, connector=aiohttp.TCPConnector(ssl=False, limit=3)) as session:
            k = await sys.key_info()
            for i in k:
                lines = await sys.sep_info(i)
                json_data = await sys.analyze_info(lines)
                async with session.post('http://127.0.0.1:5100/', json=json_data) as resp:
                    if resp.status == 200:
                        print(await resp.text())

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(main()))
