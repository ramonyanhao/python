sum = list(range(1,31))
while len(sum) > 15:
    print('{}号下船了'.format(sum.pop(8)))#先把第一个9去掉，pop(8)就是删除sum列表索引为8的值，然后执行for循环
    # 循环后sum列表第一个值就是刚删除的索引为8的值，因为刚才已经删除了，程序执行到这里再次删除sum列表索引为8的值，基于刚才sum列表继续往后推8个数
    for i in range(8):
        sum.append(sum.pop(0))#循环8个数，把sum列表第一个移动到列表最后一个，以此类推
print('*'*50)
sum = list(range(1,31))#和上面的方法一样，就是最后用的不是for循环
while len(sum) > 15:
    print('{}号下船了'.format(sum.pop(8)))
    sum +=sum[0:8]#这里把列表前8个数添加到列表最后
    del sum[0:8]#然后删除列表前8个数
print('*'*50)
#其实也可以这样写
sum = list(range(1,31))
while len(sum) > 15:
    for i in range(8):#可以先取出列表8个数添加到最后
        sum.append(sum.pop(0))
    print('{}号下船了'.format(sum.pop(0)))#然后删除列表第一个数，这样比上面的方法更容易理解
print('*'*50)
sum = list(range(1,31))
while len(sum) > 15:
    sum +=sum[0:8]#先添加8个数到列表最后
    del sum[0:8]#再删除列表开头8个数
    print('{}号下船了'.format(sum.pop(0)))#然后打印出列表第一个数
print('*'*50)
s=list(range(1,31))
for i in s:
    if len(s)>15:
            print(s[8])
            s=s[9:]+s[:8]#把s列表改成从第10个数开始到列表最后一个数，然后在列表最后添加列表第一个数到列表第8个数，这样列表第9个数就会被删除