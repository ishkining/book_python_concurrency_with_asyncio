import aiohttp
import asyncio
from aiohttp import ClientSession


import path_project
from chapter_4_concurrent_web_requests import fetch_status
from util import async_timed


@async_timed()
async def main():
    async with ClientSession() as session:
        urls = ['https://www.example.com' for _ in range(1000)]
        requests = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*requests)
        print(status_codes)


asyncio.get_event_loop().run_until_complete(main())
