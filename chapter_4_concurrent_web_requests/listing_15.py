import asyncio
import aiohttp
from aiohttp import ClientSession

import path_project
from chapter_4_concurrent_web_requests import fetch_status
from util import async_timed


@async_timed()
async def main():
    async with ClientSession() as session:
        url = 'https://www.example.com'
        fetchers = [
            asyncio.create_task(fetch_status(session, url)),
            asyncio.create_task(fetch_status(session, url)),
            asyncio.create_task(fetch_status(session, url, delay=3)),
        ]

        done, pending = await asyncio.wait(fetchers, timeout=1)

        for done_task in done:
            result = await done_task
            print(result)


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
