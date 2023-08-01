import time


def print_fib(number: int) -> None:
    def fib(n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 2) + fib(n - 1)

    print(f'{number} is {fib(number)}')


def fibs_nothreading():
    print_fib(40)
    print_fib(41)


start_time = time.time()

fibs_nothreading()

end_time = time.time()

print(f'Completed {end_time - start_time:.4f}')
