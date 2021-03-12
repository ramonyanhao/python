import pymysql
#操作数据库与操作文件类似，在读取修改开始和结束时都需要进行连接（打开），断开（关闭）等固定操作，文件读写时可以使用 with （上下文管理器）来简化操作，数据库当然也是可以的
class DB():
    def __init__(self, host='localhost', port=3306, db='ramon', user='root', passwd='root', charset='utf8'):
        # 建立连接
        self.conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset=charset)
        # 创建游标，操作设置为字典类型
        self.cur = self.conn.cursor(cursor = pymysql.cursors.DictCursor)
#pymysql默认返回的数组为元组类型，设置cursor游标为cursors.dictcursor表示返回的数组为字典类型
    def __enter__(self):
        # 返回游标
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 提交数据库并执行
        self.conn.commit()
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()

db_dict={
    'host':'localhost',
    'port':3306,
    'db':'ramon',
    'user':'root',
    'passwd':'root',
    'charset':'utf8'
}

if __name__ == '__main__':
    with DB() as db:#通过上面的__enter__和__exit__属性，这里可以使用with
        db.execute('select * from site')
        for i in db:
            print(i)
    conn = pymysql.connect(**db_dict)
    cursor = conn.cursor()
    cursor.execute('select * from site')
    print(cursor.fetchall())
    print(cursor.rowcount)