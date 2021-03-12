from socket import *
import socket
s=socket.socket(AF_INET,SOCK_STREAM)
host='192.168.1.15'
port=21566
addr=(host,port)
s.connect(addr)
while True:
    data=input('>>>')
    while not data:
        print('请输入内容')
        data = input('>>>')
    s.send(data.encode('utf8'))
    if data in ['exit','EXIT']:
        print('客户端退出')
        break
    else:
        data=s.recv(1024)
        if not data:
            print('服务器无响应')
            break
    print(data.decode('utf8'))
s.close()
