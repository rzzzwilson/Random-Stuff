stack_dump
==========

This is class used to dump the callback stack to stdout or a file-like
object.  It is used to understand the execution flow of a large body of
code.

Simple example
--------------

A simple usage that will dump the execution stack to stdout is::

    import stack_dump
    
    sd = stack_dump.StackDump()

    sd('A simple stack dump example')

If you want to capture the dump in a file you can do either of::

    # just supply a filename
    sd = stack_dump.StackDump('dump.out')

    # supply an open file
    fd = open('dump2.out', 'w')
    sd = stack_dump.StackDump(fd)

If you want to limit amount of stack information, do either of::

    # turn down the verbosity
    sd = stack_dump.StackDump('dump.out', verbose=False)

    # limit the stack depth that is dumped
    sd = stack_dump.StackDump('dump.out', depth=2)

It is possible to combine the two *verbose=* and *depth=* parameters.

TODO
====

Allow file-like objects.  Logging module?

Allow usage in multiple modules.
