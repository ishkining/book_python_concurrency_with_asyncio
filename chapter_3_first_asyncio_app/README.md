## My notes

### 08.08.2023 16:42

Nothing to say

### 08.08.2023 18:44

### Summary

- We’ve learned how to create simple applications with blocking sockets. Blocking sockets will stop the entire thread when they are waiting for data. This prevents us from achieving concurrency because we can get data from only one
client at a time.
- We’ve learned how to build applications with non-blocking sockets. These sockets will always return right away, either with data because we have it ready, or
with an exception stating we have no data. These sockets let us achieve concurrency because their methods never block and return instantly.
- We’ve learned how to use the selectors module to listen for events on sockets in
an efficient manner. This library lets us register sockets we want to track and will
tell us when a non-blocking socket is ready with data.
- If we put select in an infinite loop, we’ve replicated the core of what the asyncio
event loop does. We register sockets we are interested in, and we loop forever,
running any code we want once a socket has data available to act on.
- We learned how to use asyncio’s event loop methods to build applications
with non-blocking sockets. These methods take in a socket and return a
coroutine which we can then use this in an await expression. This will suspend our parent coroutine until the socket has data. Under the hood, this is
using the selectors library.
- We’ve seen how to use tasks to achieve concurrency for an asyncio-based echo
server with multiple clients sending and receiving data at the same time. We’ve
also examined how to handle errors within those tasks.
- We’ve learned how to add custom shutdown logic to an asyncio application. In
our case, we decided that when our server shuts down, we’d give it a few seconds for any remaining clients to finish sending data. Using this knowledge, we
can add any logic our application needs when it is shutting down.
