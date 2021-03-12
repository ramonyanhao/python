# 如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。 例如1^3 + 5^3 + 3^3 = 153
lower = int(input("最小值: "))
upper = int(input("最大值: "))

for num in range(lower, upper + 1):
    # 初始化 sum
    suma = 0
    # 指数
    n = len(str(num))#这里注意想要获取len的值，括号里不能是整数类型，需要转换为字符串类型才能获取位数，range也是把一个数转换为列表，通过len计算列表里的个数
    # 检测
    temp = num#在下面while循环中需要改变num的值，所以这里通过把num再赋值到另一个变量temp，while循环只会更改temp的值，最终结果不会影响num的值
    while temp > 0:
        digit = temp % 10#这里的公式代表取出temp值的最后一位数字，比如temp=123，先取出个位，123%10=3,digit=3;再一次循环digit=12%10=2;再一次循环1%10=1
        suma += digit ** n#这里计算sum开始自相加temp值最后一位数字的n次方，sum+=3**3，sum=27;再一次循环sum+=2**3,27+8=35;再一次循环sum+=1**3,35+1=36
        temp //= 10#这里代表通过每次while循环把temp值向前推进一位，比如temp=123,上面的digit代表了temp个位数，这里向前一位123//10=12;再一次循环12//10=1;再一次循环1//10=0,temp=0不符合while条件，退出循环
#其实while循环的意思就是取出temp的每一位数，然后把这些数的n次方相加是否等于我们要查询的数，这里的例子得出的最终结果是sum=36,不是123,所以123就不是阿姆斯特朗数
    if num == suma:#如果sum自相加到最后等于我们需要查询的数，那查询的这个数就是阿姆斯特朗数
        print(num)

lower=int(input("Please input a number: "))
upper=int(input("Please input a number: "))
suma=0
for num in range(lower,upper):
    l = len(str(num))
    for n in str(num):#还有一种循环嵌套方法：for n in str(num)得出n的值都是字符串类型的num,而且还包括num本身，这是因为上一层for循环下来的值在这层for循环通过str原样输出
        suma=suma+int(n)**l#这里再把n的值转换为整数类型，这种方法不用计算num的个位，十位，百位，通过str可以把一个数的个位，十位，百位单独列出来，比如for n in str(10)输出的n值就是1和0
    if num==suma:
        print(num)
    suma=0

#通过列表推导式查询阿姆斯特朗数
lower=int(input("Please input a number: "))
upper=int(input("Please input a number: "))
y = [x for x in range(lower,upper+1) if sum([int(i)**len(str(x)) for i in str(x)])==x]
#x是当前查询的数，i是x的个位，十位，百位等等，但是i的值是字符串类型，使用时需要转换整数，把x所有位数的n次方相加是否等于x
print(y)