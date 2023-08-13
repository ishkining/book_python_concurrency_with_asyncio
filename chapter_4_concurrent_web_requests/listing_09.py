import asyncio
import aiohttp
from aiohttp import ClientSession

import path_project
from util import async_timed
from chapter_4_concurrent_web_requests import fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        fetchers = [
            fetch_status(session, 'https://www.example.com', 1),
            fetch_status(session, 'https://www.example.com', 1),
            fetch_status(session, 'https://www.example.com', 10),
        ]
        for finished_task in asyncio.as_completed(fetchers, timeout=2):
            try:
                result = await finished_task
                print(result)
            except asyncio.TimeoutError:
                print('timeout')


asyncio.get_event_loop().run_until_complete(main())
