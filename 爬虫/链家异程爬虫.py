import time
from bs4 import BeautifulSoup
from multiprocessing import Pool
import aiomysql
import asyncio
import aiohttp


class Lianjia:

    def __init__(self, url=None, headers=None):
        self.url = url
        self.headers = headers

    async def get_url(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url, headers=self.headers) as resp:  # 在aiohttp中自定义headers
                if resp.status == 200:
                    data = await resp.text()  # 这里的resp.text()是一个协程，使用await读取里面的内容并赋值给data,内容就是网页里的内容
                    soup = BeautifulSoup(data, 'lxml')
                    liitems = soup.select('a.content__list--item--aside')  # 这里只爬取了需要用的标签，如果遇到需要爬取总标签下面的内容而分标签没有则需要先爬取总标签
                    '''
                    没有简化代码前的内容
                     liitems = soup.select('div.content__list')  div.content__list是整个连接页面的总标签，它下面包含了content__list--item--aside标签
                    也可以这样写 li = soup.find_all('div', class_='content__list')
                    urls = []
                    for url in liitems:  然后是把总标签做遍历，把每条标签中的href取出添加进urls列表
                        for i in range(len(url.select('a.content__list--item--aside'))):
                            urls.append(http_url+url.select('a.content__list--item--aside')[i]['href'])
                            注意url.select('a.content__list--item--aside')本身是个列表，所以需要使用索引来获取href
                    '''
                    urls = [self.url+url['href'] for url in liitems]  # 由于返回的列表内容不是网站，而是/zufang/BJ2554111202184151040.html，所以前面需要加入url
                    return urls
                else:
                    return 'error %s' % resp.status

    async def get_info(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers) as resp:  # 在aiohttp中自定义headers
                if resp.status == 200:
                    info = {}
                    data = await resp.text()
                    soup = BeautifulSoup(data, 'lxml')
                    info['标题'] = soup.select('p.content__title')[0].text
                    info['租金'] = soup.select('div.content__aside--title')[0].text[1:8]
                    info['租赁方式'] = soup.select('ul.content__aside__list')[0].text[6:8]
                    info['房屋类型'] = soup.select('ul.content__aside__list')[0].text[14:24]
                    info['朝向楼层'] = soup.select('ul.content__aside__list')[0].text[-22:-13].replace('/', ' ').replace(
                        '：', '')
                    print(info)
                    return info

    async def write_db(self, info, loop):
        global _pool
        _pool = await aiomysql.create_pool(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='root',
            db='ramon',
            loop=loop)
        sql = '''
                insert into 链家爬虫数据库 (`标题`, `租金`, `租赁方式`, `房屋类型`, `朝向楼层`)
                values(%s,%s,%s,%s,%s)
            '''
        value = (info['标题'], info['租金'], info['租赁方式'], info['房屋类型'], info['朝向楼层'])
        async with _pool.acquire() as conn:
            async with conn.cursor() as cur:
                try:
                    await cur.execute("create table if not exists `链家爬虫数据库` (`id` int not null auto_increment primary key,`标题` char(255) not null,`租金` char(255) not null,`租赁方式` char(255) not null,`房屋类型` char(255) not null,`朝向楼层` char(255) not null)")
                    await cur.execute(sql, value)
                    await conn.commit()
                except Exception as e:
                    print(e)
                    await conn.rollback()
