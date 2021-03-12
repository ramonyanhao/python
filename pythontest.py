f='''basedir=__file__
print(basedir)
'''
with open('d:/ramon.py','w+') as a:
    a.write(f)
import os
p=os.system('python d:/ramon.py')
print(p)


import os#通过二进制方式拷贝文件到当前脚本目录下
a='D:\\haozip_v5.9.8.exe'#指定拷贝的源文件
b=os.path.basename(a)#拷贝到当前目录下，b为拷贝过来的a的文件名
open(b,'wb').write(open(a,'rb').read())#如果不要拷贝到当前目录下可以再这里指定目录，open('路径'+b+'wb')
#这句话意义：使用wb方式打开b，然后写入以rb方式读取a的内容，达到拷贝文件的目的，而且以这种方式拷贝txt文件还可以保持源文件的格式
#在cmd中可以使用python -c "python的命令行"这种方式直接在cmd中运行python语句，python -c后面的双引号一定要加上，否则指定到python语句时遇到空格会报EOL结束符错误
#如果遇到文件中有换行，比如文件foo.txt内容如下：
'''
我热爱祖国
热爱人民
爱编程
爱生活
'''
#如果通过open('foo.txt','r').read()这种方式打开，结果是:'我热爱祖国\n热爱人民\n爱编程\n爱生活'
#这时需要print(open('foo.txt','r').read())可以自动识别换行符\n
