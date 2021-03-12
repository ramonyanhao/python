import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "ramonyanhao"  # 用户名
mail_pass = "manageMENT1"  # 邮箱登陆密码manageMENT!1,由于163邮箱启用第三方登录smtp服务器授权码，授权码为manageMENT1

sender = 'ramonyanhao@163.com'
receivers = ['ramonyanhao@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">这是一个链接</a></p>
"""
message = MIMEText(mail_msg, 'html', 'utf-8')#text发送过去的邮件正文为附件形式，后缀名是.bin,使用plain发送过去的邮件正文可以直接显示,这里使用html方式
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] = Header("测试", 'utf-8')
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())#发送邮件，sender为发送的邮箱地址，receivers为接受的邮箱地址，这里使用列表形式可以发送到多个邮箱，用逗号隔开
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print("Error: 无法发送邮件",e)