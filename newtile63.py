lst = list(range(1,31))
j,k = 1,0#列表索引都是从0开始的，列表内容从1开始，所以列表索引0就是列表内容1
while True:
    if len(lst) > 15:
        if j == 9:
            print('{:<2d}号被抛下'.format(lst[k]))
            lst.remove(lst[k])
            j = 1
        else:
            j += 1
            k += 1
        if len(lst) == k:#这里的意思是当lst列表元素数量等于k时，k取值为0，因为k用作lst列表的索引，如果lst列表的元素数量和索引不一致会报错
            k = 0#k的值会一直增加，所以列表lst的索引k会比lst列表元素多
    else:
        break
#filter()函数和lambda一起使用，filter返回的值是符合lambda公式条件的值组成的列表，不符合的去掉，注意filter只接受一个参数列表，而且filter不会返回lambda计算的结果
#map()函数也和lambda一起使用，map返回的值是通过lambda计算出来的结果组成的列表，map可以接受多个参数列表，如果多个列表里的元素不一样多，计算时只采用列表元素最少的一个
people=list(range(1,31))#这种方法把people列表符合while条件的放在列表最后，当i=9时把people列表第一个数取出然后添加到peopledie列表
peopledie = []
while len(people)>15:

    i=1
    while i<9:#当i=9时，people列表第一个数就是我们需要的数
        people.append(people.pop(0))#这里很重要，当i<9时，people列表开始循环，把第一个数取出再添加到列表的最后
        i+=1
    print('{:2d}号下船了'.format(people[0]))
    peopledie.append(people.pop(0))
    print(peopledie)
    print(people)
