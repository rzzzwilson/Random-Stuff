What is this?
=============

Here we implement *parallel_ping()* in the simplest parallel way possible,
with one thread for each host, no limits.

This approach is fine for a small number of hosts, but has problems with
a large number of hosts.

Results
-------

When we execute the program, we get:

    $ time python3 parallel_ping.py
    127.0.0.1        127.0.0.1                               Host is up (0.0144s)
                     no_such_site.xyz                        DNS failure (0.0303s)
    8.8.4.4          8.8.4.4                                 Host is up (0.0484s)
    8.8.8.8          8.8.8.8                                 Host is up (0.0574s)
    146.88.60.59     google.com                              Host is up (0.0807s)
    93.184.216.34    example.com                             Host is up (0.2269s)
    127.1.1.1        127.1.1.1                               Timeout (5.0154s)
    
    real   0m5.104s
    user   0m0.095s
    sys    0m0.039s

This shows that we are executing the pings in parallel and that the *total*
runtime is roughly the time it takes todo the slowest ping.
