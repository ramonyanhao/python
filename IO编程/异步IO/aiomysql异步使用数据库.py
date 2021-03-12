import asyncio
import aiomysql

loop = asyncio.get_event_loop()

async def go():
    pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                           user='root', password='root',
                                           db='testdb', loop=loop, autocommit=False)

    # 使用acquire可以从空闲池获得连接的协程。如果需要，创建新的连接，并且池的大小小于maxsize。也可以使用async with pool.get() as conn:从池中获得一个连接，但是pool.get()已经弃用，现在用pool.acquire替代
    # 需要注意这里使用了async,因为async的作用是把一个generator标记为coroutine类型，然后在coroutine内部用await调用另一个coroutine实现异步操作,最后我们就把这个coroutine扔到EventLoop中执行，with就是一个generator类型
    async with pool.acquire() as conn:
        cur = await conn.cursor()
        await cur.execute("SELECT 10")
        print(cur.description)
        (r,) = await cur.fetchone()
        assert r == 10
        print('ok')
    # pool.release(conn) 释放掉conn,将连接放回到连接池中,由于使用with，所有的连接使用完自动关闭，不需要release释放。
    pool.close()  # 关闭连接池，如果连接池中还有连接在运行的话，需要运行wait_closed等待运行的连接关闭后再关闭整个连接池
    # pool.terminate() 终止池，同时立即关闭所有获得的连接。如果连接池中还有连接在运行的话，需要运行wait_closed等待运行的连接关闭后再关闭整个连接池
    # await pool.wait_closed()  等待释放和关闭所有获得的连接的协程。应该在close()之后调用，以等待实际的池关闭。由于使用with，所有的连接使用完自动关闭，不需要等待。

loop.run_until_complete(go())