import asyncio

import path_project
from util import delay


async def main() -> None:
    task = asyncio.create_task(delay(10))

    try:
        result = await asyncio.wait_for(asyncio.shield(task), 5)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Task took too long')
        result = await task
        print(result)


asyncio.run(main())
