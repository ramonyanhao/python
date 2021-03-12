def swaplist(len,arr,n):
    if n > (len//2):
        print('无法翻转！')
    else:
        arr[:n],arr[-n:] = arr[-n:],arr[:n]#这里注意列表索引[:n]和[n]的区别，[:n]代表列表的一段，就是0到n,[n]只代表列表的一个元素，位置是索引n
        print('翻转后的列表：',arr)#如果指定列表中的两个元素互相对调，这里的索引就需要使用[n]了

a=int(input('请输入数列的长度：'))
b=list(range(1,a+1))
c=int(input('请输入头尾对调的数目：'))
print('翻转前的列表：',b)
swaplist(a,b,c)


def swapPositions(list, pos1, pos2):
    first_ele = list.pop(pos1)#注意列表先取出一个元素后，列表中只有3个元素
    print(list)
    second_ele = list.pop(pos2-1)#注意这里列表list是[65,19,90],如果像取出19，需要pos2-2=1,因为列表只有三个元素，所以这里减1，再运用这个函数时再减1
    print(list)
    print(second_ele,first_ele)
    list.insert(pos1, second_ele)
    list.insert(pos2, first_ele)

    return list


List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions(List, pos1 - 1, pos2 - 1))

