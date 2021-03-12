import json
from urllib.parse import urlparse,parse_qs
from wsgiref.simple_server import make_server
import os
#服务器后台运行任务，获取任务运行状态并且作为api的返回参数
def application(environ, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    params = urlparse(environ['QUERY_STRING'])# environ是当前请求的所有数据,返回是string类型,包括Header和URL，body，urlparse取得URL并返回一个元组
    # (scheme:协议(http或者https)，netloc:域名(www.baidu.com)，path:路径，query:参数一般是get方式的网页?后面的部分)
    parse_qs(params.query)
    #parse_qs解析query，返回词典格式数据，词典的key是query中变量名字，value是对应的值例如:params=urlparse("http://www.google.com/search?hl=en&q=urlparse&btnG=")
    #返回scheme='http', netloc='www.google.com', path='/search', params='', query='hl=en&q=urlparse&btnG=', fragment='',再使用parse_qs(params.query)返回{'q': ['urlparse'], 'hl': ['en']}
 # 获取当前get请求的所有数据，返回是string类型
    #如果使用post获取所有数据，请使用wsgi.input,具体看前端html使用的是post还是get方式
    #request_body = environ["wsgi.input"].read(int(environ.get("CONTENT_LENGTH", 0)))
    job = os.popen("tasklist|findstr chrome").readlines()#os.system执行系统命令返回值为0或者1表示成功或者失败，而os.popen执行系统命令返回值是文件句柄，相当于打开文件，通过readlines读取出来
    job = job[0]
    return job#这里传入的是字符串，需要把C:\Users\ramon\AppData\Local\Programs\Python\Python37\lib\wsgiref\handlers.py中的data加上if data is not bytes:data=data.encode()
if __name__ == "__main__":
    port =5088
    httpd = make_server("0.0.0.0", port, application)
    print("serving http on port {0}...".format(str(port)))
    httpd.serve_forever()
    #python -m http.server 9999可以直接创建一台http服务器,显示当前路径下的所有文件列表