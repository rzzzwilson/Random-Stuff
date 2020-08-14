I wrote the original code a long time ago for a small talk I gave on recursion.
That's the *binary_tree.py* and *hanoi.py* files.

More recently I started to investigate the relative speeds of various
implementations of a Fibonacci function:

+-------------------------+-------------------------------------------------------------+
| File                    | Implementation                                              |
+=========================+=============================================================+
|fibonacci_naive.py       | A naive, simple implementation                              |
+-------------------------+-------------------------------------------------------------+
|fibonacci_memo_global.py | Using a global dictionary to memoize the function           |
+-------------------------+-------------------------------------------------------------+
|fibonacci_memo_param.py  | Using a local (parameter)dictionary to memoize the function |
+-------------------------+-------------------------------------------------------------+
|fibonacci_tail.py        | Using tail recursion                                        |
+-------------------------+-------------------------------------------------------------+
|fibonacci_iter.py        | An iterative implementation to test against                 |
+-------------------------+-------------------------------------------------------------+

The *test_fib.py* file runs all Fibonacci implementations for the number given
and lists the results and relative performances.  The python files are run via
the *subprocess* module and the time is reported by the module itself::

    $ python3 test_fib.py 40
     FILE                     |  RUNTIME    | RESULTS
    --------------------------+-------------+--------------------------------
     fibonacci_iter.py        |  0.0000079s | this is the fastest
     fibonacci_tail.py        |  0.0000160s |        2.0 times slower
     fibonacci_memo_param.py  |  0.0000281s |        3.6 times slower
     fibonacci_memo_global.py |  0.0000329s |        4.2 times slower
     fibonacci_naive.py       | 67.9198227s |  8597445.9 times slower

The *test_fib_import.py* file runs all the implementations by importing them
and calling the *fibonacci()* function directly with timing done by the calling
code.  This was done to see if there is any difference in times.
The results are:

    $ python3 test_fib2.py 40
     FILE                  |  RUNTIME    | RESULTS
    -----------------------+-------------+--------------------------------
     fibonacci_iter        |  0.0000119s | this is the fastest
     fibonacci_memo_global |  0.0000339s |        2.8 times slower
     fibonacci_memo_param  |  0.0000389s |        3.3 times slower
     fibonacci_tail        |  0.0000412s |        3.5 times slower
     fibonacci_naive       | 68.4674668s |  5743467.4 times slower

It appears the "import and run direct" approach is slower overall, but the
"tail" and "memo*" times are swapped?
