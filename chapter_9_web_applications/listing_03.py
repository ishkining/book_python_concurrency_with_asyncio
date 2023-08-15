from aiohttp import web
from aiohttp.web_app import Application
from aiohttp.web_request import Request
from aiohttp.web_response import Response

import asyncpg
from asyncpg import Record
from asyncpg.pool import Pool

routes = web.RouteTableDef()
DB_KEY = 'database'


async def create_db_pool(app: Application):
    print('Creating db pool')
    pool: Pool = await asyncpg.create_pool(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        password='test',
        database='test_ai_async_db',
        min_size=6,
        max_size=6
    )

    app[DB_KEY] = pool


async def destroy_db_pool(app: Application):
    print('Destroying db pool')
    pool: Pool = app[DB_KEY]
    await pool.close()


@routes.get('/products/{id}')
async def get_product(request: Request) -> Response:
    try:
        str_id = request.match_info('id')
        product_id = int(str_id)

        query = 'SELECT product_id, product_name, brand_id' \
                'FROM product' \
                'WHERE product_id = $1'

        connection: Pool = request.app[DB_KEY]
        result: Record = await connection.fetchrow(query, product_id)

        if result is not None:
            return web.json_response(dict(result))
        else:
            raise web.HTTPNotFound
    except ValueError:
        raise web.HTTPBadRequest


app = Application()
app.on_startup.append(create_db_pool)
app.on_cleanup.append(destroy_db_pool)

app.add_routes(routes)
web.run_app(app)
