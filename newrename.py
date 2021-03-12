import os,sys
path=os.getcwd()
for i in os.listdir(path):
    f=i.split('.')
    if f[-1]=='py':
        newname='new'+i
        os.rename(i,newname)

