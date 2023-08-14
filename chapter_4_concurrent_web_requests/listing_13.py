import aiohttp
import asyncio
import logging
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
            asyncio.create_task(fetch_status(session, url)),
        ]

        done, pending = await asyncio.wait(fetchers, return_when=asyncio.FIRST_COMPLETED)

        print(f'Done task count {len(done)}')
        print(f'Pending task count {len(pending)}')

        for done_task in done:
            print(await done_task)


asyncio.get_event_loop().run_until_complete(main())
