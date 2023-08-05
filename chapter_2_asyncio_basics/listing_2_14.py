from asyncio import Future

mu_future = Future()

print(f'Is my future done {mu_future.done()}')

mu_future.set_result(32)

print(f'Is my future done {mu_future.done()}')
print(f'Result is {mu_future.result()}')
