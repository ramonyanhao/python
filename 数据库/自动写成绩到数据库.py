import pymysql
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
            return cls.学生姓名 + '的评级是：优'
        elif 平均分>= 80 and 平均分<90 :
            return cls.学生姓名 + '的评级是：良'
        elif 平均分>= 60 and 平均分<80 :
            return cls.学生姓名 + '的评级是：中'
        else:
            return cls.学生姓名 + '的评级是：差'
def mys():
    db=pymysql.connect("localhost","root","root","testdb")
    cursor=db.cursor()
    cursor.execute("create table if not exists score (id int not null auto_increment primary key,name char(255) not null,chinese_score float(5,2) not null,math_score float(5,2) not null,rating char(255) not null)")
    cursor.execute("desc score")
    for i in cursor:
        print(i)
    data="insert into score (name,chinese_score,math_score,rating) values (%s,%s,%s,%s)"
    value=(成绩单.学生姓名,成绩单.语文_成绩,成绩单.数学_成绩,成绩单.评级())
    try:
        cursor.execute(data,value)
        db.commit()
    except:
        db.rollback()
    cursor.execute("select * from score")
    for i in cursor:
        print(i)
    cursor.close()
    db.close()

if __name__ == "__main__":
    while True:
        成绩单.录入成绩单()  # 使用@classmethod可以不用实例化类就可以输出，例如直接使用成绩单.方法名就可以输出，不用实例化类a=成绩单()
        成绩单.评级()
        mys()
        a=input("是否继续Y/N:")
        if a == 'N' or a == 'n':
            break
