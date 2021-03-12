'''
python线程的事件用于主线程控制其他线程的执行，事件是一个简单的线程同步对象，其主要提供以下几个方法：

clear	将flag设置为“False”
set	    将flag设置为“True”
is_set	判断是否设置了flag
wait	会一直监听flag，如果没有检测到flag就一直处于阻塞状态
事件处理的机制：全局定义了一个“Flag”，当flag值为“False”，那么event.wait()就会阻塞，当flag值为“True”，那么event.wait()便不再阻塞。
'''
#利用Event类模拟红绿灯
import threading
import time

event = threading.Event()


def lighter():
    count = 0
    event.set()     #初始值为绿灯
    while True:
        if 5 < count <=10 :
            event.clear()  # 如果count在5和10之间，则通过event.clear()设置flag为False
            print("\33[41;1mred light is on...\033[0m")
        elif count > 10:   # 如果count大于10则把count还原为0，重新开始计数
            count = 0
        else:  #  如果count在0和5之间则通过event.set()设置flag为True
            event.set()  # 绿灯，设置标志位
            print("\33[42;1mgreen light is on...\033[0m")

        time.sleep(1)
        count += 1

def car(name):
    while True:
        if event.is_set():      # 判断是否设置了标志位，如果设置了标志位，is_set为True
            print("[%s] running..."%name)  # 可以理解成当前是绿灯，汽车开始运行
            time.sleep(1)
        else:  #  否则flag为False
            print("[%s] sees red light,waiting..."%name)  # 可以理解成当前是红灯，等待
            event.wait()  # wait一直监听flag,知道flag变为True
            print("[%s] green light is on,start going..."%name) # 检测到flag变为True,可以理解成绿灯了，汽车开始运行

light = threading.Thread(target=lighter,)
light.start()

car = threading.Thread(target=car,args=("MINI",))
car.start()

