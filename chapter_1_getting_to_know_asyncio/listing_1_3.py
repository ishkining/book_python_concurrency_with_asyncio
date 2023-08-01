import threading


def hello():
    print(f'Current thread is {threading.current_thread()}')

hello_thread = threading.Thread(target=hello)
hello_thread.start()

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(total_threads)
print(thread_name)

hello_thread.join()