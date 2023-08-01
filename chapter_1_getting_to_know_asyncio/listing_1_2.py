import os
import threading

print(os.getpid())

total_threads =threading.active_count()
thread_name = threading.current_thread().name

print(total_threads)
print(thread_name)