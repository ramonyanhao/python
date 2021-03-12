#反转列表时注意变量尽量不要用python内置函数，如变量不要用list,使用后python内置函数list丢失
ll=[1,2,3,4,5]
ll.reverse()#再交互界面可以使用，但是reverse函数没有返回值，所以不可以赋值给变量，使用后直接倒序列表
print(ll)
a=reversed(ll)#reversed拥有返回值，可以赋值给变量，但是reversed返回值是一个迭代器，可以使用for循环打印出结果，也可以直接使用a=list(reversed(ll))
for i in a:
    print(i,end=' ')
#列表可以使用index(a)找出a在列表的哪个位置，例如ll.index(5)，返回索引4,可以利用这种方法把字典的值改为列表然后根据index(字典值)找出字典的键
dic={1:2,3:4,5:6,7:8,9:0}
d=list(dic.keys())[list(dic.values()).index(0)]#这里注意前面把dic的键变为列表，后面把dic的值变为列表，然后根据列表的index找出值为0的索引，键列表引用返回的索引找出这个键，[]里面的内容整体可以看成一个列表索引
print(d)#最终打印出结果值是0键是9
new_dict={v:k for k,v in dic.items()}#这里创建一个新字典，把字典的键改为值，把值改为键，如果查找原字典的值，现在直接查找新字典的键
print(new_dict)
#列表复制时如果直接使用列表变量=另一个变量(a=b)虽然两个列表内容一样，但是不是复制，是引用了相同的内存地址，如果更改其中一个列表内容，另一个也会更改,这种情况在脚本中注意
#列表复制一般使用a=list(b),或者a=b[:],又或者a=[],a.extend(b)
#注意在列表中如果索引使用[-3:-1]这种方式，-1不代表列表最后一个元素，只能使用[-1]这种方式索引才是列表最后一个元素
#如果在列表中想要计算列表所有元素的和或者乘积，需要先创建一个变量y=0，然后for x in 列表:y=y+x
#在循环中，如果遇到列表每次循环删除一个元素，如pop，那在循环中使用列表索引要先减1，因为循环下来的列表元素数量肯定比之前的少一个
test_str = "Runoob"

# 输出原始字符串
print("原始字符串为 : " + test_str)

# 移除第三个字符 n
new_str = ""

for i in range(0, len(test_str)):
    if i == 2:
        test_str=test_str[:i]+test_str[i+1:]
#test_str=test_str.replace(test_str[2],'',1)
#if 'n' in test_str:
    #print('Ruoob')
print("字符串移除后为 : " + test_str)