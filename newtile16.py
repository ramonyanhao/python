# 打开文件
fo = open("runoob.txt", "w+")#open()返回的是文件的对象，就是文件占用内存的地址然后复制给变量fo
print ("文件名为: ", fo.name)

f1=fo.write('this is test')#write写入文件对象，比如这个fo.write,如果是os.write是给文件描述符写入内容
print(f1)

fid = fo.fileno()#返回文件对象以后才可以使用fileno()查看这个对象的文件描述符是多少，如果使用os.open则直接返回文件描述符不是文件对象，所以注意如果用os.open的话这里就不可以使用fileno()
print ("文件描述符为: ", fid)

# 关闭文件
fo.close()#这里也是如果使用os.open()也不可以使用close()来关闭这个文件描述符，如果要关闭可以使用os.close(文件描述符)

import os, sys

# 打开文件
fd = os.open("runoob.txt", os.O_RDWR | os.O_CREAT)

# 复制文件描述符
d_fd = os.dup(fd)
print(d_fd)
print(fd)

# 使用复制的文件描述符写入文件
f2=os.write(d_fd, "This is test".encode())#注意这里d_fd返回的是文件描述符不是文件对象，所以需要用os.write给文件描述符对应的文件写入内容
# 使用encode()把字符串this is test以指定的编码格式编码为bytes对象，使用decode()把字符串以指定的编码格式解码为bytes对象，默认为utf-8
print(f2)
# 关闭文件
os.closerange(fd, d_fd)

print("关闭所有文件成功!!")
print('test'.encode('utf-8'))

