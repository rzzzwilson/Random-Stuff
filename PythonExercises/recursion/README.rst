I wrote the original code a long time ago for a small talk I gave on recursion.
That's the *binary_tree.py* and *hanoi.py* files.

More recently I started to investigate the relative speeds of various
implementations of a Fibonacci function:

-------------------+-------------------------------------------------------
 File              | Implementation
===================+=======================================================
fibonacci_naive.py | A naive, simple implementation
-------------------+-------------------------------------------------------
fibonacci_memo.py  | Using a dictionary to memoize the function
-------------------+-------------------------------------------------------
fibonacci_tail.py  | Using tail recursion
-------------------+-------------------------------------------------------
fibonacci_iter.py  | An iterative implementation to test against
-------------------+-------------------------------------------------------

The *test_fib.py* file runs all Fibonacci implementations for number given
and lists the results and relative performances::

    $ python3 test_fib.py 40
     FILE              |  RUNTIME   | RESULTS
    -------------------+------------+--------------------------------
     fibonacci_iter.py |  0.000007s | this is the fastest
     fibonacci_tail.py |  0.000024s |        3.3 times slower
     fibonacci_memo.py |  0.000034s |        4.7 times slower
     fibonacci.py      | 70.091387s |  9734914.8 times slower
