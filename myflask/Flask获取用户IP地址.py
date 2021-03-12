from flask import Flask, render_template, request
# Initialize the Flask application
app = Flask(__name__)
# Default route, print user's IP
@app.route('/')
def index():
 ip = request.remote_addr  # 一般查看客户端真实IP是通过request.remote_addr看，X-Forwarded-For都是通过nginx往请求头里写入这个值
 ip1 = request.headers  # 这里没有设置nginx做代理或者负载均衡，所以请求头(headers)没有X-Forwarded-For这个字段
 # 在nginx配置中$http_x_forwarded_for就是nginx接受到的http request header中的X-Forwarded-For的值
 # http request header中没有X-Forwarded-For这个header，那$http_x_forwarded_for为空
 # $remote_addr是直接与nginx通信的那台主机的ip。
 # 如果$http_x_forwarded_for为空:  $proxy_add_x_forwarded_for = $http_x_forwarded_for + ',' + $remote_addr
 # 如果$http_x_forwarded_for不为空： $proxy_add_x_forwarded_for = $remote_addr
 '''
 如果在nginx做如下配置，往请求头里写入X-Real-IP,X-Forwarded-For,Host几个变量，后面以$开头的字符串为前面变量的值，这些以$开头的值为nginx自带变量，他们会自动
 这时再看请求头就会多X-Real-IP，X-Forwarded-For和Host出这几项
 server {
       listen       80;
       server_name  www.boke.com;
       location / {
         proxy_set_header X-Real-IP $remote_addr;  proxy_set_header的作用是允许重新定义或添加字段传递给代理服务器的请求头，如果没有定义proxy_set_header时会继承之前定义的值。
         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
         proxy_set_header Host $http_host;
         proxy_set_header X-NginX-Proxy true;
         proxy_pass http://127.0.0.1:9009/;  
         proxy_redirect off; 
            }
         }
    proxy_redirect的作用是重定向被代理服务器返回的响应头，例如这里我们的proxy_redirect设置为off,使用curl -l www.boke.com返回的值Location会暴漏服务器实际地址跟端口9009
    HTTP/1.1 301 Moved Permanently
    Server: nginx
    Date: Thu, 24 Dec 2015 12:08:34 GMT
    Content-Type: text/html; charset=iso-8859-1
    Connection: keep-alive
    Location: http://127.0.0.1:9009/
    所以我们使用proxy_redirect ~^http://127.0.0.1:9009(.*)   http://www.boke.com$1;再用curl -l www.boke.com返回的值Location就是www.boke.com
    [root@localhost nginx]# curl -I http://www.boke.com
    HTTP/1.1 301 Moved Permanently
    Server: nginx
    Date: Thu, 24 Dec 2015 12:08:34 GMT
    Content-Type: text/html; charset=iso-8859-1
    Connection: keep-alive
    Location: http://www.boke.com/

    proxy_pass的作用是代理转发，如果在proxy_pass后面的url加/，表示绝对根路径；如果没有/，表示相对路径，把匹配的路径部分也给代理走
    例如：下面四种情况分别用 http://192.168.1.1/proxy/test.html 进行访问。

第一种：

location /proxy/ {
    proxy_pass http://127.0.0.1/;

}

代理到URL：http://127.0.0.1/test.html

第二种（相对于第一种，最后少一个 / ）

location /proxy/ {
    proxy_pass http://127.0.0.1;

}

代理到URL：http://127.0.0.1/proxy/test.html

第三种：

location /proxy/ {
    proxy_pass http://127.0.0.1/aaa/;

}

代理到URL：http://127.0.0.1/aaa/test.html

第四种（相对于第三种，最后少一个 / ）

location /proxy/ {
    proxy_pass http://127.0.0.1/aaa;

}

代理到URL：http://127.0.0.1/aaatest.html


X-Forwarded-For又称XFF: client, proxy1, proxy2
可以看到，XFF 的内容由「英文逗号 + 空格」隔开的多个部分组成，最开始的是离服务端最远的设备 IP，然后是每一级代理设备的 IP。

如果一个 HTTP 请求到达服务器之前，经过了三个代理 Proxy1、Proxy2、Proxy3，IP 分别为 IP1、IP2、IP3，用户真实 IP 为 IP0，那么按照 XFF 标准，服务端最终会收到以下信息：

X-Forwarded-For: IP0, IP1, IP2
Proxy3 直连服务器，它会给 XFF 追加 IP2，表示它是在帮 Proxy2 转发请求。列表中并没有 IP3，IP3 可以在服务端通过 Remote Address 字段获得。
我们知道 HTTP 连接基于 TCP 连接，HTTP 协议中没有 IP 的概念，Remote Address 来自 TCP 连接，表示与服务端建立 TCP 连接的设备 IP，在这个例子里就是 IP3。

Remote Address 无法伪造，因为建立 TCP 连接需要三次握手，如果伪造了源 IP，无法建立 TCP 连接，更不会有后面的 HTTP 请求。
 '''
 print(ip,ip1)
 return render_template('index.html', user_ip=ip)
if __name__ == '__main__':
 app.run(host='0.0.0.0',port=5000)
'''
注意这里的host=’0.0.0.0‘为了可以让外网客户端访问，但是如果直接使用pycharm运行后服务器还是在127.0.0.1上，只能在CMD中运行这个python文件才可以
需要在run->edit configurations->Additional options里添加--host=0.0.0.0。
注意运行这个脚本不能直接使用右键--run,需要在屏幕右上角点击绿三角旁边的配置文件--选择带有--host=0.0.0.0的配置文件，然后点击绿三角运行脚本

'''
