import orm
from models import User, Blog, Comment
import asyncio
loop=asyncio.get_event_loop()
async def test():

    await orm.create_pool(user='www-data', password='www-data', db='awesome',loop=loop)

    u = User(name='Test12', email='test12@example.com', passwd='12345601123', image='about:blank')

    await u.save()


loop.run_until_complete(test())

