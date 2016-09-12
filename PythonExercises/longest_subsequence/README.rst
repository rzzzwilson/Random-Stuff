I lurk in `/r/learnpython <https://www.reddit.com/r/learnpython>`_ and I came
across `this <https://www.reddit.com/r/learnpython/comments/52a86k/write_a_program_that_prints_the_longest_substring/>`_
question:

::

    Write a program that prints the longest substring of s in which the letters occur in alphabetical order

The code here is my take on the problem.

test.py
-------

A very simple functional approach.  It's a little cryptic and inefficient -
but simple!

::

    def longest(s):
        prev = None
        for (i, c) in enumerate(s):
            if prev and c < prev:
                return s[:i] if len(s[:i]) > len(longest(s[i:])) else longest(s[i:])
            prev = c
        return s
    
    s = 'azcbobobegghakl'
    print('%s->%s' % (s, longest(s)))

test2.py
--------

A version of *test.py* that performs an explicit split into the **head** and
**tail** variables.  This makes that bit of the algorithm more clear.

But still inefficient, due to the multiple recursive calls.

::

    def longest(s):
        prev = None
        for (i, c) in enumerate(s):
            if prev and c < prev:
                head = s[:i]
                tail = s[i:]
                return head if len(head) > len(longest(tail)) else longest(tail)
            prev = c
        return s

test3.py
--------

Removed the multiple recursive call.  It's a lot faster, but not as clear as
required for /r/learnpython.

::

    def longest(s):
        prev = None
        for (i, c) in enumerate(s):
            if prev and c < prev:
                head = s[:i]
                tail = s[i:]
                longest_tail = longest(tail)
                return head if len(head) > len(longest_tail) else longest_tail
            prev = c
        return s
