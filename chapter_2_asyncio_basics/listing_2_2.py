async def async_add(n: int) -> int:
    return n + 1


def add(n: int) -> int:
    return n + 1


function_result = add(1)
coroutine_result = async_add(1)

print(f'Function result is {function_result} and type is {type(function_result)}')
print(f'Async result is {coroutine_result} and type is {type(coroutine_result)}')
