import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    passwd='manageMENT!1',
    user='root',
    database='ramon'
)
mycursor=mydb.cursor()
#使用update更新表数据
sql = "UPDATE site SET name = %s WHERE name = %s"
val = ("ZH", "Zhihu")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, " 条记录被修改")
mycursor.execute("select * from site")
for i in mycursor:
    print(i)
#删除表数据使用 "DROP TABLE" 语句， IF EXISTS 关键字是用于判断表是否存在，只有在存在的情况才删除
#mycursor.execute("drop table if exists site")
#import python文件时不需要加后缀.py,直接import 文件名即可，如果文件不在import搜索路径中，需要加入sys.path.append(文件路径)
# 如果import的pathon文件在不同的目录下，则在目录中新建__init__.py空白文件即可