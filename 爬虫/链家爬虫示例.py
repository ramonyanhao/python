import json
from multiprocessing import Pool
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import pymongo
# Cookie，类型为“小型文本文件”，是某些网站为了辨别用户身份，进行Session跟踪而储存在用户本地终端上的数据（通常经过加密），由用户客户端计算机暂时或永久保存的信息
session=requests.session()
# requests是基于上下文管理器做的自动关闭session，而session基于http长连接sokcet，保留历史请求的状态，这就对依赖于登陆状态的二次请求提供了很便利的途径
# 说白了在某些需要账户密码登陆的网站使用session可以在每次请求都保持登陆状态，不用每次requests都使用登陆账户和密码,也就是一直保持cookie缓存
# session还有一个好处是requests中的session对象能够让我们跨http请求保持某些参数，即让同一个session对象发送的请求头携带某个指定的参数，例如:
# session.headers.update({'x-test': 'true'}),r1 = session.get('http://httpbin.org/headers', headers={'x-test2': 'true'})，r2 = session.get('http://httpbin.org/headers')
# r1和r2的区别就是r1在原有的session.headers里面加入了x-test2,而r2没有x-test2,r1.text的返回值:"X-Test": "true", "X-Test2": "true",r2.text的返回值:"X-Test": "true"
# 从结果中我们可以得出两条结论：
# session可以为请求方法提供缺省数据，比如第一次请求session.headers.update()的{'x-test': 'true'}就是缺省数据，此时的缺省数据就是跨请求参数。
# 方法级别的参数不会被跨请求保持，比如第二次请求时，没有携带headers={'x-test2': 'true'}，返回的结果中也没有{'x-test2': 'true'}，说明该参数没有在第一次请求后被保持住。
def generate_allurl(user_in_nub, user_in_city):  # 生成url
    url = 'http://' + user_in_city + '.lianjia.com/ershoufang/pg{}/'
    for url_next in range(1, int(user_in_nub)):
        yield url.format(url_next)


def get_allurl(generate_allurl):  # 分析url解析出每一页的详细url

    # 这里模拟一下请求头，头文件是从浏览器里面抓到的，否则服务会回复403错误，（其实就是服务器做的简单防爬虫检测）
    # 在请求网页爬取的时候，输出的text信息中会出现抱歉，无法访问等字眼，这就是禁止爬取，需要通过反爬机制去解决这个问题。
    # headers是解决requests请求反爬的方法之一，相当于我们进去这个网页的服务器本身，假装自己本身在爬取数据。
    # 对反爬虫网页，可以设置一些headers信息，模拟成浏览器取访问网站 。
    headers={
        'Host':'xa.lianjia.com',
        'Connection':'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cookie':'TY_SESSION_ID=bd212f0d-fa69-41b2-bd24-b147b1aa6f93; lianjia_uuid=4479a173-a725-499e-ae06-99e9e2d78c3a; UM_distinctid=167e9c20cd221b-0d1bfec5576324-10724c6f-1fa400-167e9c20cd42aa; select_city=442000; _jzqckmp=1; all-lj=c60bf575348a3bc08fb27ee73be8c666; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1546392681,1546572269,1546591543,1546591988; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1546591988; _smt_uid=5c23441b.121b752a; CNZZDATA1254525948=1906388473-1545883862-%7C1546590852; CNZZDATA1255633284=2126119324-1545884076-%7C1546587312; CNZZDATA1255604082=1549936819-1545883843-%7C1546591140; _jzqa=1.351604181808559040.1545815068.1546591544.1546591990.9; _jzqc=1; _jzqb=1.1.10.1546591990.1; _qzja=1.757497874.1545885920295.1546591543773.1546591989755.1546591839817.1546591989755.0.0.0.10.7; _qzjb=1.1546591543773.4.0.0.0; _qzjc=1; _qzjto=5.3.0; _ga=GA1.2.763502423.1545815070; _gid=GA1.2.1829352401.1546591547; lianjia_ssid=f3e5db05-9789-4d8e-aae2-80b919a3cfa8'
    }
    session.headers.clear()
    session.headers.update(headers)

    get_url = session.get(generate_allurl)
    if get_url.status_code == 200:
        #原来代码用没有正则搜索出结果，这里屏蔽下，用BS完成所有赛选
        #re_set = re.compile('<li.*?class="clear">.*?<a.*?class="img.*?".*?href="(.*?)"')
        #re_get = re.findall(re_set, get_url.text)
        soup = BeautifulSoup(get_url.text, 'html5lib')
        # liitem = soup.findall('li',{'class':'clear LOGCLICKDATA'})
        urls=[]
        liitems = soup.select('li.clear.LOGCLICKDATA')
        for item in liitems:
            url = item.select('a')[0]['href']
            urls.append(url)
        return urls