def main():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'lianjia_uuid=2f387345-fbf9-430b-9d93-5ef57b3de08e; _smt_uid=5f1e9143.9298709; UM_distinctid=1738f676f8522-07c37b3a70566a-b7a1334-1fa400-1738f676f86495; _ga=GA1.2.902361938.1595838789; select_city=110000; _jzqy=1.1595838788.1596271482.2.jzqsr=baidu|jzqct=lianjia.jzqsr=baidu|jzqct=%E9%93%BE%E5%AE%B6; _jzqckmp=1; _gid=GA1.2.1638092469.1596271483; _jzqx=1.1596275368.1596275368.1.jzqsr=bj%2Elianjia%2Ecom|jzqct=/.-; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221738f67715e295-0eb5a254a9e9ac-b7a1334-2073600-1738f67715f247%22%2C%22%24device_id%22%3A%221738f67715e295-0eb5a254a9e9ac-b7a1334-2073600-1738f67715f247%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22wybeijing%22%2C%22%24latest_utm_content%22%3A%22biaotimiaoshu%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D; CNZZDATA1253477573=550265482-1595834537-https%253A%252F%252Fwww.baidu.com%252F%7C1596350451; CNZZDATA1254525948=932533236-1595836570-https%253A%252F%252Fwww.baidu.com%252F%7C1596349749; CNZZDATA1255633284=2041993544-1595833867-https%253A%252F%252Fwww.baidu.com%252F%7C1596350594; CNZZDATA1255604082=1589575893-1595834809-https%253A%252F%252Fwww.baidu.com%252F%7C1596348427; _qzjc=1; _jzqa=1.241100014125769120.1595838788.1596283015.1596350866.6; _jzqc=1; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1595838796,1596271485,1596350868; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1596350983; _qzja=1.1774120280.1595838787827.1596283015250.1596350865812.1596350975974.1596350983323.0.0.0.23.6; _qzjto=7.1.0; lianjia_ssid=a5070a0b-2a01-e79a-ebb2-b09c5e550786; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiY2I5ZTE5OTJhMTcwMzc0ZDU4NWUyMTMyOWRkZjAzNmVlMmFjZjY5ZGQzY2I5MmIwNzc0YWY4NjAzZTEzYWQzZGJkN2RmMzg1MjRhMzczY2JkZmNjZDBiYTZkMDk5OGRjNjgxNzAzMTI5MmUwZmFjYThmODc3Y2JkMzcxZDNmMTRlYWM3ZmJlMmNmNWEyOThhMmJmNTNmY2Y5OTk5NDgzZGFhYTdmNDc2NzVkY2ZlOTU1ZTAxNGYxNDE4ZTRhNDgxOWMxNTllYmU0MGZjY2IzOTIyN2YyM2MyNzg2Zjk0ZGRmZWQyM2YzNjQwMWNlZjEwODk3YjY4NGRjMDg5MjQ1NGYwZjcyZTI1ZDcwZjZmZmZhNzRhNGFmODQ1NjMzZTY2Nzc0MTI4ZmExNWYxZmZjNzk3OTNjMjMxMDA0MjMyZGU5MDI3NzRhNmIyNDJjYmQ0NjQyOGM3MmIyYzc2N2Y4NVwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCIyZDgwNzFlNlwifSIsInIiOiJodHRwczovL2JqLmxpYW5qaWEuY29tL3p1ZmFuZy8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ==',
        'Host': 'bj.lianjia.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    url = 'https://{}.lianjia.com/zufang/pg{}'.format('bj', 1)
    lj = Lianjia(headers=headers, url=url)
    now = time.time()

    async def main_task():
        set_url = await lj.get_url()
        tasks = await asyncio.gather(*[lj.get_info(i) for i in set_url])
        for i in tasks:
            await lj.write_db(i, loop)  # 由于main_task这个函数是放在loop循环中运行，在运行这个函数之前已经获取了loop循环，所以main_task函数或者数据库中可以先指定loop
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_task())
    end = (time.time() - now) / 60
    print('用时%.4f 秒' % end)


if __name__ == '__main__':
    pool = Pool(4)
    '''
    for i in range(5):  # 使用多进程加协程连续执行5次爬虫，并写入数据库，总用时只有0.05秒，没有进程池只用异程爬取一次总用时0.06秒
        pool.apply_async(func=main)  # 因为多次爬取容易被链家网封锁，所以这里只用作说明多进程或者进程池加异程效率有多高
    '''
    pool.apply_async(func=main)  # 因为进程池中只有一个进程main,所以时间和普通的没有区别，如果有多个main进程就可以使用pool.apply_async异步执行了
    pool.close()
    pool.join()