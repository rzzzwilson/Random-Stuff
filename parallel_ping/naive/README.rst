What is this?
=============

Here we implement *parallel_ping()* in the simplest way possible without
any parallelism at all.  One ping at a time and wait for the response.

This is just to get the basics of pinging settled, and to compare with a
parallel solution.

When we run the program, we see:

::

    $ time python3 parallel_ping.py
    146.88.60.39     google.com                              Host is up (0.0307s)
    127.1.1.2        127.1.1.2                               No response (5.0110s)
    93.184.216.34    example.com                             Host is up (0.2962s)
                     no_such_site.xyz                        DNS failure (0.0205s)
    8.8.8.8          8.8.8.8                                 Host is up (0.0443s)
    8.8.4.4          8.8.4.4                                 Host is up (0.0461s)
    127.0.0.1        127.0.0.1                               Host is up (0.0085s)
    127.1.1.1        127.1.1.1                               No response (5.0129s)

    real   0m10.540s
    user   0m0.090s
    sys    0m0.033s

Note that since we have two IP addresses that are unresponsive, they will timeout
and the entire operation takes over 10 seconds.
