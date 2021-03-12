def meisen(n):#梅森质数，2**p-1结果为梅森质数  p为质数
    n += 1
    while True:
        k = n % 2
        n = n // 2
        if k != 0:
            return False
        if n == 1:
            break
    return True

def sushu():
    n = 1
    while True:
        if n == 1 or n == 2 or n == 3:
            yield n
        else:
            m = n//2
            flag = False
            for i in range(2,m+1):
                if n % i == 0:
                    flag = True
            if not flag:
                yield n
        n += 1

import time
begin_time = time.time()
for i in sushu():
    if i > 10000:      #改 i >的值可以增加求取范围
        break
    if meisen(i):
        print(i)
        end_time = time.time()
        print(end_time-begin_time)
        begin_time = end_time