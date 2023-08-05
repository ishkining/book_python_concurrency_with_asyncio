import asyncio

import path_project
from util import delay


async def main() -> None:
    delay_task = asyncio.create_task(delay(2))
    try:
        result = await asyncio.wait_for(delay_task, timeout=1)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Timeout bitch!')
        print(f'Was it cancelled {delay_task.cancelled()}')


asyncio.run(main())
