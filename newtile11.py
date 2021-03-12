# 打开文件
fo = open("runoob.txt", "w+")
fo.write('这是第一行\n这是第二行\n这是第三行\n这是第四行\n这是第五行\n')
print ("文件名为: ", fo.name)
fo.seek(0)
for index in range(5):
    line = fo.readline()#在python3x版本readline()代替了next(),如果使用readlines()将返回一个列表，包含了文件所有内容
    print ("第 %d 行 - %s" % (index, line))

# 关闭文件
fo.close()


with open("runoob.txt", "r") as f:
    data = f.readlines()
    print(data)
    a = data[0]
    b = data[1]
    c = data[2]
    d = data[3]
    e = data[4]
    print(a, b,c,d,e)#按照列表索引输出结果没有换行符



fo = open("runoob.txt", "r+")
fo.seek(0)
for foo in fo.readlines():
    foo=foo.rstrip('\n')
    print('内容： %s'%(foo))#如果使用%s或者%d来输出字符串，注意语法不使用逗号，如果使用普通字符串加变量输出，那普通字符串和变量中间加逗号隔开
fo.close()