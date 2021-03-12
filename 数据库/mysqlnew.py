import pymysql

mysqlcon = pymysql.connect(
        host='localhost',
        port=3306,
        db='testdb',
        user='root',
        passwd='root',
        charset='utf8')

# 在其他脚本中直接 from 数据库 import mysqlnew 导入这个文件
# 然后再需要输入数据库连接信息时直接使用导入的这个文件，这样就不会把一些数据库账户密码明文写在脚本中了
'''
db = mysqlnew.mysqlcon
cursor=db.cursor()
cursor.execute("show databases")
print(cursor.fetchall())
'''