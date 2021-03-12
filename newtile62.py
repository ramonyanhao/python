people = [i for i in range(1, 31)]
j = 0
while len(people) > 15:
    die = []#跳出for循环后die清空列表，如果把die放在while外面，die列表会不停更新，如果die列表没清空,for p in die更新过的p值
    for i in people:#注意这里的条件指定i在30以内，如果超过30跳出for循环,继续查看len(people)是否大于15个，如果符合条件继续下一轮for循环
        print(i,end='\t')
        j += 1
        if j % 9 == 0: #这里是重点，把if看成是当前循环的一个子环境，当j%9=0时，i当前循环的值就是j
            print(i,j,'离开')
            die.append(i)#不可以直接再people中做更改，因为当people.remove(i)时，列表会减少一个元素，这就影响了i的取值
            print(die)
    for p in die:#解决方法就是再创建一个列表，把需要去掉的元素都加入这个列表中然后统一删除
        people.remove(p)
    #[people.remove(p) for p in die]
print(people)



people={}#people字典中所有键的值默认为1，然后通过check检查把对应的键值改为0
for x in range(1,31):
    people[x]=1#people字典中设置x键的值为1，得出的结果是字典一共30个键，值都是1{1：1，2：1，3：1...}
# print(people)
check=0#检查数到9的人
i=1#总人数
j=0#最后剩余人数
while i<=31:
    if i == 31:
        i=1#当i加到31时，进行下一轮，i又从1开始
    elif j == 15:
        break
    else:
        if people[i] == 0:
            i+=1
            continue
        else:
            check+=1
            if check == 9:#数到9把people[i]的值改为0，最后查看people字典值为1的都活下来，值为0的都跳船了
                people[i]=0
                check = 0#check归零，再重新计数，这样就不用计算9的倍数了
                print("{}号下船了".format(i))
                j+=1
            else:
                i+=1
                continue
save=[]#获救的人
die=[]#跳船的人
for i in people:
    if people[i]==1:#注意字典中通过for遍历后想要访问某个键：字典名[键名]
        save.append(i)#把people字典中i值为1添加到save列表
    if people[i]==0:#把people字典中i值为0的添加到die列表
        die.append(i)
print(save,'\n',die)