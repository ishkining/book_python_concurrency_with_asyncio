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
            asyncio.create_task(fetch_status(session, 'https://www.example.com')),
            asyncio.create_task(fetch_status(session, 'https://www.example.com')),
        ]
        done, pending = await asyncio.wait(fetchers)

        print(f'Done tasks {len(done)}')
        print(f'Pending cases {len(pending)}')

        for done_task in done:
            result = await done_task
            print(result)


asyncio.get_event_loop().run_until_complete(main())
