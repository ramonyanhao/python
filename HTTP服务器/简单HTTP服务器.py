import socket
import os
from multiprocessing import Process


def handle_client(client_socket):
    """
    处理客户端请求
    """
    request_data = client_socket.recv(1024)
    print("request data:", request_data)
    # 构造响应数据
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_headers = "Server: My server\r\n"
    response_body = os.popen('tasklist').readlines()
    response = response_start_line + response_headers + "\r\n" + ''.join(response_body)#当遇到连续两个\r\n时，Header部分结束，后面的数据全部是Body

    # 向客户端返回响应数据
    client_socket.send(response.encode('GBK'))

    # 关闭客户端连接
    client_socket.close()


if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", 8000))
    server_socket.listen(128)
    print(server_socket.accept())
    while True:
        client_socket, client_address = server_socket.accept()
        print("[%s, %s]用户连接上了" % client_address)
        handle_client_process = Process(target=handle_client, args=(client_socket,))
        handle_client_process.start()
        # handle_client(client_socket)可以不适用多进程函数Process,直接使用tcp协议函数handle_client(client_socket)
        client_socket.close()