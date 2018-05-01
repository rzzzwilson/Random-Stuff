Code for:

https://www.reddit.com/r/learnpython/comments/7r8p76/help_with_coding_a_circular_queue/

Reply:

A couple of points that may make things easier for you.

First, you simplify your code a *lot* if you allocate all possible elements of
your list underneath the circular queue (CQ).  That means you should do:

    queue = []
    for _ in range(maxsize):
        queue.append(None)

It doesn't matter what you initialize the CQ value to - I used None above.

Second, you can't get the length of the CQ by `len(queue)`.  You have to do
arithmetic on your `rearP` and `frontP` values.  Worry about both cases,
where `rearP` is behind `frontP` and when it is in front.  For instance,
when you've added two items (1 and 2) and removed one from the CQ you have:

    +---+---+---+---+---+
    | 1 | 2 | _ | _ | _ |
    +---+---+---+---+---+
          ^   ^
     rear-+   +-front

and the CQ length is `frontP - rearP`.  What about this?

    +---+---+---+---+---+
    | 6 | 2 | 3 | 4 | 5 |
    +---+---+---+---+---+
          ^       ^
    front-+       +-rear

Finally, you use a global `queue` that your functions operate on.  Nothing
wrong with that in learning code, but in production code that means you can have only
one CQ in your program, which is a bit limiting.  Better to pass a reference to
the CQ list **and** the front/rear pointers.  Doing that is a pain and demonstrates
why the class approach is so much nicer!

Edit: spelling, formatting.
