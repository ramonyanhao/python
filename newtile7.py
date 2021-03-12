import time
date = input("输入时间（格式如：2017-04-04）:")
t = time.strptime(date,"%Y-%m-%d")
print(t)
print('今年的第'+(time.strftime("%j",t))+'天')

