from socket import *
connect=socket(AF_INET,SOCK_DGRAM)
server_ip = ('192.168.1.15', 9999)
while True:
    msg=input('>>')
    while not msg:
        print('请输入内容')
        msg = input('>>')
    connect.sendto(msg.encode('utf8'), server_ip)
    if msg in ['exit','EXIT']:
        print('退出')
        break
    else:
        msg=connect.recv(1024)
        if not msg:
            print('服务器超时')
            break
    print('来自服务器的消息:%s'%msg.decode('utf8'))
connect.close()