I recently viewed a video posted to Reddit /r/learnpython subreddit:
https://www.reddit.com/r/learnpython/comments/7x8kxv/discussing_and_implementing_a_stack_in_python/ .
The video was sort of OK, but implemented stacks in a non-pythonic
way - OK for beginners but I though a *real* python programmer would
use a stack.  So I thought I would have a go.

The video implemented a stack class with these methods:

- stack.isEmpty() -> boolean
- x = stack.peek() -> show next object to be popped
- x = stack.pop() -> pop object "x" from top of stack
- stack.push(x) -> push object "x" onto stack
- size = stack.size() -> get number of objects in the stack

The basic idea is that a python *list* is **already** a stack::

    x = list.pop() == x = stack.pop()
    list.append(x) == stack.push(x)

So our *stack* class will inherit from *list*.
