#直接使用命令python -c "python命令行"可以直接在cmd中输出python命令，例如：
# python -c "import os;print(os.getlistdir())输出当前路径下的文件，注意有一点不同的是-c后面是以字符串形式转为命令行，所以想要输出函数需要用print打印出来
# 复杂的命令行需要用[]包括起来，多行命令用多个[]，用;分隔开，例如:python -c "import os;[print (os.getcwd())];[print(os.listdir())]"
# 而mysql使用-e参数在cmd中输出mysql命令，例如:mysql -uroot -pmanageMENT!1 -e "use testdb;select * from employee"
# 创建两个py文件，server端:
'''
#!C:\\Users\\ramon\\AppData\\Local\\Programs\\Python\\Python37\\python.exe
# 导入 socket、sys 模块
import socket
import sys

# 创建 socket 对象
serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()
port = 9999
# 绑定端口号
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)

while True:
    # 建立客户端连接
    clientsocket,addr = serversocket.accept()

    print("连接地址: %s" % str(addr))

    msg='欢迎访问菜鸟教程！'+ "\r\n"
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()

客户端
#!C:\\Users\\ramon\\AppData\\Local\\Programs\\Python\\Python37\\python.exe
# 导入 socket、sys 模块
import socket
import sys

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

# 设置端口号
port = 9999

# 连接服务，指定主机和端口
s.connect((host, port))

# 接收小于 1024 字节的数据
msg = s.recv(1024)

s.close()

print (msg.decode('utf-8'))

打开两个cmd窗口，一个运行server.py，一个运行client.py,server端检测到有连接的时候就会执行print("连接地址: %s" % str(addr))
再打开第一个终端，就会看到有以下信息输出--连接地址： ('192.168.0.118', 33397),由于client没有while True循环，所以打开后就关闭了，然后输出欢迎访问菜鸟教程！
'''