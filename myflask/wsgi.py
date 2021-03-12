from test import app#这样就把flask应用中所有的处理函数都导入进来
from wsgiref.simple_server import make_server#使用make_server启动flask中的app

if __name__=='__main__':

    httpd=make_server('localhost',8080,app)
    httpd.serve_forever()