What is this mess?
==================

Here we have code for a *parallel ping* function.  The function is implemented
in various ways, from a naive non-parallel way through to fully parallel
implementations using threads.

The reason for this code was a conversation in this Reddit_ thread.

.. _Reddit: https://www.reddit.com/r/learnpython/comments/5fu9m5/ping_tool_gives_recursion_error/).

parallel_ping()
---------------

There will be a function to perform the ping operation.  It takes a list of
hosts, performs the pings in various ways, and returns a list of tuples, one
for each host, containing:

::

    (IP, hostname, result)

The function is called so:

::

    results = parallel_ping(hosts)
    # results: [(IP, hostname, result), ...]

where the *hosts* list will be a list of strings containing hostnames, either an
IP or a domain name.  The *result* string in the returned tuples will contain
either the ping time or some explanation of an error.

Directories
===========

The *parallel_ping()* function will be implemented in various ways.  Each
separate implementation will be in a separate module.  The module names and
the implementation within are:

=============== ========================================
 Module          Implementation
=============== ========================================
 naive           not parallel, one ping at a time
 massive         one thread for each host, no limit
 pool            a fixed number of threads
=============== ========================================
