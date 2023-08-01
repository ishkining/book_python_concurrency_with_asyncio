import time
import requests
import threading


def read_example() -> None:
    response = requests.get('https://www.example.com')
    print(response.status_code)


thread_1 = threading.Thread(target=read_example)
thread_2 = threading.Thread(target=read_example)

sync_start = time.time()

thread_1.start()
thread_2.start()

print('they are running')

thread_1.join()
thread_2.join()

sync_end = time.time()

print(f'Sync time {sync_end - sync_start:.4f}')