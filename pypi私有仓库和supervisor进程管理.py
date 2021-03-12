'''
Supervisor是用Python开发的一套通用的进程管理程序，能将一个普通的命令行进程变为后台daemon，并监控进程状态，异常退出时能自动重启
最好使用yum安装supervisor,如果使用pip安装就需要手动配置supervisor服务和配置文件，下面进行安装
yum install epel-release(企业Linux的额外软件包)必须要先安装epel才可以再安装supervisor,否则yum提示找不到supervisor软件包
yum install supervisor
supervisord：装好supervisor软件后，supervisord用于启动supervisor服务。
supervisorctl：用于管理supervisor配置文件中program。
在/etc/supervisord.conf配置文件中的最后把*.ini改为*.conf至此supervisor安装完成并且通过supervisorctl status查看到下面没有正在管理的进程
systemctl enable supervisord开启supervisor服务开机自启动，systemctl start supervisord启动supervisor服务
我们的目的就是通过supervisor管理pypi，这样可以省去使用nohup来创建pypi后台进程

pypi可以在自己的服务器上搭建私有仓库，使用twine软件可以上传自己制作好的pip安装包到pypi私有仓库
先在服务器创建账户 useradd pypi
为了不污染全局的python环境，我们使用虚拟环境来安装各种组件
python -m venv venv 在当前目录下创建了一个venv的文件夹
source venv/bin/activate 激活虚拟环境
pip install pypiserver
然后进入pypi的账户目录下创建一个目录packages,使用这个目录作为我们上传包到pypi私有仓库的目录
mkdir packages
pip install passlib 软件passlib是用来生成密码文件
htpasswd -sc .htaccess user 上传package需要用户名密码，密码文件.htaccess使用命令htpasswd命令生成,回车后会提示输入密码，输入123456
pypi-server应该在后台运行，简单的话可用使用nohup命令，但一般都用supervisor来管理。在当前目录创建pypi-server.conf
[program:pypi-server]
directory=/home/pypi/
command=/home/pypi/venv/bin/pypi-server -p 10086 -P /home/pypi/.htaccess /home/pypi/packages
autostart=true
autorestart=true
redirect_stderr=true
其中-p选项指定侦听的端口，-P选项指定密码文件
如果不想使用supervisor管理pypi,可以不用创建这个配置文件，直接使用nohup /home/pypi/venv/bin/pypi-server -p 10086 -P /home/pypi/.htaccess /home/pypi/packages &来启动pypi
然后客户端通过网页打开http://服务器ip:10086就可以看到pypiserver的欢迎页面
使用python -m twine upload --repository-url http://192.168.43.128:10086 需要上传的包路径 就可以上传自己的包到pypi私有仓库里了，然后在服务器端的/home/pypi/packages目录下可以看到刚刚上传的文件
如果使用supervisor管理pypi,执行ln -s /home/pypi/pypi-server.conf /etc/supervisord.d/pypi-server.conf创建一个软链接到supervisor配置文件指定的目录中，还记得上面把supervisor配置文件最后的ini改为conf吗
执行supervisorctl reload
supervisorctl status再次查看supervisor下面正在管理的进程，这时会出现
pypi-server                      RUNNING    pid 27289, uptime 16:41:19
这就代表我们通过supervisor软件管理了pypi，也可以把其他的程序通过创建conf文件并且软连接到/etc/supervisord.d/中进行管理，就可以省去nohup创建很多后台进程不好管理的局面，比如uwsgi
supervisorctl status        //查看所有进程的状态
supervisorctl stop es       //停止es
supervisorctl start es      //启动es
supervisorctl restart       //重启es
supervisorctl update        //配置文件修改后使用该命令加载新的配置
supervisorctl reload        //重新启动配置中的所有程序
然后安装twine用来上传制作好的包 pip install twine
安装setuptools用来制作自己的包 pip install setuptools
这里使用虚拟机中的polls制作成一个polls包，在根目录下创建一个django-polls目录，然后把polls拷贝到这个目录下，
为了让创建的应用包包含额外文件，我们需要在django-polls中创建一个名为 MANIFEST.in 的文件，内容如下
recursive-include polls/static *
recursive-include polls/templates *
recursive-include docs *
如果还想包含其他目录都可以填入这个文件中，最后的recursive-include docs *是为了以后如果需要增加一些说明文档，就可以直接把这些文档放在docs目录中
创建setup.py文件
from setuptools import setup
setup()
保存退出后执行python -m setup.py sdist 后在django-polls中会自动创建一个dist目录并构建应用包 django-polls-0.1.tar.gz
现在就可以直接安装这个应用包，pip install /django-polls/dist/django-polls-0.1.tar.gz
安装完后如果需要使用这个包，就更改使用这个包的项目文件，例如，先更改urls.py
from django.urls import include
增加一条 path('py/polls/', include('polls.urls'))
再更改settings.py文件，在INSTALLED_APPS下增加polls,增加静态文件目录 STATICFILES_DIRS = [os.path.join(BASE_DIR,'polls/static')]
保存退出到项目目录，使用manage.py migrate增加polls中的模板到当前数据库，重启这个项目，客户端访问http://192.168.43.128/py/polls/
这样就代表我们的应用包已经成功了，以后有项目需要使用这里的功能就可以下载安装，测试完这个应用包后就可以上传到pypi仓库了
python -m twine upload --repository-url http://192.168.43.128:10086 /django-polls/dist/django-polls-0.1.tar.gz
提示输入用户名和密码，用户名就是通过htpasswd创建的user,密码是123456,因为pypi-server.conf配置文件中指定的密码文件.htaccess
服务器端在/home/pypi/packages目录中就可以看到刚刚上传过来的django-polls-0.1.tar.gz应用包
'''

