import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    passwd='manageMENT!1',
    user='root',
    database='ramon'
)
mycursor=mydb.cursor()
#mycursor.execute("CREATE TABLE site (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), url VARCHAR(255),uptime timestamp default current_timestamp on update current_timestamp)")
sql="insert into site (name,url) values (%s,%s)"
val= [
  ('Google','https://www.google.com'),
  ('Github','https://www.github.com'),
  ('Taobao','https://www.taobao.com'),
  ('stackoverflow','https://www.stackoverflow.com/')
]
mycursor.executemany(sql, val)#excute执行一条sql语句，executemany同时执行多条语句,如果表中批量插入数据，使用executemany更快
print(mycursor.rowcount,"条记录插入成功")
mycursor.execute("insert into site (name,url) values ('zhihu','www.zhihu.com')")
print("1 条记录已插入, ID:", mycursor.lastrowid)#mycursor.lastrowid返回最后插入数据的id号,id列一般是表中的主键，而且不重复
mycursor.execute('desc site')
for i in mycursor:#这里也可以用for i in mycursor.fetchall(),fetchall()作用是接收全部的返回结果行
    print(i)
#如果遇到两次查询时，如desc site和select * from site，必须先输出一次查询结果再执行下一次，否则报错发现未读的结果
mycursor.execute('select * from site')
for x in mycursor:
    print(mycursor.rowcount,x)#mycursor.rowcount 计算前面的行号
#还可以使用fetchall()来输出返回的结果，如
'''
result=mycursor.fetchall()  返回所有查询结果
for i in result:
    print(i)
result1=mycursor.fetchone()  只返回一条查询结果
print(result1)
'''
#mycursor.execute("delete from site where name='名字'")#可以使用这条命令删除表中重复的数据
mydb.commit()#数据表有更新最后一定要使用这个语句提交事务，否则mysql数据表不会更新,注意如果有mydb.commit()，执行一次这个脚本文件就会插入一次数据