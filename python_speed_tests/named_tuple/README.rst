Test relative speed of unpacking a tuple versus unpacking a namedtuple,
that is::

    (a, b, c, d, e, f, g) = my_tuple

against::

    a = my_named_tuple.a
    b = my_named_tuple.b
    c = my_named_tuple.c
    d = my_named_tuple.d
    e = my_named_tuple.e
    f = my_named_tuple.f
    g = my_named_tuple.g

As an extra test, compare the full tuple unpacking against::

    b = my_named_tuple.b

Summary
-------

Running the test gets results like::

    Using Python 2.7.11 on Darwin-15.6.0-x86_64-i386-64bit
    For 10000000 concatenations:
                tuple:  1.69s
           namedtuple: 31.00s
    namedtuple single:  1.64s

This shows that complete tuple unpacking is a lot faster than complete
namedtuple unpacking.  This is not really surprising.

Pulling one element out of a namedtuple is about as fast as complete tuple
unpacking.

The takeaway is that if you want speed in handling **all** of a bundled data
structure you should use a simple tuple.  However if you only want access to
one or two elements you could use a namedtuple and get the readability.

Using a simple tuple for speed is at the heart of **pySlip**, but the user
shouldn't have to see such ugliness!
