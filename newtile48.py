def isTriangle(a,b,c):
    flag=1
    if(a+b>c and a+c>b and b+c>a):
        if(a==b==c):
            print("输入数据构成的三角形为等边三角形")
        elif(a==b or a==c or b==c):
            print("输入数据构成的三角形为等腰三角形")
        else:
            print("输入数据构成的三角形为普通三角形")
        flag=1
    else:
        #print("输入数据不能构成三角形，请重新输入数据！")
        flag=0
    return flag
#计算三角形的面积
def triangleArea(a,b,c):
    if(isTriangle(a,b,c)==1):
        # 计算半周长
        s = (a + b + c) / 2
        # 计算面积
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('三边边长分别为{0} {1} {2}的三角形的面积为{3:.2f}'.format(a,b,c,area))
    else:
        print("输入数据不能构成三角形，请重新输入数据！")
        a=float(input("请输入三角形第一条边长的数据："))
        b=float(input("请输入三角形第二条边长的数据："))
        c=float(input("请输入三角形第三条边长的数据："))
        triangleArea(a,b,c)
a=float(input("请输入三角形第一条边长的数据："))
b=float(input("请输入三角形第二条边长的数据："))
c=float(input("请输入三角形第三条边长的数据："))
triangleArea(a,b,c)