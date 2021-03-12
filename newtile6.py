list=[[1, 2, 3], [4, 5, 6],[7,8,9]]
for i in list:
    for j in i:
        print (j,end=' ')
print()#空行，可以起到换行的作用，不然结果会在一行输出
print (list[::-1])#倒叙排列，注意语法，[::-1]第一个:代表开始位置，第二个:代表结束为止，-1代表步数
print(list[:-1])#列表输出到倒数第二个元素
print(list)#前面的list[:]操作不会影响list本来的值，list[:]会创建一个副本来运行

list1=['你','我','它']
print(list1)

#清空列表中的多项空值：

test = ['a','','b','','c','','']
test = [i for i in test if i != '']#test列表做for循环，遍历a,空，b,空, c,空然后加条件如果i不等于空

print(test)

#寻找文件最长的行,(核心代码）

f = open('/etc/python_code','r')#以只读模式打开文件
longest = max(len(x.strip()) for x in f)#x.strip()删除x开头和结尾的空格，len再检测剩余的字符长度，然后max找出最大的字符串
f.close()