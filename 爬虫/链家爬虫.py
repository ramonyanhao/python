import requests
import re,time
from bs4 import BeautifulSoup
from multiprocessing import Pool, Queue
import pymysql


def get_url(city, pg):
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
    session = requests.session()
    session.headers.clear()
    session.headers.update(headers)
    http_url = 'https://{}.lianjia.com/zufang/pg{}'.format(city, pg)  # city可以更换其他城市,pg更换一个页面
    response = session.get(http_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')  # lxml是帮助我们解析HTML、XML文件，快速定位，搜索、获取特定内容的Python库。我们知道，对于纯文本的HTML文件的查找可以使用正则表达式、BeautifulSoup等完成。lxml也是对网页内容解析的一个库
        liitems = soup.select('div.content__list')
        # 也可以这样写 li = soup.find_all('div', class_='content__list'),注意url.select('a.content__list--item--aside')本身是个列表，所以需要使用索引来获取href
        urls = []
        for url in liitems:
            for i in range(len(url.select('a.content__list--item--aside'))):
                urls.append(http_url+url.select('a.content__list--item--aside')[i]['href'])  # 由于返回的列表内容不是网站，而是/zufang/BJ2554111202184151040.html，所以前面需要加入http_url
        return urls
    else:
        return 'error %s'% response.status_code


def Regular_expression(url):  # 如果使用正则表达式来获取需要的信息
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
    session = requests.session()
    session.headers.clear()
    session.headers.update(headers)
    response = session.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        limit = soup.select('div.content__list')
        re_set = re.compile('<a.*?class="content__list--item--aside".*?href="(.*?)"')  # <a class="content__list--item--aside" href="/zufang/BJ2554111202184151040.html" target="_blank" title="整租·东泽园 1室1厅 南">是整个字符串，
        # 注意href="(.*?)"最后的",因为?非贪婪模式只匹配最少的字符，所以从前面匹配到href="开始，然后中间括号中的内容.*?匹配了网址https://bj.lianjia.com/ershoufang/101108575010.html
        # 最重要的是最后的",因为使用了贪婪模式.*?，所以到网址后面的双引号结束，但是如果使用了贪婪模式.*,就会把target="_blank"也匹配进去，href="(.*?)"多了一个括号，只保留括号中的内容,其他舍弃
        '''
        非贪婪操作符“？”，这个操作符可以用在"*","+","?"的后面，要求正则匹配的越少越好
        >>> re.match(r"aa(\d+)","aa2343ddd").group(1)
        '2343'
        >>> re.match(r"aa(\d+?)","aa2343ddd").group(1)
        '2'
        >>> re.match(r"aa(\d+)ddd","aa2343ddd").group(1) 
        '2343'
        >>> re.match(r"aa(\d+?)ddd","aa2343ddd").group(1)
        '2343'
        '''
        re_get = re.findall(re_set, str(limit))  # 最后通过findall把href="(.*?)"括号中匹配的内容返回
        return re_get


def get_info(url):
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
    session = requests.session()
    session.headers.clear()
    session.headers.update(headers)
    response = session.get(url)
    if response.status_code == 200:
        info = {}
        soup = BeautifulSoup(response.text, 'lxml')
        info['标题'] = soup.select('p.content__title')[0].text
        info['租金'] = soup.select('div.content__aside--title')[0].text[1:8]
        info['租赁方式'] = soup.select('ul.content__aside__list')[0].text[6:8]
        info['房屋类型'] = soup.select('ul.content__aside__list')[0].text[14:24]
        info['朝向楼层'] = soup.select('ul.content__aside__list')[0].text[-22:-13].replace('/', ' ').replace('：', '')
        print(info)
        return info


def get_db():
    conn = {
        'host':'localhost',
        'user':'root',
        'password':'root',
        'database':'ramon',
        'charset':'utf8mb4'
    }
    return pymysql.connect(**conn)


def up_db(info):
    db = get_db()  # 把db写进函数中，不用在main函数的apply_async中调用并传参
    sql = '''
        insert into 链家爬虫数据库 (`标题`, `租金`, `租赁方式`, `房屋类型`, `朝向楼层`)
        values(%s,%s,%s,%s,%s)
    '''
    value = (info['标题'], info['租金'], info['租赁方式'], info['房屋类型'], info['朝向楼层'])
    cursor = db.cursor()
    try:
        cursor.execute(sql, value)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    # 另一种sql语句执行方法:
    '''
    values = "'{}'," * 4 + "'{}'"  这里是因为要有5个values,所以需要创建5个{},而且使用,隔开，但是在最后不能有逗号，所以只能使用"{}，"*4再另加一个{}保证最后不会有逗号
    sql_value = values.format(info['标题'], info['租金'], info['租赁方式'], info['房屋类型'], info['朝向楼层'])
    sql = 
        insert into 链家爬虫数据库 (`标题`, `租金`, `租赁方式`, `房屋类型`, `朝向楼层`)
        values({}).format(sql_value)       
    '''


def main():  # 多进程池方法，总计用时0.08秒
    Regular_expression('https://bj.lianjia.com/zufang/')  # 通过正则表达式返回网页列表
    db = get_db()
    cur = db.cursor()
    cur.execute(
        "create table if not exists `链家爬虫数据库` (`id` int not null auto_increment primary key,`标题` char(255) not null,`租金` char(255) not null,`租赁方式` char(255) not null,`房屋类型` char(255) not null,`朝向楼层` char(255) not null)")
    pool = Pool(4)  # 一下写入4条数据
    now = time.time()
    for info in pool.map(get_info, get_url('bj', 2)):  # 使用pool.map和map函数一样，把get_url函数的返回值中的每个元素当作参数返回给get_info
        # pool.apply_async(up_db, args=(info, db))  # 加上参数db后代码执行没有问题，但是不会把数据写进数据库中
        pool.apply_async(up_db, args=(info,))  # 使用异步把数据写入到数据库中,注意这里修改了之前的db,没有把db变量当参数传进apply_async的args中
    count = time.time() - now
    print('总计用时%.2f 秒' % (count/60))
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()

'''
普通方法，总计用时0.2秒

def main():
    Regular_expression('https://bj.lianjia.com/zufang/')  # 通过正则表达式返回网页列表

    count = 0
    for i in get_url('bj', 2):
        now = time.time()
        info = get_info(i)
        up_db(info)
        end = (time.time() - now) / 60
        print('用时%.4f 秒' % end)
        count += end

    print('总计用时%.2f 秒' % count)


if __name__ == '__main__':
    main()
'''
