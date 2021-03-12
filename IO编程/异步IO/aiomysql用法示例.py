import asyncio
import aiomysql

# 普通用法
async def test_example(loop):
    conn = await aiomysql.connect(host='127.0.0.1', port=3306,
                                  user='root', password='root', db='testdb',
                                  loop=loop)

    async with conn.cursor() as cur:
        await cur.execute("SELECT * FROM score")
        print(cur.description)
        r = await cur.fetchall()
        print(r)
    conn.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(test_example(loop))

# 存储过程示例
async def test_procedure(loop):
    conn = await aiomysql.connect(host='127.0.0.1', port=3306,
                                  user='root', password='root',
                                  db='testdb', loop=loop)

    async with conn.cursor() as cur:
        await cur.execute('DROP PROCEDURE IF EXISTS myinc;')  # PROCEDURE就是mysql存储过程，后面的myinc就是存储过程变量名
        await cur.execute("""CREATE PROCEDURE myinc(p1 INT)   
                             BEGIN
                                 SELECT p1 + 1;
                             END""")

        await cur.callproc('myinc', [1])
        # callproc(procname，args)用args执行存储过程procname，此方法为协程，需要在前面使用await执行,这里就相当于把1传参到存储过程myinc的p1变量中,p1+1=2
        (ret, ) = await cur.fetchone()
        assert 2, ret
        print(ret)

    conn.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(test_procedure(loop))

# cur.executemany用法：
async def test_example_executemany(loop):
    conn = await aiomysql.connect(host='127.0.0.1', port=3306,
                                       user='root', password='root',
                                       db='testdb', loop=loop)

    async with conn.cursor() as cur:
        await cur.execute("DROP TABLE IF EXISTS music_style;")
        await cur.execute("""CREATE TABLE music_style
                                  (id INT,
                                  name VARCHAR(255),
                                  PRIMARY KEY (id));""")
        await conn.commit()

        # insert 3 rows one by one
        await cur.execute("INSERT INTO music_style VALUES(1,'heavy metal')")
        await cur.execute("INSERT INTO music_style VALUES(2,'death metal');")
        await cur.execute("INSERT INTO music_style VALUES(3,'power metal');")
        await conn.commit()

        # 使用executemany方法一次性插入三行数据
        data = [(4, 'gothic metal'), (5, 'doom metal'), (6, 'post metal')]
        await cur.executemany(
            "INSERT INTO music_style (id, name)"
            "values (%s,%s)", data)
        await conn.commit()

        # fetch all insert row from table music_style
        await cur.execute("SELECT * FROM music_style;")
        result = await cur.fetchall()
        print(result)

    conn.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(test_example_executemany(loop))

# 事务回滚和提交:
async def test_example_transaction(loop):
    conn = await aiomysql.connect(host='127.0.0.1', port=3306,
                                  user='root', password='root',
                                  db='testdb', autocommit=False,
                                  loop=loop)

    async with conn.cursor() as cursor:
        stmt_drop = "DROP TABLE IF EXISTS names"
        await cursor.execute(stmt_drop)
        await cursor.execute("""
            CREATE TABLE names (
            id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
            name VARCHAR(30) DEFAULT '' NOT NULL,
            cnt TINYINT UNSIGNED DEFAULT 0,
            PRIMARY KEY (id))""")
        await conn.commit()

        # Insert 3 records
        names = (('Geert',), ('Jan',), ('Michel',))
        stmt_insert = "INSERT INTO names (name) VALUES (%s)"
        await cursor.executemany(stmt_insert, names)

        # Roll back!!!!
        await conn.rollback()

        # There should be no data!
        stmt_select = "SELECT id, name FROM names ORDER BY id"
        await cursor.execute(stmt_select)
        resp = await cursor.fetchall()
        # Check there is no data
        assert not resp

        # Do the insert again.
        await cursor.executemany(stmt_insert, names)

        # Data should be already there
        await cursor.execute(stmt_select)
        resp = await cursor.fetchall()
        print(resp)
        # Do a commit
        await conn.commit()

        await cursor.execute(stmt_select)
        print(resp)

        await cursor.close()
        conn.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(test_example_transaction(loop))

# 连接池示例：
async def test_pool(loop):
    pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                      user='root', password='root',
                                      db='testdb', loop=loop)
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT 42;")
            (r,) = await cur.fetchone()
            assert r == 42
            print()
            print('ok')
    pool.close()
    await pool.wait_closed()


loop = asyncio.get_event_loop()
loop.run_until_complete(test_example(loop))