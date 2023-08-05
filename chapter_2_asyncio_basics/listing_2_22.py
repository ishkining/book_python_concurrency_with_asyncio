import asyncio

import path_project
from util import delay


def call_later() -> None:
    print('func smth doing')


async def main() -> None:
    loop = asyncio.get_running_loop()
    loop.call_soon(call_later)
    await delay(1)


asyncio.run(main())
