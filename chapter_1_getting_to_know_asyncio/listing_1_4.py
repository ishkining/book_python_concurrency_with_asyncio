import multiprocessing
import os


def hello():
    print(f'ID: {os.getpid()}')


if __name__ == '__main__':
    hello_process = multiprocessing.Process(target=hello)
    hello_process.start()
    print(f'parend id: {os.getpid()}')

    hello_process.join()


