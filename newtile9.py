def reverse(li):
    for i in range(0, len(li)//2):#i in range (0,len(li)//2代表5//2=2）相当于i in range(0,2)
        temp = li[i]#temp=li[i]看成temp=[1,2,3,4,5][0,1]，temp=[1,2]
        li[i] = li[-i-1]#li[i]=li[-i-1]看成[1,2,3,4,5][0,1]也就是列表的1和2 = [1,2,3,4,5][0-1]或者[-1-1],等于[1,2,3,4,5][-1]或者[-2]也就是列表的5和4.
        # 直接看成[1,2,3,4,5][0]就是1,等于[1,2,3,4,5][-1]就是5，所以li[i]=[1,2];li[-i-1]=[5,4],列表1就变成5，2变成4
        li[-i-1] = temp#前面temp=[1,2],li[-i-1]=temp看成[1,2,3,4,5][-0-1][-1-1]=[1,2],再往下运算列表[1,2,3,4,5][-1][-2]=[1,2],代表列表里的5改成1，4改成2
        #再加上前面的运算列表[1,2,3,4,5]顺序就反过来了


l = [1, 2, 3, 4, 5]
reverse(l)
print(l)

print('-----')
def reverse(li):
    for i in range(len(li)//2):
        li[i], li[-i - 1] = li[-i - 1], li[i]#这里简化了上面的写法，li[i]看成[1,2],li[-i-1]看成[5,4],所以这里直接看成[1,2],[5,4]=[5,4],[1,2]
l = [1, 2, 3, 4, 5]
reverse(l)
print(l)

print('------')
def reverse(ListInput):
    RevList=[]
    for i in range (len(ListInput)):
        RevList.append(ListInput.pop())#pop取列表最后一位值返回，然后添加到RevList空列表中
    return RevList
f=reverse([1,2,3,4,5,6,7,8,9,0])
print(f)