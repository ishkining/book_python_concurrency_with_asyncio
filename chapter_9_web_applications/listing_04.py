from aiohttp import web
from aiohttp.web_app import Application
from aiohttp.web_request import Request
from aiohttp.web_response import Response

import asyncpg

from listing_03 import create_db_pool, destroy_db_pool

routes = web.RouteTableDef()
DB_KEY = 'database'


@routes.post('/product')
async def create_product(request: Request) -> Response:
    PRODUCT_NAME = 'product_name'
    BRAND_ID = 'brand_id'

    if not request.can_read_body:
        raise web.HTTPBadRequest()

    body = await request.json()

    if PRODUCT_NAME in body and BRAND_ID in body:
        db = request.app[DB_KEY]
        await db.execute('''INSERT INTO product(
            product_id,
            product_name,
            brand_id
        ) VALUES (DEFAULT, $1, $2)''', body[PRODUCT_NAME], int(body[BRAND_ID]))

        return web.Response(status=201)
    else:
        raise web.HTTPBadRequest()


app = Application()
app.on_startup(create_db_pool)
app.on_cleanup(destroy_db_pool)

app.add_routes(routes)
web.run_app(app)
