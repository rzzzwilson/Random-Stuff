What is this?
=============

Here we implement *parallel_ping()* in the imost flexible  parallel way possible,
with pings performed by a *pool* with a fixed number of threads.

This approach is fine for a small number of hosts, but has problems with
a large number of hosts.

Results
-------

When we execute the program, we get:

    $ time python3 parallel_ping.py
                     no_such_site.xyz                        DNS failure (0.0209s)
    146.88.60.45     google.com                              Host is up (0.0279s)
    8.8.8.8          8.8.8.8                                 Host is up (0.0444s)
    8.8.4.4          8.8.4.4                                 Host is up (0.0454s)
    127.0.0.1        127.0.0.1                               Host is up (0.0106s)
    93.184.216.34    example.com                             Host is up (0.2289s)
    127.1.1.2        127.1.1.2                               Timeout (5.0149s)
    127.1.1.1        127.1.1.1                               Timeout (5.0109s)

    real   0m5.155s
    user   0m0.092s
    sys    0m0.036s

If we force the number of worker threads to be larger than the number of hosts, we see:

    $ time python3 parallel_ping.py -w 8
    127.0.0.1        127.0.0.1                               Host is up (0.0161s)
    146.88.60.45     google.com                              Host is up (0.0332s)
                     no_such_site.xyz                        DNS failure (0.0332s)
    8.8.8.8          8.8.8.8                                 Host is up (0.0507s)
    8.8.4.4          8.8.4.4                                 Host is up (0.0500s)
    93.184.216.34    example.com                             Host is up (0.2291s)
    127.1.1.2        127.1.1.2                               Timeout (5.0158s)
    127.1.1.1        127.1.1.1                               Timeout (5.0115s)

    real   0m5.103s
    user   0m0.100s
    sys    0m0.043s

This shows that we are executing the pings in parallel and that the *total*
runtime is roughly the time it takes todo the slowest ping.
