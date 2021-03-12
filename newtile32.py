import os,sys
#open()参数打开一个文件返回一个文件对象，就是文件的内存地址
#os.open()打开一个文件返回一个文件描述符，就是0，1，2，3
#os.fdopen()通过文件描述符返回一个文件对象，这种方法可以把os.open打开的文件可以使用tell(),seek()等
#os.write,os.read,os.open都是从文件描述符写入或者读取内容，这些内容都是以二进制暂存在内存中
#os.stat和os.lstat是一样的，都是用来查看文件信息，当前连接用户数，文件最大字节，文件用户ID,组ID等等,这两个都是用文件路径查看，os.fstat是用文件描述符查看
#os.fsync() 方法强制将文件描述符为fd的文件写入硬盘，首先f.flush(),然后os.fsync(f.fileno())
#os.getcwdu返回一个当前工作目录的Unicode对象，如果在当前目录创建中文名称的文件，用getcwd会出现乱码，改用getcwdu
'''u = os.getcwd()
u+= u'\测试2'
os.mkdir(u)'''#创建文件夹不会有乱码
#os.chown,chmod,lchown,lchmod都是指定路径文件修改权限，需要先关闭打开的文件对象，而fchown,fchmod是通过文件描述符修改文件权限，不用关闭打开的文件对象
#os.link创建硬链接,创建一个已存在文件的拷贝,两个参数，第一个是存在的文件，第二个是不存在的目标文件
#os.lseek和seek用法一样，只不过lseek是通过文件描述符
#os.closerange可以关闭所有文件描述符
#os.mkdir只创建一层目录，如果上级目录不存在则返回错误，os.makedirs递归创建目录，可以把路径中不存在的目录自动创建，makedirs可以使用./相对路径在当前目录下创建子目录
#os.removedirs和os.rmdir都是删除目录，前者为按照指定路径递归删除目录，后者只删除指定目录,removedirs也可以使用./相对路径删除当前目录下的子目录
#os.path.splitext()将文件名和扩展名分开，os.path.join()把文件名和路径合成一个整体，os.path.split（）把文件名和路径分隔成两部分，一部分是文件名，一部分是路径
#os.rename只能给一个文件或文件夹改名，os.renames可以递归方式给文件或文件夹改名，rename和renames可以把一个文件或文件夹通过改名到另一个路径下，这个路径下所有不存在的文件夹自动创建，原文件里的内容不变
'''import os
import os.path
批量修改文件后缀名：.blv改为.flv
ext_from = '.blv'
ext_to = '.flv'

read_file_dir = input(r'请输入要修改文件扩展名的路径：')

files = os.listdir(read_file_dir) # 列出当前目录下所有的文件

for filename in files:
    portion = os.path.splitext(filename) # 分离文件名字和后缀

    if portion[1] ==ext_from:  #检测扩展名
        newname = portion[0]+ext_to  #改新的新扩展名
        os.chdir(read_file_dir)  
        os.rename(filename,newname)
        print(os.path.basename(filename)+' -> '+ os.path.basename(newname))'''
#os.symlink()用于创建一个软链接,os.path.islink(path) 来判断一个path是不是一个软连接，如果是的话再用os.readlink(path)获取该连接所指向的真实路径
#os.popen和os.system一样，都是在参数中输入windows命令来执行，但是popen返回一个文件描述符号打开的文件对象，所以需要在popen后面加.read()或者.readlines()
#os.unlink方法用于删除指定文件路径链接
#os.walk输出一个三元组【文件夹路径, 文件夹名字, 文件名】，walk没有返回值，所以需要用for循环输出，最终目的是输出当前目录下'.'所有文件和文件夹列表
# topdown为True表示优先输出当前目录'.'下的文件夹名和文件名，如果topdown为False表示优先输出当前目录'.'下的子文件夹里的文件夹名和文件名，当前目录'.'下的文件夹和文件最后输出
for root, dirs, files in os.walk(".", topdown=False):#三个参数root代表路径，dirs代表文件夹名字，files代表文件名，topdown=False表示文件夹下面的子文件夹的路径，文件夹名称，文件名称优先输出
    for name in files:#再遍历文件名，如果name参数在这个文件名列表中
        print(os.path.join(root, name))#输出完整的文件路径+文件名称
    for name in dirs:#遍历文件夹名称，如果name参数在这个文件夹名称列表中
        print(os.path.join(root, name))#输出完整的文件夹路径+文件夹名称
#os.path.abspath(path)	返回绝对路径
#os.path.exists(path)	路径存在则返回True,路径损坏返回False.判断文件或文件夹是否存在
#os.path.isfile(path)	判断路径是否为文件
#os.path.isdir(path)	判断路径是否为目录
#os.path.join(path1[, path2[, ...]])	把目录和文件名合成一个路径
#os.path.relpath(path[, start])	从start开始计算相对路径，例如可以这样os.path.relpath('foo.txt','../'),返回foo.txt+上一级目录的相对路径
print(os.path.relpath('foo.txt','../'))
#os.path.split(path)	把路径分割成文件夹名和文件名，返回一个元组
#os.path.splitext(path)	分割路径，返回路径名和文件扩展名的元组
#os.getcwd()与os.curdir都是用于获取当前工作路径，但是os.curdir返回的是'.'，代表当前目录，可以使用os.path.abspath(os.curdir)效果与os.getcwd()一样
#os.sep根据你所处的平台，无论是windows还是linux,自动采用相应的分隔符号,如果是windows自动采用\,如果是linux自动采用/
#os.linesep字符串给出当前平台使用的行终止符。例如，Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'
#os.getcwd() + os.sep + filename + os.linesep表示os.getcwd()当前路径+os.set根据系统平台自动给出分隔符号+filename文件名+os.linesep根据系统平台自动给出行终止符
#os.pardir和os.curdir意思差不多，os.curdir返回的是'.',os.pardir返回的是'..'就是返回上一级目录，例如：os.chdir(os.pardir)将当前工作目录返回到上一级目录