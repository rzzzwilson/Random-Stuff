I wrote this code a long time ago for a small talk I gave on recursion.

Recent additions add tail call optimization and compares the run time
of each algorithm.  The output is::

    $ python3 test_fib.py 40
     FILE              |  RUNTIME   | RESULTS
    -------------------+------------+--------------------------------
     fibonacci_iter.py |  0.000007s | this is the fastest
     fibonacci_tail.py |  0.000024s |        3.3 times slower
     fibonacci_memo.py |  0.000034s |        4.7 times slower
     fibonacci.py      | 70.091387s |  9734914.8 times slower
