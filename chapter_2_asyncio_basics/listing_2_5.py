import asyncio


async def hello() -> str:
    await asyncio.sleep(1)
    return 'Hello world'


async def main() -> None:
    message = await hello()
    print(message)


asyncio.run(main())
