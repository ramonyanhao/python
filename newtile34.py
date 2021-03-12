import os
#显示所有视频格式文件，mp4，avi，rmvb

def search_file(start_dir, target):
    os.chdir(start_dir)
#这个函数特点是在当前工作目录下进行的，后面代码执行后要注意时刻更改当前工作目录
    for each_file in os.listdir(os.curdir):
        ext = os.path.splitext(each_file)[1]
        if ext in target:
#os.sep根据你所处的平台，无论是windows还是linux,自动采用相应的分隔符号,如果是windows自动采用\,如果是linux自动采用/
#os.linesep字符串给出当前平台使用的行终止符。例如，Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'
#os.getcwd() + os.sep + filename + os.linesep表示os.getcwd()当前路径+os.set根据系统平台自动给出分隔符号+filename文件名+os.linesep根据系统平台自动给出行终止符
            vedio_list.append(os.getcwd() + os.sep + each_file + os.linesep)#结果就是完整路径+文件名+行终止符
        if os.path.isdir(each_file):
            search_file(each_file, target)  # 递归调用
            os.chdir(os.pardir)  # 递归调用后切记更改当前工作目录返回上一层目录
#os.pardir和os.curdir意思差不多，os.curdir返回的是'.',os.pardir返回的是'..'就是返回上一级目录，例如：os.chdir(os.pardir)将当前工作目录返回到上一级目录
#os.getcwd()与os.curdir都是用于获取当前工作路径，但是os.curdir返回的是'.'，代表当前目录，可以使用os.path.abspath(os.curdir)效果与os.getcwd()一样
start_dir = input('请输入待查找的初始目录：')
program_dir = os.getcwd()

target = ['.mp4', '.avi', '.rmvb']
vedio_list = []

search_file(start_dir, target)

f = open(program_dir + os.sep + 'vedioList.txt', 'w')
f.writelines(vedio_list)
f.close()