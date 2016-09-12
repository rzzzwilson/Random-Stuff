I lurk in `/r/learnpython`__ and I came acrosss `this`__ question:

::

    Write a program that prints the longest substring of s in which the letters occur in alphabetical order

.. /r/learnpython: https://www.reddit.com/r/learnpython

.. this: https://www.reddit.com/r/learnpython/comments/52a86k/write_a_program_that_prints_the_longest_substring/

The code here is my take on the problem.

test.py
-------

A very simple functional approach.  It's a little cryptic and inefficient -
but simple!

test2.py
--------

A version of *test.py* that performs an explicit split into the **head** and
**tail** variables.  This makes that bit of the algorithm more clear.

But still inefficient, due to the multiple recursive calls.

test3.py
--------

Removed the multiple recursive call.  It's a lot faster, but not as clear as
required for /r/learnpython.
