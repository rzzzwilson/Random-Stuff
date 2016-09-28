#!/usr/bin/env python

"""
Convert a results file:

    Using Python 2.7.12 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial
    For 50000000 concatenations:
            naive:  9.77s
             join: 11.53s
         stringio: 19.97s
    comprehension:  9.76s

into a GitHub-style RST table:

    Using Python 2.7.12 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial
    For 50000000 concatenations:

    +-------------+-------+
    | Method      | Time  |
    +=============+=======+
    |        naive|  9.77s|
    +-------------+-------+
    |         join| 11.53s|
    +-------------+-------+
    |     stringio| 19.97s|
    +-------------+-------+
    |comprehension|  9.76s|
    +-------------+-------+

Usage:  make_table.py <filename>

where <filename>  is the path to the results file.

The output is written to 'stdout'.
"""

import sys


def usage(msg=None):
    if msg:
        print('*'*60)
        print(msg)
        print('*'*60)
    print(__doc__)



def main(path):
    """Read a results file and output RST data."""

    # get all lines in file
    with open(path, 'r') as fd:
        lines = fd.readlines()

    # first two lines are just passed through, plus blank line
    print('| %s' % lines[0].strip())
    print('| %s' % lines[1].strip())
    print('')

    rest = lines[2:]

    # emit remaining lines in RST table form
    print('+---------------+--------+')
    print('| Method        | Time   |')
    print('+===============+========+')

    for l in rest:
        l = l.strip()
        (method, time) = l.split()
        method = method[:-1]
        method = method + ' '*20
        time = '      ' + time
        print('| %s | %s |' % (method[:13], time[-6:]))
        print('+---------------+--------+')


if len(sys.argv) != 2:
    usage()
else:
    path = sys.argv[1]
    main(path)
