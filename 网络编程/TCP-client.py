#!C:\Users\ramon\AppData\Local\Programs\Python\Python37\python.exe
# -*-coding:utf-8 -*-
from socket import *
from time import ctime
HOST = '192.168.1.15' #服务端ip
PORT = 21566 #服务端端口号
BUFSIZ = 1024
ADDR = (HOST, PORT)
tcpCliSock = socket(AF_INET, SOCK_STREAM) #创建socket对象
tcpCliSock.connect(ADDR) #连接服务器
while True:
    data = input('>>')
    while not data:
        print('请输入内容')
        data = input('>>')
    tcpCliSock.send(data.encode('utf-8'))  # 发送消息
    if data in ['exit','EXIT']:
        print('客户端退出')
        break
    else:
        data = tcpCliSock.recv(BUFSIZ) #读取消息
        if not data:
            print('服务器无响应，请重新连接')
            break
    print(data.decode('utf-8'))
tcpCliSock.close() #关闭客户端