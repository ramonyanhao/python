import ctypes
# 一般我们通过id(变量)获取变量所在的内存地址，ctypes可以通过内存地址获取存储的变量
def va():
    k=10
    return k
print(id(va))
a=va()
print(id(a))
memory_address=ctypes.cast(id(va),ctypes.py_object).value
address=ctypes.cast(id(a),ctypes.py_object).value
print(memory_address,address) # memory_address是函数va的内存地址，address是函数va()运行后的内存地址
# 检查对象的内存使用
import sys
num=21
print(sys.getsizeof(num)) # 共使用了28个字节

from collections import Counter
# 把一个带有重复元素的列表转化为字典，字典的值为列表中重复元素的个数，键就是列表中的元素
l=['a','a','a',1,1,1,'b','b','c',33]
cou=Counter(l)
print(cou)

#合并两个字典
dic1={'a':1,'b':2}
dic2={'a':3,4:'a'} # 如果两个字典包含重复的键，则输出后面字典中的键值
dic3={**dic1,**dic2}
print(dic3)

import secrets # 给列表中的元素做随机加密取样
secure_random=secrets.SystemRandom() # 创建一个随机加密对象
print(secure_random.sample(l,2)) # 从l列表中随机取出2个元素并加密

for i in set(l): # l列表转化为集合，计算l列表中重复元素的个数
    print(i,':',l.count(i),end='\t')
# 集合是不重复的无序元素组成,可以利用集合的不重复属性来检查列表元素的唯一性
def uniqe(l):
    if len(l) == len(set(l)): # 通过判断l列表的长度是否和转换为集合的l列表长度一样得出列表元素的唯一性
        print('列表中没有重复元素')
    else:
        print('列表中包含重复元素')
uniqe(l)