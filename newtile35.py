#调用类方法
class 成绩单():       #定义类
    @classmethod     #声明类方法,声明后可以使用类成绩单里的变量和函数
    def 录入成绩单(cls):
        cls.学生姓名 = input('请输入学生姓名：')
        cls.语文_成绩 = int(input('请输入语文成绩：'))
        cls.数学_成绩 = int(input('请输入数学成绩：'))

    @classmethod#再函数计算平均分中，声明了类方法后，参数cls就是类成绩单()
    def 计算平均分(cls):
        平均分 = (cls.语文_成绩 + cls.数学_成绩)/2#这里的语句可以理解为平均分 = (成绩单().语文_成绩 + 成绩单().数学_成绩)/2
        return 平均分       #因为此方法我们需要调用，所以用return返回结果便于后面的调用

    @classmethod#这里也可以去掉，不声明类方法，后面的参数cls全部改成类名成绩单
    def 评级(cls):#这里可以把参数cls去掉，下面代码把cls都改成成绩单
        平均分 = cls.计算平均分()        #类方法调用其他的方法
        if 平均分>=90:
            print(cls.学生姓名 + '的评级是：优')
        elif 平均分>= 80 and 平均分<90 :
            print(cls.学生姓名 + '的评级是：良')
        elif 平均分>= 60 and 平均分<80 :
            print(cls.学生姓名 + '的评级是：中')
        else:
            print(cls.学生姓名 + '的评级是：差')

成绩单.录入成绩单()#使用@classmethod可以不用实例化类就可以输出，例如直接使用成绩单.方法名就可以输出，不用实例化类a=成绩单()
成绩单.评级()
#从内部修改/增加类属性
class 类():          #定义类
    @classmethod          #声明类方法
    def 增加类属性(cls):
        cls.变量 = input('请随意输入字符串：')    #从内部增加属性

类.增加类属性()  #调用类方法就可以在下面使用函数增加类属性里的变量函数，如果没有调用，在下面print(类.变量)就会报错

print('打印新增的类属性：')
print(类.变量)                  #调用属性并打印出来
#实例化一个类相当于复制一个类到一个变量，这个变量就是实例，实例和类拥有相同的内容，修改类属性，实例属性会随着更改，修改实例属性不会影响类，实例是独立的个体，修改指定实例属性后，再修改类属性只会影响到未被修改的实例属性
#实例属性的修改并不会影响到类属性
class 类():
    变量 = 100

实例1 = 类() # 实例化
实例2 = 类() # 实例化

print('原先的类属性：')
print(类.变量)
print('原先的实例1属性：')
print(实例1.变量)
print('原先的实例2属性：')
print(实例2.变量)

实例1.变量 = 'abc'
print('--------修改实例1的属性后----------')

print('现在的类属性：')
print(类.变量)
print('现在的实例1属性：')
print(实例1.变量)
print('现在的实例2属性：')
print(实例2.变量)

#“重写类方法”分成两个步骤：第一个步骤是在类的外部写一个函数，第二个步骤是把这个新函数的名字赋值给类.原始函数
class 类():
    def 原始函数(self):
        print('我是原始函数！')

def 新函数(self):         #定义新方法
    print('我是重写后的新函数!')

a = 类()  # 实例化
a.原始函数()

# 用新函数代替原始函数，也就是【重写类方法】
类.原始函数 = 新函数#这里特别注意不能重写实例，如果使用a.原始函数=新函数就会报错，因为实例方法不能被重写，实例属性是可以新增或修改

# 现在原始函数已经被替换了
a.原始函数()
