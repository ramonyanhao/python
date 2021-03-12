import random
a=random.randint(0,10)#系统自动生成0到10的随机数
i=1
while 1:
    try:
        b=int(input('input number0-10:'))#b放在这里表示通过错误检查输入的是否为数字，如果不是则跳出异常
        if a<b:
            print('you input than computer big')
            b = int(input('input 0-10:'))#如果这里不加b=则不会改变b的值，系统比较的一直都是之前的值，所以会一直跳相同结果
        elif a>b:
            print('you input than computer small')
            b = int(input('input 0-10:'))#改变b的值为当前输入的值
        i+=1
    except ValueError:
        print('please input number')

    else:
        print('ok,used to %.f times'%(i))
        break

