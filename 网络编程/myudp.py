import threading
from multiprocessing import Process
from socket import *
def myudp(data,con):
    try:
        if data.decode('utf8') in ['exit','EXIT']:
            print('%s退出'%con[0])
            return
        else:
            print('客户端%s发送的内容:%s'%(con[0],data.decode('utf8')))
    except timeout():
        print('time out')
    msg = '您发送的消息:%s' % data.decode('utf8')
    s.sendto(msg.encode('utf8'), con)
if __name__ == '__main__':
    print('启动UDP服务器')
    s=socket(AF_INET,SOCK_DGRAM)
    host=gethostbyname(gethostname())
    port=9999
    server_ip=(host,port)
    s.bind(server_ip)
    s.settimeout(60)
    while True:
        data,con=s.recvfrom(1024)
        t=threading.Thread(target=myudp,args=(data,con))
        t.start()
