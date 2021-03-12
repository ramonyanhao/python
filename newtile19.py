import random
import sys
import time

result = []
while True:
    result.append(int(random.uniform(1,7)))
    result.append(int(random.uniform(1,7)))
    result.append(int(random.uniform(1,7)))
    print (result)
    count = 0
    index = 2
    pointStr = ""
    while index >= 0:
        currPoint = result[index]#result列表中三个乱数按照index索引取出一个，比如[4,5,6][index=2]取出6
        count += currPoint#算三个乱数的总数
        index -= 1#索引减1，然后取出result列表中第二个乱数，知道index<0时跳出循环，共取出0，1，2三个索引对应的数字
        pointStr += " "#这句话意思是在每个数字前加空格
        pointStr += str(currPoint)#把列表中的数字转为字符串然后输出
    if count <= 11:#如果count小于等于11结果就是小，否则大于11就为大
        sys.stdout.write(pointStr + " -> " + "小" + "\n")#sys.stdout.write相当于print,sys.stdout.write默认输出到控制台，可以修改sys.stdout.write=输出到某个文件
        time.sleep( 1 )   # 睡眠一秒
    else:
        sys.stdout.write(pointStr + " -> " + "大" + "\n")
        time.sleep( 1 )   # 睡眠一秒
    result = []#清空列表，进入下一轮循环