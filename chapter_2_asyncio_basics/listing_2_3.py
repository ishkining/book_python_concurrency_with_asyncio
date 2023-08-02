import asyncio


async def coroutine_add(n: int) -> int:
    return n + 1


result = asyncio.run(coroutine_add(1))

print(result)
