import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart#这个模块功能是可以让邮件以附件形式发送
from email.header import Header
#邮件带附件形式发送
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "ramonyanhao"  # 用户名
mail_pass = "manageMENT1"  # 邮箱登陆密码manageMENT!1,由于163邮箱启用第三方登录smtp服务器授权码，授权码为manageMENT1

sender = 'ramonyanhao@163.com'
receivers = ['ramonyanhao@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] = Header("测试", 'utf-8')
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

# 邮件正文内容
message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))

# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="test.txt"'
message.attach(att1)

# 构造附件2，传送当前目录下的 runoob.txt 文件
att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
message.attach(att2)

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功",message.as_string())
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
