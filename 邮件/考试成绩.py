chinese=int(input("语文"))
maths=int(input("数学"))
english=int(input("英语"))
get=""
if (chinese ==100 or maths ==100 or english ==100):
    if chinese ==100:get += "语文"
    if maths == 100:get +="数学"
    if english ==100:get +="英语"
    print("你的%s得了100分，奖励小红花"%get)
elif ((chinese >=90 and maths>=90)or (chinese>=90 and english>=90) or (maths>=90 and english>=90)):
#如果这里条件使用if，遇到两门成绩都是100的时候结果会输出两条记录，符合=100的条件同时也符合>=90的条件，所以这里使用elif,如果符合=100，那elif就不会执行，否则执行>=90的条件
#如果想要多行加#注释，可以把需要注释的行选中然后使用快捷键ctrl+/
    if (chinese>=90):get+="语文"
    if maths>=90:get+="数学"
    if english>=90:get+="英语"
    print("你的%s大于90分，奖励小红花"%get)
else:
    if(chinese>=80 and maths>=80 and english>=80):
        print("你的数学，语文，英语都大于80分，奖励小红花")
x = 10
expr = """
z = 30
sum = x + y + z
print(sum)
"""
#python内置函数exec可以执行"""注释过的内容
def func():
    y = 20
    exec(expr)#这里的结果是60,sum=10+20+30
    exec(expr, {'x': 1, 'y': 2})#这里的结果是33,sum=1+2+30
    exec(expr, {'x': 1, 'y': 2}, {'y': 3, 'z': 4})#注意这里的结果是34,sum=1+3+30,在expr中的变量z，exec运行不管怎么改变这个值，最后取值都是在expr中的值
    # 而x和y都是在expr之外赋值的变量，所以这里根据字典里取值，x=1,y=3,因为后面的字典中只给y赋值为3，所以x的值取前面字典中的赋值1
    # exec(object[, globals[, locals]])
    # object：必选参数，表示需要被指定的Python代码。它必须是字符串或code对象。如果object是一个字符串，该字符串会先被解析为一组Python语句，然后在执行（除非发生语法错误）。如果object是一个code对象，那么它只是被简单的执行。
    # globals：可选参数，表示全局命名空间（存放全局变量），如果被提供，则必须是一个字典对象。
    # locals：可选参数，表示当前局部命名空间（存放局部变量），如果被提供，可以是任何映射对象。如果该参数被忽略，那么它将会取与globals相同的值。
func()