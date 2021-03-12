def leijia(x,n=1):#尾递归
    if x==1:#出口，当x=1时返回n的值
        return n
    return leijia(x-1,x+n)#x=100,参数x-1一直减到x=0时返回n的值，通过x-1得出的x的值就是下一步x的值，然后x+n就是这一步n的值，可以理解为x+n相当于x加下一步x的值
print(leijia(100))

def leji(x):#递归函数
    if x==1:
        return 1
    return x+leji(x-1)#当x=1时返回1，这里返回x与下一步x的值相加，一直加到x=1时结束，x=100
print(leji(100))

def lj(x):#普通函数1加到100得多少
    return (x+1)*(x//2)#直接计算100+1再乘100的一半
print(lj(100))

print(sum(range(1,1001)))

import time
print('按下回车开始计时，按下 Ctrl + C 停止计时。')
while True:
    input("")  # 如果是 python 2.x 版本请使用 raw_input()
    starttime = time.time()
    print('开始')
    try:
        while True:
            print('计时: ', round(time.time() - starttime, 0), '秒', end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print('结束')
        endtime = time.time()
        print('总共的时间为:', round(endtime - starttime, 2), 'secs')
        break