def open_url(re_get):  # 分析详细url获取所需信息

    headers={
        'Host':'xa.lianjia.com',
        'Connection':'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cookie':'TY_SESSION_ID=bd212f0d-fa69-41b2-bd24-b147b1aa6f93; lianjia_uuid=4479a173-a725-499e-ae06-99e9e2d78c3a; UM_distinctid=167e9c20cd221b-0d1bfec5576324-10724c6f-1fa400-167e9c20cd42aa; select_city=442000; _jzqckmp=1; all-lj=c60bf575348a3bc08fb27ee73be8c666; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1546392681,1546572269,1546591543,1546591988; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1546591988; _smt_uid=5c23441b.121b752a; CNZZDATA1254525948=1906388473-1545883862-%7C1546590852; CNZZDATA1255633284=2126119324-1545884076-%7C1546587312; CNZZDATA1255604082=1549936819-1545883843-%7C1546591140; _jzqa=1.351604181808559040.1545815068.1546591544.1546591990.9; _jzqc=1; _jzqb=1.1.10.1546591990.1; _qzja=1.757497874.1545885920295.1546591543773.1546591989755.1546591839817.1546591989755.0.0.0.10.7; _qzjb=1.1546591543773.4.0.0.0; _qzjc=1; _qzjto=5.3.0; _ga=GA1.2.763502423.1545815070; _gid=GA1.2.1829352401.1546591547; lianjia_ssid=f3e5db05-9789-4d8e-aae2-80b919a3cfa8'
    }
    session.headers.clear()
    session.headers.update(headers)

    res = session.get(re_get)
    if res.status_code == 200:
        info = {}
        soup = BeautifulSoup(res.text, 'lxml')
        info['标题'] = soup.select('.main')[0].text
        info['总价'] = soup.select('.total')[0].text + '万'
        info['每平方售价'] = soup.select('.unitPriceValue')[0].text
        info['参考总价'] = soup.select('.taxtext')[0].text
        info['建造时间'] = soup.select('.subInfo')[2].text
        info['小区名称'] = soup.select('.info')[0].text
        info['所在区域'] = soup.select('.info a')[0].text + ':' + soup.select('.info a')[1].text
        info['链家编号'] = str(re_get)[34:].rsplit('.html')[0]
        # for i in soup.select('.base li'):
        #     i = str(i)
        #     if '</span>' in i or len(i) > 0:
        #         key, value = (i.split('</span>'))
        #         info[key[24:]] = value.rsplit('</li>')[0]
        # for i in soup.select('.transaction li'):
        #     i = str(i)
        #     if '</span>' in i and len(i) > 0 and '抵押信息' not in i:
        #         key, value = (i.split('</span>'))
        #         info[key[24:]] = value.rsplit('</li>')[0]
        print(info)
        return info

def update_to_MongoDB(one_page):  # update储存到MongoDB
    Mongo_Url = 'localhost'
    Mongo_DB = 'Lianjia'
    Mongo_TABLE = 'Lianjia' + '\n' + str('zs')
    client = pymongo.MongoClient(Mongo_Url)
    db = client[Mongo_DB]
    if db[Mongo_TABLE].update({'链家编号': one_page['链家编号']}, {'$set': one_page}, True): #去重复
        # print('储存MongoDB 成功!')
        return True
    return False

# pandas写excel只找到了一次写入没找到追加方式，暂时不用吧
def pandas_to_xlsx(info):  # 储存到xlsx
    pd_look = pd.DataFrame(info,index = False)
    pd_look.to_excel('链家二手房.xlsx', sheet_name='链家二手房')

def writer_to_text(list):  # 储存到text
    with open('链家二手房.text', 'a', encoding='utf-8')as f:
        f.write(json.dumps(list, ensure_ascii=False) + '\n')  # json.dumps 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False
        f.close()

def main(url):
    info = open_url(url)
    writer_to_text(info)    #储存到text文件
    # pandas_to_xlsx(info)    #储存到xlsx文件
    update_to_MongoDB(info)   #储存到Mongodb

if __name__ == '__main__':
    # user_in_city = input('输入爬取城市：')
    # user_in_nub = input('输入爬取页数：')

    pool = Pool()
    for i in generate_allurl('2', 'xa'):
        pool.map(main, [url for url in get_allurl(i)])  # pool.map将列表中的每个元素提取出来当作main函数的参数，创建一个个进程，放进进程池中
# 第一个参数是函数，第二个参数是一个迭代器，将迭代器中的数字作为参数依次传入函数中,作用：这是多进程的创建，应用在爬虫中主要目的是提高爬取的效率，实现秒爬