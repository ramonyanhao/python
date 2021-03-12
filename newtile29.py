import os
import os.path
ls = []
#检索指定路径下后缀是 py 的所有文件
def getAppointFile(path,ls):
    fileList = os.listdir(path)#指定路径下列出所有的文件和目录，传入fileList变量
    try:
        for tmp in fileList:
            pathTmp = os.path.join(path,tmp)#参数中path是用户输入的需要查询的路径，tmp是遍历os.listdir返回的所有文件夹列表，他们拼接起来就是绝对路径
            #os.path.isdir()和os.path.isfile()需要传入的参数是绝对路径，但是os.listdir()返回的只是一个某个路径下的文件和列表的名称，不带路径
            #因此需要os.path.join()函数，将os.listdir()返回的名称拼接成文件或目录的绝对路径再传入os.path.isdir()和os.path.isfile().
            if True==os.path.isdir(pathTmp):#判断pathTmp是否为文件夹，os.path.isfile()用于判断某一对象(需提供绝对路径)是否为文件
                getAppointFile(pathTmp,ls)#这里表示如果pathTmp是文件夹，那给参数path加默认参数为pathTmp,下面调用getAppointFile函数时就可以不用指定具体参数
            elif pathTmp[pathTmp.rfind('.')+1:].upper()=='PY':#然后再进行查找后缀名为py的文件,upper()表示后缀名小写改为大写==PY,如果本身是大写就不会变动，这样不会报错
                ls.append(pathTmp)#把结果传入ls列表
    except PermissionError:
        pass

def main():
    while True:
        path = input('请输入路径:').strip()
        if os.path.isdir(path) == True:
            break

    getAppointFile(path,ls)
    print(ls)
    print(len(ls))

main()