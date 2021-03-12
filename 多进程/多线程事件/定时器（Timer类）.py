# 定时器，指定n秒后执行某操作
from threading import Timer


def hello():
    print("hello, world")


t = Timer(1, hello) # 1秒后输出hello,world
t.start()