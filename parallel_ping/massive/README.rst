What is this?
=============

Here we implement *parallel_ping()* in the simplest parallel way possible,
with one thread for each host, no limits.

This approach is fine for a small number of hosts, but has problems with
a large number of hosts.

Results
-------

When we execute the program, we get:

::

    $ time python3 parallel_ping.py 
    127.0.0.1        127.0.0.1                               Host is up (0.0128s)
                     no_such_site.xyz                        DNS failure (0.0282s)
    8.8.8.8          8.8.8.8                                 Host is up (0.0499s)
    8.8.4.4          8.8.4.4                                 Host is up (0.0537s)
    146.88.60.52     google.com                              Host is up (0.0709s)
    93.184.216.34    example.com                             Host is up (0.2334s)
    127.1.1.2        127.1.1.2                               Timeout (5.0157s)
    127.1.1.1        127.1.1.1                               Timeout (5.0147s)

    real   0m5.111s
    user   0m0.103s
    sys    0m0.040s

This shows that we are executing the pings in parallel and that the *total*
runtime is roughly the time it takes todo the slowest ping.  The two slowest
pings are added last to the result queue.
