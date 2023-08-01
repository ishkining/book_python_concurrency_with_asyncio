import threading
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


def fibs_with_threads():
    fortieth_thread = threading.Thread(target=print_fib, args=(40,))
    forty_first_thread = threading.Thread(target=print_fib, args=(41,))

    fortieth_thread.start()
    forty_first_thread.start()

    fortieth_thread.join()
    forty_first_thread.join()


start_time = time.time()

fibs_with_threads()

end_time = time.time()

print(f'Completed {end_time - start_time:.4f}')
