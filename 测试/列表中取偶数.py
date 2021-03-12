a = [1,2,3,4,5,6,7,8]
b = [2,3,4,5,6,7,8,9]
c = [3,4,5,6,7,8,9,10]
d = [5,6,7,8,9,10,11,12]
e=filter(lambda x:x%2==0,[x for x in a])#lambda只是一个公式算法，filter就是通过这个算法取出后面列表[x for x in a]符合这个算法条件的值
print(list(e))
f=[x for x in a if x %2==0]
print(f)
lst = [1,2,3,4,5,6,7,8]#对列表lst中的偶数位置的元素进行加3后求和
print(list(filter(lambda x:x%2==0,range(len(lst)))))#求出偶数索引位
result =sum(map(lambda x:lst[x]+3,filter(lambda x:x%2==0,range(len(lst)))))
print(result)#先计算最里面的filter(lambda x:x%2==0,range(len(lst))求出偶数索引位，然后map(lambda x:lst[x]+3,[0,2,4,6])把列表中所有的偶数位的元素都+3,最后sum求和
from itertools import product,combinations
print('combinations:',list(combinations(a+b+c+d,4)))#combinations是横向遍历列表，先遍历a列表中所有元素，4个一组，然后再往下遍历b列表所有元素例如：(1, 2, 3, 4), (1, 2, 3, 5), (1, 2, 3, 6)
#combinations也可以纵向遍历
for i in range(len(a)):#由于abcd4个列表中的元素一样多，所以这里可以提取出a列表的索引用到bcd三个列表中
    print(list(combinations([a[i]]+ [b[i]] + [c[i]] + [d[i]], 4)))#和product不同，遍历结果是纵向一排组成一个列表，例如[(1, 2, 3, 5)]，[(2, 3, 4, 6)]
print('product:',list(product(a,b,c,d)))#product是纵向遍历，就是把abcd4个列表中第一元素组合成一个列表，然后abc前三个元素加d的第2个元素组成一个列表，这就是笛卡尔积，又可以理解成
'''print([(x,y,z,o)for x in a for y in b for z in c for o in d])
for x in a:
    for o in b:
        for p in c:
            for q in d:
                print(x,o,p,q,end='')'''
#让列表元素组合成多个偶数集合,permutations和combinations类型一样，都是横向遍历，但是combinations只能顺时针遍历，而permutations不仅顺时针，还要逆时针遍历例如
'''
list(itertools.combinations('abc', 2))
#只顺时针遍历，结果：[('a', 'b'), ('a', 'c'), ('b', 'c')]
list(itertools.permutations('abc',2))
#顺时针加逆时针遍历，结果：[('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a')('c', 'b')]
'''
#找出a列表中所有可能的偶数组合
def oushu(ll):
    from itertools import permutations
    li=[]
    for k in range(len(ll)):
        for i in permutations(ll,k):#通过permutations列出a列表中所有可以组成不同数字的组合，k是permutations的参数，表示一个组合中有多少个元素，通过上面的遍历引入这个参数k
            i="".join(map(str,i))#把每个组合都变为一串数字，因为permutations返回的都是元组，例如(1,2,3,4,5,6,7,8),但是元组里面都是整数，通过map(str,i)把里面的整数变为字符串
            # 然后就可以通过join函数把这些字符串连接起来，因为join前面使用的空字符，可以达到把这些连接起来的字符串变成一整串数字,例如12345678,注意这串数字类型还是str
            if i == '':# 因为"".join把i转为整串数字后，开头第一个是空字符，例如：通过"".join转换的结果是'','1','2','3','4','5','6','7','8','12,'13'等等
                continue#所以这里要把第一个空字符去掉，遇到空字符直接跳过
            if int(i) % 2 == 0:#再把这些整串的字符串转为整数，如果遇到偶数则添加进li列表
                li.append(i)
    return li
print(oushu(a))