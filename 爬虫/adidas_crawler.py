import time
from bs4 import BeautifulSoup
from multiprocessing import Pool
import aiomysql
import asyncio
import aiohttp
import os
import re
import requests


class Adidas:
    def __init__(self):
        self.count = 0
        self.info = {}
        self._url = 'https://www.adidas.com.cn/men_newarrivals'
        self._headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'eyeofcloudEndUserId=oeu1591528167539r0.18426108821207499; eyeofcloudSegments=%7B%221%22%3A%22gc%22%2C%222%22%3A%22false%22%2C%223%22%3A%22direct%22%7D; eyeofcloudBuckets=%7B%2254%22%3A%220%22%7D; ADHOC_MEMBERSHIP_CLIENT_ID1.0=6148469f-9e8d-436b-3df8-33268b6efad9; _ga=GA1.3.1256723224.1591528168; locale=zh_CN; _9755xjdesxxd_=32; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221587451%22%2C%22%24device_id%22%3A%221728e789cad565-0bfd166c55cc5-f7d1d38-2073600-1728e789cae8bf%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%221728e789cad565-0bfd166c55cc5-f7d1d38-2073600-1728e789cae8bf%22%7D; the_cookie_footer_banner=the_value; s_c_c_n=0; gdxidpyhxdE=z%5CqEdujqS3PNwix44sqk%5Co5TqXaB7PM4qdY3iWMw1%5Ce6pQyN2L19UbengELoC3w40PQ7m2E2igxRunRD68bKOPkXR8x6YMB70k%5CX2DniKYLxo5ZsRHCuRfSHpAqoyNqwICZLXAk2wcgHW086%5CNQriSWLLeQcjoePapY1GNHprSK0QRZT%3A1596805853908; recommend_tool_cookie_id_v1=1-132ea8b1f13c046296d23f0ce0de058d7f37a18c; f_b_h=Tq7cSrih0TfD5sFGKFQVhvIskPBiq/gwS5VcjsCrs9doPOKoZFdBjG4h2FgpTdDgRIaOYYQ90NdKE1Q7VWZbuXMvXP7MB7bD3kXsWPOw7UfDJOeTVkLB/kBv6/3M9i3Z; _gid=GA1.3.1394045476.1598705032; Hm_lvt_80c6e16552c255ce9d85ca7568a03495=1596790541,1596866393,1596956391,1598705032; XSRF-TOKEN=59ae0722-9dea-4a14-a5d3-fcd85c5cc3bf; _Jo0OQK=1B7A5545C81800E36BCD1829497C1580BA121796D870FC7AE16B33F7AEB49110D346C18064654CB9C03B0A40D962B528B3095BC313D53DC69A92751E19FFB610EE35665F9612581D08FF234CD160F1A9AA0F234CD160F1A9AA0813F1CE9B8CC3F3AGJ1Z1Kw==; firsttime=first; ADHOC_CROSS_PAGE_EXPIDS1.0=%5B%2201bd0d78-e45a-435d-ae2b-d55aa4553279%22%5D; AMCVS_7ADA401053CCF9130A490D4C%40AdobeOrg=1; s_cc=true; AMCV_7ADA401053CCF9130A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C18504%7CMCMID%7C78601691822577403087848265543207445154%7CMCAID%7CNONE%7CMCOPTOUT-1598712233s%7CNONE%7CMCAAMLH-1599309832%7C11%7CMCAAMB-1599309833%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI; recommend_tool_member_id_v1=1; SESSIONID=cba1fee1-6977-4c19-8fe1-330356bd2a76; adidas_recommend_cookie_keyzh_CN=%u8FD0%u52A8%u5427%u5C11%u5E74%u540C%u6B3E%2CPW%2C%u60C5%u4FA3%u88C5%2C%u9632%u6652%u670D%2C%u65B0%u54C1%u4E0A%u5E02%2Cadicolor%2C%u8054%u540D%u6B3E%2CY-3; _pk_id.2_3029faa541cd34f0c6dc7f8b9d17411a.9929=27ee4d8636bca685.1591528168.0.1598705038..; Hm_lpvt_80c6e16552c255ce9d85ca7568a03495=1598705038; utag_main=v_id:01728e789c0400b05d5a9e9d227803072001a06a00bd0$_sn:20$_ss:0$_st:1598706839064$order_id:AD21288380466$ses_id:1598705032410%3Bexp-session$_pn:2%3Bexp-session$_prevpage:PLP%7CG_%E7%94%B7%E5%AD%90%3Bexp-1598708639069; s_sess=%5B%5BB%5D%5D; s_pers=%20pn%3D53%7C1599396953616%3B%20s_vnum%3D1598889600809%2526vn%253D13%7C1598889600809%3B%20s_invisit%3Dtrue%7C1598706839091%3B%20v56%3D%255B%255B%2527SITE%252520NAVIGATION%2527%252C%25271598705039099%2527%255D%255D%7C1756471439099%3B; s_sq=%5B%5BB%5D%5D',
    'Host': 'www.adidas.com.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}

    async def get_session(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self._headers) as resp:
                if resp.status == 200:
                    data = await resp.text()
                    soup = BeautifulSoup(data, 'lxml')
                return soup

    async def get_url(self):
        soup = await self.get_session(self._url)
        limit = soup.select('div.pro-big-img-box')
        urls = [url.a['href'] for url in limit]
        discounts = [i.find('div', class_='badge').text if i.find('div', class_='badge').text else None
                     for i in limit]
        return urls, discounts

    def rename_file(self, filename):
        path = "D:\python\爬虫\jpg\%s.jpg" % filename
        uniq = 1
        while os.path.exists(path):
            path = "D:\python\爬虫\jpg\%s(%d).jpg" % (filename, uniq)
            uniq += 1
        return path

    async def NewGoods(self, url, k):
        soup = await self.get_session(url)
        try:
            self.info['商品'] = soup.select('div.pdp-title.none-sm')[0].h3.text.replace('/', '')
            self.info['价格'] = soup.select('span.goods-price')[0].text if soup.select('span.goods-price.price-single') \
        else '现价:{},原价:{}'.format(soup.select('span.goods-price')[0].text[:soup.select('span.goods-price')[0].text.index('¥', 2)],
                                        soup.select('del.original-price')[0].text)
            self.info['折扣'] = k  # 由于折扣不在传进来的页面中，需要到上一层页面中获取，所以这里设置一个参数k传入从上一层获取出来的折扣的值
            self.info['颜色'] = soup.select('div.pdp-color.events-color-close')[0].h3.text
            self.info['链接'] = soup.select('div.scroll-background-image.icon-play-new')[0].img['src']
            self.info['照片'] = requests.get(self.info['链接']).content
            with open(self.rename_file(self.info['商品']), 'wb') as f:
                f.write(self.info['照片'])  # os.path.abspath(__file__)代表当前文件完整路径,把图片放到jpg文件夹中
            print('爬取一件商品:%s' % self.info['商品'])
            self.count += 1
            return self.info
        except Exception as e:
            print(e)


    async def write_db(self, loop):
        global _pool
        _pool = await aiomysql.create_pool(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='root',
            db='ramon',
            loop=loop)
        sql = '''
                        insert into adidas (`商品`, `价格`, `折扣`, `颜色`, `照片`)
                        values(%s,%s,%s,%s,%s)
                    '''
        value = (self.info['商品'], self.info['价格'], self.info['折扣'], self.info['颜色'], self.info['照片'])
        async with _pool.acquire() as conn:
            async with conn.cursor() as cur:
                try:
                    await cur.execute("create table if not exists `adidas` (`id` int not null auto_increment primary key,"
                                      "`商品` char(255) not null,`价格` char(255) not null,`折扣` char(255),`颜色` char(255) not null,"
                                      "`照片` longblob not null)")
                    await cur.execute(sql, value)
                    await conn.commit()
                except Exception as e:
                    print(e)
                    await conn.rollback()


def main():
    adidas = Adidas()

    async def main_task():
        url_list, discounts = await adidas.get_url()  # url_list是需要爬取的网页列表，discounts是在总页面中爬取出来的折扣列表
        for i in url_list:
            await adidas.NewGoods(i, discounts.pop(0))  # 在循环中每次取出discounts列表中的第一个值discounts.pop(0)并传入进NewGoods函数赋值给self.info['折扣']
            await adidas.write_db(loop)  # 把info字典写入进数据库
        print('共计%d件商品' % adidas.count)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_task())



if __name__ == '__main__':
    now = time.time()
    main()
    end = (time.time() - now) / 60
    print('用时%.4f 秒' % end)
