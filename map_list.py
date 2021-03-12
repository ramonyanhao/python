a = ['adam', 'LISA', 'barT']#把列表变成['Adam', 'Lisa', 'Bart']
def f():
    for i in a:
        a[a.index(i)]=i.lower().capitalize()#使用index返回i在a列表中的索引值
    return a#这里直接改变了a列表
print(f())
#也可以使用简单的map函数完成
a = ['adam', 'LISA', 'barT']
def x(a):
    return a.lower().capitalize()#这里不会改变a列表
print(list(map(x,a)))#map函数返回值是一个迭代器，所以使用list
#其他方法
a = ['adam', 'LISA', 'barT']
def l():
    for i in range(len(a)):
        a[i]=a[i].lower().capitalize()
    return a
print(l())
#尝试通过list.append(list.pop(0))方法把list列表最后一个元素删除，再添加进修改过的元素
a = ['adam', 'LISA', 'barT']
def p():
    for i in a:
        i = i.lower().capitalize()
        if len(a)<=5:#如果不加这个条件，a列表会变死循环，因为a.append(i)会给列表添加i元素，但是到for i in a时，发现新添加的元素就会再循环一次，这样就出现无限循环添加发现元素
            a.append(i)
    for x in range(3):#这里循环3次，每次删除列表第一个元素，剩下的就是需要的结果
        a.pop(0)
    return a
print(p())
#for i in list的坑大致原因就是remove a[0]之后,i 自动变成了 a[1], 但是 a已经变成了['LISA', 'barT'],所以i=a[1]就悲催的指向了barT,跳过了LISA
a = ['adam', 'LISA', 'barT']
for i in a[:]:#这里需要使用for i in a[:]:
    a.remove(i)
    i=i.lower().capitalize()
    a.append(i)
    print(a)
a = ['adam', 'LISA', 'barT']
b=a[:]#给a做浅拷贝，只要列表中没有二级元素，比如['adam', 'LISA',[1,2,3], 'barT'],使用b=copy.deepcopy(a)为深拷贝，不管有多少列表嵌套
for i in b:
    a.pop(0)
    i = i.lower().capitalize()
    a.append(i)
    print(a)
