from 数据库 import mysqlnew
db = mysqlnew.mysqlcon  # 这样可以在一个文件中设定统一的数据库连接账户和密码，然后在其他文件连接数据库时导入这个配置文件来使用
cursor=db.cursor()
cursor.execute("show databases")
print(cursor.fetchall())
# cursor.execute("create database testdb")
# cursor.execute("create table employee (id int not null auto_increment primary key,firstname char(255) not null,lastname char(255) not null,age int,sex char(10),income char(255))")
cursor.execute("desc employee")
for i in cursor:
    print(i)
# cursor.execute("create user 'testuser'@'localhost' identified by 'test123'")
# cursor.execute("grant all privileges on testdb.* to testuser@localhost")
sql="insert into employee (firstname,lastname,age,sex,income) values ('mac','mohan',20,'M',2000)"
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
cursor.execute("update employee set age=age+1 where sex='M'")#找出sex=M的数据更新age字段加1
cursor.execute("select * from employee")
print(cursor.fetchall())
