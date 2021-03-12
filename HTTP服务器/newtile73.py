#在windows安装apache需要注意在配置文件httpd.conf中，更改apache安装路径时，不能使用\,需要使用/
#还要注意80端口和443端口是否被占用，如果被占用使用netstat -ano|findstr 端口号查看被哪个PID占用，然后tasklist|findstr PID查看时哪个程序，最后taskkill /pid PID号结束进程释放端口
#或者在httpd.conf中更改默认的80端口，在extra\httpd-ssl.conf配置文件中修改默认端口443,如果遇到配置文件修改失败，可以在conf\original中拷贝原始配置文件进行还原
#在httpd.conf中还要把AddHandler前的#号删除，在后面添加.py,使apache可以运行py脚本文件，还需要更改AllowOverride的值为All,Require的值为all granted，使apache可以接受所有的外部访问
#如果在apache的cgi-bin中运行py脚本出现中文乱码，需要运行
# import codecs, sys
#sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
#需要注意如果安装httpd服务，需要以管理员身份运行cmd,然后在apache安装目录下的bin文件夹中运行httpd -k install
#在apache中，py脚本文件都放在cgi-bin中，使用浏览器访问时路径localhost:端口号/cgi-bin/py文件名.如果是html文件，需要把文件放在htdocs中，访问时只需要输入localhost:端口号/html文件名即可
# htdocs就是html文件的根目录,在apache配置文件中可以把这个默认的htdocs改名为WWW,如
'''
DocumentRoot "D:/Apache2.4/htdocs"
<Directory "D:/Apache2.4/htdocs">
改成
DocumentRoot "D:/Apache2.4/WWW"
<Directory "D:/Apache2.4/WWW">
'''
#在apache配置文件中ScriptAlias /cgi/ "D:/Apache2.4/cgi-bin/"这条指令代表通过网页访问cgi中的脚本时，前面的/cgi/代表网址变量，后面的路径代表访问的文件所在路径
# 还可以在cgi-bin中配置多条默认路径如:
#    ScriptAlias /cgi/ "D:/Apache2.4/cgi-bin/"
#   ScriptAlias /test/ "D:/Apache2.4/test/"
#需要在下面也添加相应的目录属性
'''
<Directory "D:/Apache2.4/cgi-bin">
    AllowOverride All
    Options None
    Require all granted
</Directory>
<Directory "D:/Apache2.4/test">
    AllowOverride All
    Options None
    Require all granted
</Directory>
'''
#post和get两种方式不同的地方在于post不会显示网址?后面的私有数据