import asyncio
import aiohttp

import path_project
from chapter_4_concurrent_web_requests import fetch_status


async def main():
    async with aiohttp.ClientSession() as session:
        api_a = fetch_status(session, 'https://www.example.com')
        api_b = fetch_status(session, 'https://www.example.com', delay=2)

        done, pending = await asyncio.wait([api_a, api_b], timeout=1)

        for task in pending:
            if task is api_b:
                print('api b too slow')
                task.cancel()

asyncio.get_event_loop().run_until_complete(main())