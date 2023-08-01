## My notes

### 1 day - 01.08 

____concurrency____ means allowing more than one task being handled at the same time.

When we say two tasks are happening __concurrently__, we mean those tasks are happening at the same time

PREEMPTIVE MULTITASKING. In this model, we let the operating system decide how to switch between which work is
currently being executed via a process called time slicing. When the operating system
switches between work, we call it preempting. 

COOPERATIVE MULTITASKING. In this model, instead of relying on the operating system to decide when to switch
between which work is currently being executed, we explicitly code points in our
application where we can let other tasks run.

Briefly, the ___GIL___ prevents one Python process from executing more than one Python bytecode instruction at any given time.

A coroutine can be thought of as executing a lightweight thread.

A __socket__ is a low-level abstraction for sending and receiving data over a network

### Summary
- CPU-bound work is work that primarily utilizes our computer’s processor whereas
I/O-bound work primarily utilizes our network or other input/output devices.
asyncio primarily helps us make I/O-bound work concurrent, but it exposes
APIs for making CPU-bound work concurrent as well.
- Processes and threads are the basic most units of concurrency at the operating
system level. Processes can be used for I/O and CPU-bound workloads and
threads can (usually) only be used to manage I/O-bound work effectively in
Python due to the GIL preventing code from executing in parallel.
- We’ve seen how, with non-blocking sockets, instead of stopping our application
while we wait for data to come in, we can instruct the operating system to tell us
when data has come in. Exploiting this is part of what allows asyncio to achieve
concurrency with only a single thread.
- We’ve introduced the event loop, which is the core of asyncio applications. The
event loop loops forever, looking for tasks with CPU-bound work to run while
also pausing tasks that are waiting for I/O.




