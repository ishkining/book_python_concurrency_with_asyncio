import asyncio

import path_project
from util import async_timed, delay


@async_timed()
async def cpu_bound_work() -> int:
    counter = 0
    for i in range(100_000_000):
        counter += counter
    return counter


@async_timed()
async def main() -> None:
    task_one = asyncio.create_task(cpu_bound_work())
    task_two = asyncio.create_task(cpu_bound_work())
    delay_task = asyncio.create_task(delay(4))

    await task_one
    await task_two
    await delay_task


asyncio.run(main())
