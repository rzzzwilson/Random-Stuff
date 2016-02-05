Test relative speed of:

::

    value = 1
    if flag:
        value = 2

against:

::

    value = 2 if flag else 1

The three line version is quicker, though not by much:

::

    Using Python 2.7.11 on Darwin-15.3.0-x86_64-i386-64bit for 100000000 operations
    if     took 10.37s
    ifelse took 10.47s

I'll probably stick to the three line version as I think it's more readable.

