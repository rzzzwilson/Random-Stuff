Test relative speed of:

::

    x = 2
    y = 3
    sq = (x + y) * (x + y)

against:

::

    x = 2
    y = 3
    sq = (x + y)**2

Also test for the simple cases, x*x and x**2

Results are:

::

    Using Python 2.7.11 on Darwin-15.3.0-x86_64-i386-64bit
    For 50000000 concatenations:
            x*x:  2.81s
           x**2:  4.07s
    (x+y)*(x+y):  5.12s
       (x+y)**2:  4.72s

While, in the simple case, **x*x** is quite a bit faster than **x**2**,
it's not so clear-cut in more complicated cases.  So no obvious conclusion,
except to profile real code when time is a concern.
