from socket import *
import socket,time
import threading
from multiprocessing import Process
def client_tcp(conn,addr):
    while True:
        try:
            data=conn.recv(1024)
        except Exception:
            print('客户端退出',addr)
            break
        if data.decode('utf8') in ['exit','EXIT']:
            print('客户端退出', addr)
            break
        else:
            print('客户端发送内容',data.decode('utf8'))
        msg='在[%s]您发送的内容:%s'%(time.strftime("%Y-%m-%d %X"),data.decode('utf8'))
        conn.send(msg.encode('utf8'))
    conn.close()
if __name__ == '__main__':
    # 在windows中创建进程由于没有fork()创建进程, 所以是通过重载自身模块来创建的
    # 如果多进程Process()或者Manager()放在if __name__ == "__main__"外部, 就会进行无限递归循环
    # 所以重点是在windows中所有的多进程程序执行时都必须放在if __name__ == "__main__"里，如果是linux则不用
    print('启动服务器')
    Host = socket.gethostbyname(socket.gethostname())
    Port = 21566
    Addr = (Host, Port)
    s = socket.socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(Addr)
    s.listen(10)
    while True:
        conn, addr = s.accept()
        #t=threading.Thread(target=client_tcp,args=(conn,addr))
        #t.start()
        p=Process(target=client_tcp,args=(conn,addr))
        p.start()
        print('连接的客户端',addr)
