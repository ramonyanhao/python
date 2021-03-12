'''
ansible使用远程连接客户端有时出现需要sudo权限，有2中方法：
1.在使用ansible 分组名 -b -m service -a "name=nginx state=started" -u sshuser -K 提示输入sudo用户sshuser的密码
2.创建用户sshuser,并且把这个用户加入到wheel组,修改客户端的/etc/sudoers文件，把%wheel  ALL=(ALL)   NOPASSWD:ALL前的#注释取消，wheel组中的所有用户就可以无密码使用sudo
  或者修改成sshuser   ALL=(ALL)       NOPASSWD: ALL就可以指定某个账户可以无密码使用sudo权限
  然后使用ansible 分组名 -b -m service -a "name=nginx state=started" -u sshuser不需要再输入sshuser的密码就可以远程执行启动nginx服务了
ansible和其他自动运维工具不同的地方是ansible不需要在所有服务器中安装客户端，ansible直接使用ssh协议远程控制所有服务器的，所以需要先使用ssh远程测试登陆这些服务器，具体步骤:
在没有安装ansible的机器上安装openssh-server,保证ansible的机器可以通过ssh连接过来，在/etc/ssh/sshd_config配置文件中配置以下选项
PubkeyAuthentication yes  使用公钥文件验证登陆
PasswordAuthentication no  不用密码验证登陆
PermitRootLogin no  限制使用root账户登陆，不过这里第一次先改为yes,因为第一次需要把ansible机器上的公钥文件拷贝过来
在安装了ansible的机器上安装openssh-clients,使用ssh-keygen生成密钥文件，默认保存在当前用户目录下的.ssh/中
然后使用ssh-copy-id root@安装了openssh-server的机器IP地址，把生成的公钥文件拷贝到远程机器的authorized_keys文件中
尝试使用ssh -i 私钥文件 sshuser@远程机器IP，如果可以正常连接就表示ssh安装成功，再把PermitRootLogin  yes改为no
在ansible中修改默认配置文件：/etc/ansible/ansible.cfg:
[defaults]
#inventory      = /etc/ansible/hosts                        #主机列表配置文件
#library        = /usr/share/my_modules/                    #库文件存放目录
#remote_tmp     = ~/.ansible/tmp                            #临时py命令文件存放在远程主机目录
#local_tmp      = ~/.ansible/tmp                            #本机的临时命令执行目录
#forks          = 5                                         #默认的并发数
#sudo_user      = root                                      #默认sudo用户
#ask_sudo_pass = True
#ask_pass      = True                                       #每次执行ansible命令是否询问ssh密码
#remote_port    = 22                                        #目标主机端口默认22
#host_key_checking = False                                  #检查对应服务器的host_key
#log_path = /var/log/ansible.log                            #日志文件
#module_name = command                                      #默认使用模块
以上为ansible的配置文件，一般保持默认无需改变
但为了方便可以修改下面三个选项
host_key_checking = False                           #此行注释去除，否则每次将检查主机的host_key
log_path = /var/log/ansible.log                     #将日志文件打开，方便查看操作日志
module_name = shell                                 #将默认的模块改为shell，command模块功能太弱
默认清单配置文件位于/etc/ansible/hosts中，清单文件hosts就是受控节点的列表，所有要管理的主机列表
[nodes]  分组名
192.168.43.129  受控制的主机
....
ansible all -m ping 或者 ansible nodes -m ping来测试受控主机192.168.43.129是否可以ping通
ansible 参数：
-m MODULE_NAME, --module-name=MODULE_NAME 要执行的模块，默认为command模块

-b，--become：特权方式运行命令

-a MODULE_ARGS, --args=MODULE_ARGS 模块的命令参数

-u REMOTE_USER, --user=REMOTE_USER ssh 连接的用户名，默认用root，ansible.cfg 中可以配置

-k, --ask-pass 提示输入ssh 登录密码，当使用密码验证登录的时候用

-s, --sudo sudo 运行

-U SUDO_USER, --sudo-user=SUDO_USER sudo 到哪个用户，默认为root

-K, --ask-sudo-pass 提示输入sudo 密码，当不是NOPASSWD 模式时使用

-B SECONDS, --background=SECONDS run asynchronously, failing after X seconds(default=N/A)

-P POLL_INTERVAL, --poll=POLL_INTERVAL set the poll interval if using

-B (default=15)

-C, --check 只是测试一下会改变什么内容，不会真正去执行

-c CONNECTION 连接类型(default=smart)

-f FORKS, --forks=FORKS fork 多少个进程并发处理，默认5

-i INVENTORY, --inventory-file=INVENTORY 指定hosts 文件路径，默认default=/etc/ansible/hosts

-l SUBSET, --limit=SUBSET 指定一个pattern，对<host_pattern>已经匹配的主机中再过滤一次

--list-hosts 只打印有哪些主机会执行这个playbook 文件，不是实际执行该playboo

-M MODULE_PATH, --module-path=MODULE_PATH 要执行的模块的路径，默认为/usr/share/ansible/

-o, --one-line 压缩输出，摘要输出

--private-key=PRIVATE_KEY_FILE 私钥路径

-T TIMEOUT, --timeout=TIMEOUT ssh 连接超时时间，默认10 秒

-t TREE, --tree=TREE 日志输出到该目录，日志文件名会以主机名命名

-v, --verbose verbose mode (-vvv for more, -vvvv to enable connection debugging)
使用ansible只能执行一个任务，如果需要批量执行多个任务使用ansible-playbook,并且playbook具体的执行命令放在配置文件中的，例如创建一个用户:
vim /etc/ansible/create_user.yml  create_user.yml就是ansible-playbook的配置文件

---

- name: create_user  任务名称

 hosts: nodes   运行这个任务的主机,这里用的是hosts清单中的分组

 user: sshuser   运行这个任务使用的账户

 gather_facts: false  gather_facts参数制定了在以下任务执行前，是否先执行setup模块获取相关信息，这在后面的task或使用到setup获取的信息时用到

 vars:  vars参数制定了变量，这里指一个user变量，其值为test，需要注意的是，变量值一定要引号括起来

   - user: "test"

 tasks:  #任务

   - name: create user  任务名称

     user: name="{{ user }}"  user代表使用的模块，这里使用了{{user}}变量，代表创建的这个用户名是上面的test

vim /etc/ansible/test.yml

---

- hosts: nodes  清单中的分组

 remote_user: sshuser  远程执行的账户

 tasks:

   - name: test_playbook

     shell: touch /tmp/test.txt  给远程机器上创建一个test.txt空文件，这里使用的模块是shell
配置文件做好以后执行ansible-playbook   /etc/ansible/test.yml或者ansible-playbook   /etc/ansible/create_user.yml
如果想要自定义host清单，可以使用ansible-playbook -i 指定自定义清单文件 /etc/ansible/test.yml,或者自动获取清单文件，例如inventory脚本，
inventory脚本根据hostlist.txt文件自动生成清单，然后通过-i来操作这个清单，具体的执行命令：ansible-playbook -i inventory.py test.yml

'''