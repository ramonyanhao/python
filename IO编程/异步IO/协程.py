def consumer():
    r = ''
    while True:
        n = yield r  # 这里看成两步，第一步先返回当前r的值并且暂停，当程序再次执行到这里激活yield后执行第二步，给n变量赋值yield r的返回值
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)  # 在一个生成器函数未启动之前，是不能传递值进去。也就是说在使用c.send(n)之前，必须先使用c.send(None)或者next(c)来返回生成器的第一个值。
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        '''
        consumer函数是一个generator，把一个consumer传入produce后：

首先调用c.send(None)启动生成器；

然后，一旦生产了东西，通过c.send(n)切换到consumer执行；

consumer通过yield拿到消息，处理，又通过yield把结果传回；

produce拿到consumer处理的结果，继续生产下一条消息；

produce决定不生产了，通过c.close()关闭consumer，整个过程结束。
        '''
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)
'''
第一步：执行 c.send(None)，启动生成器返回第一个值，n = yield r，此时 r 为空，n 还未赋值，然后生成器暂停，等待下一次启动。

第二步：生成器返回空值后进入暂停，produce(c) 接着往下运行，进入While循环，此时 n 为1，所以打印：

[PRODUCER] Producing 1...
第三步：produce(c) 往下运行到 r = c.send(1)，再次启动生成器，并传入了参数1，而生成器从上次n的赋值语句开始执行，n 被赋值为1，n存在，if 语句不执行，然后打印：

[CONSUMER] Consuming 1...
接着r被赋值为'200 OK'，然后又进入循环，再次执行到n = yield r时，返回生成器的第二个值，'200 OK'，然后生成器进入暂停，等待下一次启动。

第四步：生成器返回'200 OK'进入暂停后，produce(c)往下运行，进入r的赋值语句，r被赋值为'200 OK'，接着往下运行，打印：

[PRODUCER] Consumer return: 200 OK
以此类推...

当n为5跳出循环后，使用c.close() 结束生成器的生命周期，然后程序运行结束。
'''