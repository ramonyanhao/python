ii=input('input num:')    #取值
iid=eval(ii)              #变数字
print(type(iid))
bnum_str='{:b}'.format(iid)    #二进制化（字符串）
bnum=eval(bnum_str)            #字符串转数字（留用）

str_putOut='num in b is:{:b}'.format(iid)    #输出准备

print(bnum,str_putOut)     #显示数字和准备的输出内容
#map函数是用来通过函数计算后面列表所有元素的值，注意map的返回值是计算后的列表
print(list(map(lambda x:x*x,[1,2,3])))
#filter函数是用来筛选列表中符合条件的元素，注意filter的返回值是符合条件的列表元素本身，不是运算过后的值
print(list(filter(lambda x:x%2==0,[1,2,3])))


def is_odd(n):
    return n % 2#n这里没有指定n%2==0,使用n%2计算出的值如果是0代表failse,如果是1代表true,failse的值不会输出，所以n%2代表n%2==1


tmplist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
newlist = list(tmplist)
print(newlist)