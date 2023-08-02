import path_project
import asyncio
from util import delay


async def add_one(n: int) -> int:
    return n + 1


async def hello() -> str:
    await delay(1)
    return 'Hello world'


async def main() -> None:
    message = await hello()
    one_plus_one = await add_one(1)
    print(one_plus_one)
    print(message)


asyncio.run(main())
