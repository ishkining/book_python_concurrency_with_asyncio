## My notes

### 2 day

Think of a __coroutine__ like a regular Python function but with the superpower that it
can pause its execution when it encounters an operation that could take a while to
complete.

The _async_ keyword will let us define a coroutine; the _await_ keyword will 
let us pause our coroutine when we have a long-running operation.

Using the __await__ keyword will cause the coroutine following it to be run, unlike
calling a coroutine directly, which produces a coroutine object.

Generally, this means the first time we hit an _await_ statement after creating
a task, any tasks that are pending will run as _await_ triggers an iteration of the event
loop







