from aiohttp import web
import asyncio
routes = web.RouteTableDef()


@routes.get('/')
async def index(request):
    await asyncio.sleep(2)
    return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html')


@routes.get('/about')
async def about(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>about us</h1>',content_type='text/html')
def init():
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app,host='127.0.0.1',port=9999)
init()