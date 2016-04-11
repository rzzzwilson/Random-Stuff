#!/bin/env python
# -*- coding: utf-8 -*-

"""
This is a program to solve the Google Code Jam "Rope Intranet" puzzle:
    https://code.google.com/codejam/contest/619102/dashboard#s=p0

Usage: rope_intranet <input_file>
"""

def count_one_intersections(rope, others):
    """Count intersections of 'rope' with 'others'.

    rope    a tuple (Ai, Bi) defining a rope of interest
    others  a list of tuples defining the other ropes

    Returns the count of intersections.
    """

#    (Ai < Bj) and (Bi > Aj)                     # relation 1
#    (Ai > Aj) and (Bi < Bj)                     # relation 2
#    (Ai < Aj) and (Bi > Bj)                     # relation 3

    print('rope=%s, others=%s' % (str(rope), str(others)))

    (Ai, Bi) = rope
    for (Aj, Bj) in others:
        print('Ai=%d, Bi=%d, Aj=%d, Bj=%d' % (Ai, Bi, Aj, Bj))
        if (Ai < Bj) and (Bi > Aj):
            print('(Ai < Bj) and (Bi > Aj)')
            return 1
        if (Ai > Aj) and (Bi < Bj):
            print('(Ai > Aj) and (Bi < Bj)')
            return 1
        if (Ai < Aj) and (Bi > Bj):
            print('(Ai < Aj) and (Bi > Bj)')
            return 1

    return 0

def get_intersections(rope_set):
    """Calculate number of intersections in rope set.

    rope_set  list of rope windows: [(A1,B1), ..., (An,Bn)]
              which is a collection of left/right window numbers

    Returns an integer which is the number of rope intersections.
    """

    print('rope_set=%s' % str(rope_set))

    intersections = 0

    for index in range(len(rope_set)):
        rope = rope_set[index]
        others = rope_set[index+1:]
        intersections += count_one_intersections(rope, others)

    return intersections

def main(input_file):
    """Solve the Rope Intranet problem.

    input_file  the input data file

    The solution is written to standard output:
        Case #x: y
    where x is the case number, and
          y is the number of intersection points (you see).
    """
    
    # read file into memory, removing trailing '\n'
    with open(input_file, 'rb') as handle:
        l = handle.readlines()
    lines = [ll.strip() for ll in l]

    # gather each test case, solve
    num_cases = int(lines[0])
    lines = lines[1:]
    for case in range(num_cases):
        num_ropes = int(lines[0])
        lines = lines[1:]
        ropes = lines[:num_ropes]
        lines = lines[num_ropes:]
        rope_set = []
        for rope in ropes:
            (a, b) = rope.split()
            a = int(a)
            b = int(b)
            rope_set.append((a, b))
        intersections = get_intersections(rope_set)

        print('Case #%d: %d' % (case, intersections))

    return 0

##############################################################################

if __name__ == '__main__':
    import sys
    import getopt
    import traceback

    # to help the befuddled user
    def usage(msg=None):
        if msg:
            print(('*'*80 + '\n%s\n' + '*'*80) % msg)
        print(__doc__)

    # our own handler for uncaught exceptions
    def excepthook(type, value, tb):
        msg = '\n' + '=' * 80
        msg += '\nUncaught exception:\n'
        msg += ''.join(traceback.format_exception(type, value, tb))
        msg += '=' * 80 + '\n'
        print(msg)
        sys.exit(1)

    # plug our handler into the python system
    sys.excepthook = excepthook

    # parse the CLI params
    argv = sys.argv[1:]

    try:
        (opts, args) = getopt.getopt(argv, 'h', ['help'])
    except getopt.error:
        usage()
        sys.exit(1)

    for (opt, param) in opts:
        if opt in ['-h', '--help']:
            usage()
            sys.exit(0)

    # check for the input file
    if len(args) != 1:
        usage()
        sys.exit(1)
    input_file = args[0]

    # run the program code
    result = main(input_file)
    sys.exit(result)

