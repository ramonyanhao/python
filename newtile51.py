import random
aa=range(0,10)
a=random.sample(aa,2)#从aa列表中生成两个随机数
print(a)
b=input('input two number 0-10:')#输入两个字符串数字，这里如果加int会报错
sides=[int(side) for side in b.split(',')]#把输入的两个字符串改为整数类型，并生成一个列表使用逗号分开
print(sides)
b=sides#再赋值给b
i=1
while a!=b:
    if a<b:
        print('bigger')
        b = input('input two number 0-10:')
        sides = [int(side) for side in b.split(',')]
        b = sides
    else:
        print('small')
        b = input('input two number 0-10:')
        sides = [int(side) for side in b.split(',')]
        b = sides
    i+=1
else:
    print('ok,used to %.f times'%(i))
