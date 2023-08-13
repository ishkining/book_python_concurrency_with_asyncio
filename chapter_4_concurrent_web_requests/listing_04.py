import asyncio

import path_project
from util import async_timed, delay


@async_timed()
async def main():
    delay_times = [3, 3, 3]
    [await asyncio.create_task(delay(seconds)) for seconds in delay_times]


asyncio.run(main())
