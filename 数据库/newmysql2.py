import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    passwd='manageMENT!1',
    user='root',
    database='ramon'
)
mycursor=mydb.cursor()
mycursor.execute("select * from site where name like '%oo%'")
result=mycursor.fetchall()#返回所有查询的结果并赋值给result变量
for i in result:
    print(i)
print(mycursor.fetchone())#注意如果前面使用过fetchall，结果集为空，fetchone返回None
#查询结果排序可以使用 ORDER BY 语句，默认的排序方式为升序，关键字为 ASC，如果要设置降序排序，可以设置关键字 DESC
mycursor.execute("select * from site order by name DESC")
for i in mycursor:
    print(i)
mycursor.execute("SELECT * FROM site LIMIT 3 OFFSET 1")#limit限制查询数量为3行，offset表示查询从第几条开始，0为第一条，1为第2条
for i in mycursor:#因为mycursor.fetchall已经返回了所有结果，行数已经固定了，使用rowcount每行输出的都是总行数，所以如果想要输出的结果中有每行的行数，那在for循环中最好不要使用for i in mycursor.fetchall()
    print(mycursor.rowcount,i)
print(mycursor.rowcount)#rowcount输出的是结果总行数，如果rowcount在for循环内，输出的行数从1开始叠加，
#在修改表数据，增加或者删除时，最好使用变量和占位符%s,如：
'''
sql = "DELETE FROM site WHERE name = %s"
na = ("stackoverflow", )
 
mycursor.execute(sql, na)
 
mydb.commit()
 
print(mycursor.rowcount, " 条记录删除")
'''
# 最后验证完再用mydb.commit()提交，防止数据丢失