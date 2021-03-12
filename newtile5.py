# 获取列表的第二个元素
def takeSecond(elem):
    return elem[1]
#elem这个参数名是随便起的，elem后面的[0]代表random列表排序按照每组的第一个数字排序，例如：（2，2），（3，4），（4，1），（1，3）
#按照每组第一个数字排序：(1,3)的第一个数字为1排在列表第一位，然后（2，2）第一个数字2排在列表第二位，依次往后排

# 列表
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# 指定第二个元素排序
random.sort(key=takeSecond)
#这里很重要，sort的key参数指定后列表按照key指定的元素进行排序,这里的key=takesecond代表key=1,就是列表按照每组的第二个元素排序，如果是0按照第一个元素排序

# 输出类别
print ('排序列表：', random)

random.sort(key=lambda x:x[0])#代表key这个参数按照lambda匿名参数x的第一个数字排序
print (1,(random))

random.sort(key=lambda x:x[0]!=2)#代表key这个参数按照lambda匿名参数x的第一个数字是否不等于2，如果不等于2返回true
print (2,(random))

random.sort(key=lambda x:x[0]==2)#代表key这个参数按照lambda匿名参数x的第一个数字等于2,等于2返回false
print (3,(random))

random.sort(key=lambda x:x[0]is 2)#代表key这个参数按照lambda匿名参数x的第一个数字引用的是同一个对象则返回 True，否则返回 False
print (4,(random))

random.sort(key=lambda x:x[0]is not 2)#代表key这个参数按照lambda匿名参数x的第一个数字引用的不是同一个对象则返回结果 True，否则返回 False
print (5,(random))