#!/bin/env python
# -*- coding: utf-8 -*-

"""
This is a program to solve the Google Code Jam "Big City Skyline" puzzle:
    http://static.googleusercontent.com/media/services.google.com/en//blog_resources/Google_CodeJam_Practice.pdf

Usage: big_city_skyline <input_file>
"""

def build_city(width_height):
    """Solve the Big City Skyline problem.

    width_height  a list of (width, height) tuples

    Return the area of the largest block.
    """

    print('build_city: width_height=%s' % str(width_height))

    return 0

def main(input_file):
    """Solve the Big City Skyline problem.

    input_file  the input data file

    The solution is written to standard output:
        y
    where y is the area of the largest possible block.

    Note that the problem statement specifies that the number of buildings N
    is on the first line and the N width/height pairs occupy the second line.
    Because python makes this easy, we allow newlines anywhere in the input
    except within a number.
    """
    
    # read file into memory, removing trailing '\n'
    with open(input_file, 'rb') as handle:
        l = handle.readlines()
    lines = [ll.strip() for ll in l]

    # split data on space, convert to ints
    numbers = []
    for l in lines:
        l = l.strip()
        n = l.split()
        numbers.extend(n)

    numbers = [int(x) for x in numbers]

    # gather into final form: N and [(W1,H1),...,(Wn,Hn)]
    N = int(numbers[0])
    numbers = numbers[1:]
    if len(numbers) != 2*N:
        print('ERROR: width+height numbers list is wrong length')
        sys.exit(10)
    width_height = zip(numbers[0::2], numbers[1::2])

    result = build_city(width_height)

    print('%d' % result)
#    print('-'*80)

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

