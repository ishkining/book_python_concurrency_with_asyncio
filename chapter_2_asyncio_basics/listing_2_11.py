import asyncio
from asyncio import CancelledError

import path_project
from util import delay


async def main() -> None:
    long_task = asyncio.create_task(delay(10))

    seconds_elapsed = 0

    while not long_task.done():
        print('checking')
        await asyncio.sleep(1)
        seconds_elapsed += 1
        if seconds_elapsed == 5:
            long_task.cancel()

    try:
        await long_task
    except CancelledError:
        print('Our task is cancelled')


asyncio.run(main())
