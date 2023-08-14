import asyncio
import aiohttp
from aiohttp import ClientSession
import logging

import path_project
from util import async_timed
from chapter_4_concurrent_web_requests import fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        good_request = fetch_status(session, 'https://www.example.com')
        bad_request = fetch_status(session, 'stupid://amI')

        fetchers = [
            asyncio.create_task(good_request),
            asyncio.create_task(bad_request),
        ]

        done, pending = await asyncio.wait(fetchers)

        print(f'Done task count: {len(done)}')
        print(f'Pending task count: {len(pending)}')

        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error('Request got exception',
                              exc_info=done_task.exception())


asyncio.get_event_loop().run_until_complete(main())
