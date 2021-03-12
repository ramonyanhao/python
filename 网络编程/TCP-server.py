# -*-coding:utf-8 -*-
from socket import *
import socket
import time
import threading
COD = 'utf-8'
HOST = socket.gethostbyname(socket.gethostname()) # 主机ip
PORT = 21566 # 软件端口号
BUFSIZ = 1024
ADDR = (HOST, PORT)
SIZE = 10
tcpS = socket.socket(AF_INET, SOCK_STREAM) # 创建socket对象，套接字类型：可以是 SOCK_STREAM（流式套接字，主要用于 TCP 协议），或者 SOCK_DGRAM（数据报套接字，主要用于 UDP 协议）
tcpS.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) # 重用ip和端口,端口释放后会等待两分钟之后才能再被使用，SO_REUSEADDR是让端口释放后立即就可以被再次使用,SOL_SOCKET是套接字层本身
tcpS.bind(ADDR) # 绑定ip端口号
tcpS.listen(SIZE)  # 设置最大链接数
def tcp_link(conn,addr):
    while True:
        try:
            data = conn.recv(BUFSIZ) # 读取已链接客户的发送的消息
        except Exception:
            print("断开的客户端", addr)
            break

        if not data or data.decode('utf-8') in ['exit','EXIT']:
            print("断开的客户端", addr)
            break
        else:
            print("客户端发送的内容:", data.decode(COD))
        msg = time.strftime("%Y-%m-%d %X") #获取结构化事件戳
        msg1 = '[%s]:%s' % (msg, data.decode(COD))
        conn.send(msg1.encode(COD)) #发送消息给已链接客户端
    conn.close() #关闭客户端链接
print("服务器启动，监听客户端链接")
while True:
    conn,addr = tcpS.accept()
    t=threading.Thread(target=tcp_link,args=(conn,addr))
    t.start()
    print("链接的客户端", addr)
