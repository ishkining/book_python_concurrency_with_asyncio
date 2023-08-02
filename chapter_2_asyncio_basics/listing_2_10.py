import asyncio

import path_project
from util import delay


async def hello() -> None:
    for i in range(2):
        await asyncio.sleep(1)
        print('Im running this shit')


async def main():
    first_delay = asyncio.create_task(delay(3))
    second_delay = asyncio.create_task(delay(3))
    await hello()
    await first_delay
    await second_delay


asyncio.run(main())
