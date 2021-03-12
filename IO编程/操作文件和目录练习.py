# 1.利用os模块编写一个能实现dir -l输出的程序。
import time
import os


def dir_l(real_path):
    os.chdir(real_path)  # 把当前工作目录转到目标路径下，如果没有这句会报错找不到文件
    for i in os.listdir(real_path):
        file_time = time.strftime('%Y/%m/%d %H:%M', time.localtime(os.path.getctime(i)))
        file_type = ''
        if os.path.isfile(i):
            file_type = '<FILE>'
            with open(i, 'rb') as f:
                print('%dM' % (f.seek(0, 2)/1024/1024))
        elif os.path.isdir(i):
            file_type = '<DIR>'
        file_size = os.path.getsize(i)/1024
        print(file_time, file_type, '%.2fK'%(file_size), i, end='\t\n')
dir_l('d:\\')


# 2.编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
def search(a, b):
    for file in os.listdir(a):
        try:
            if os.path.isfile(a + '\\' + file):
                if b in file:
                    print(file, '=>', a + '\\' + file)
            else:
                search(a + '\\' + file, b)
        except PermissionError:
            pass
search('d:','ApacheMonitor')
'''如果想要在python的IDE中查看某个文件的内容有三种方法：
1.os.system('type D:\python\IO编程\StringIO和BytesIO.py')  os.system虽然可以打印出文件内容，但是它的返回值并不是文件内容，它的返回值是0或者1，执行成功返回0，出现错误返回1
所以如果在其他程序中想要调用os.system获取内容只能获取到0或者1这个返回值，内容则不会返回
2.os.popen('type D:\python\IO编程\StringIO和BytesIO.py').readlines() 因为popen返回的是一个文件读取的对象，所以需要通过readlines()或者read()把内容打印出来
3.subprocess'''
import subprocess,os,inspect,newtile10
os.system('type D:\python\IO编程\StringIO和BytesIO.py')
print(os.popen("ipconfig").read())
status, result = subprocess.getstatusoutput('ipconfig')  # 由于os.system只返回状态码，os.popen只返回结果，subprocess既返回执行后的状态码也返回执行结果
print(status, result)
'''subprocess.getoutput('pwd')返回执行结果
   subprocess.call("ipconfig")执行命令，返回状态码(命令正常执行返回0，报错则返回1)
   subprocess.check_output('ipconfig')执行命令，如果执行成功则返回执行结果，否则抛异常
   subprocess.Popen用于执行复杂的系统命令,例如:
   obj = subprocess.Popen("mkdir t3", shell=True, cwd='./')     #在cwd目录下执行命令创建t3子目录
'''
print(inspect.getsource(newtile10.Person))  # 重点:inspect.getsource查看函数源代码





