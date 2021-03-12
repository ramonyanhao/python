import os, sys

# 打开文件
fd = os.open("foo.txt", os.O_RDWR | os.O_CREAT)

# 复制文件描述符
d_fd = os.dup(fd)

# 使用复制的文件描述符写入文件
os.write(d_fd,bytes("This is test",'utf-8'))#os.write是根据文件描述符来给这个文件写入内容，write是直接给文件对象写入内容
#这里返回的是一个以utf-8编码格式的bytes的对象，这个bytes相当于encode


# 关闭文件
os.closerange(fd, d_fd)

print("关闭所有文件成功!!")

# 打开一个文件
f = open('foo.txt', 'a')#a代表往foo.txt后面追加内容

# 将这个文件描述符代表的文件，传递给 1 描述符指向的文件（也就是 stdout）
os.dup2(f.fileno(), 1)#fileno()表示返回当前打开的文件描述符，0代表标准输入，1代表标准输出，2代表错误标准输出，3以后的数字都是新建文件自定义的文件描述符

# 关闭文件
f.close()

# print 输出到标准输出流，就是文件描述符1
print('runoob')
print('google')
#执行以上程序输出结果为, 生成一个foo.txt文件,内容为刚才print输出的内容