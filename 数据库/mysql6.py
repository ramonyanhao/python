import aiomysql
import asyncio
import logging
import traceback
'''
mysql 异步版本
'''

logobj = logging.getLogger('mysql')

class Pmysql:
    __connection = None

    def __init__(self):
        self.cursor = None
        self.connection = None

    @staticmethod
    async def getconnection():
        if Pmysql.__connection == None:
            conn = await aiomysql.connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                password='root',
                db='ramon',
                )
            if conn:
                Pmysql.__connection = conn
                return conn
            else:
                raise("connect to mysql error ")
        else:
            return Pmysql.__connection

    async def query(self,query,args=None):  # args=None这种写法在传参进来时，指定args可以替代None,不指定也不会报错
        self.cursor = await self.connection.cursor()
        await self.cursor.execute(query,args)
        r = await self.cursor.fetchall()
        await self.cursor.close()
        return r


async def test():
    conn = await Pmysql.getconnection()  # 这里首先拿到一个连接conn
    mysqlobj.connection = conn  # 注意这里又把上面的连接赋值到mysqlobj.connection,mysqlobj是整个Pmysql类的变量，在Pmysql下面有一个实例变量connection
    await conn.ping()  # connection.ping()方法来检查一下连接是否有效，该方法默认会在连接无效的时候进行重新连接
    r = await mysqlobj.query("select * from site")
    for i in r:
        print(i)
    conn.close()

if __name__ == '__main__':
    mysqlobj = Pmysql()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())