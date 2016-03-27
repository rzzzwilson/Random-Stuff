#!/bin/env python
# -*- coding: utf-8 -*-

"""
This is a program to create random data for the Google Code Jam "Big City Skyline" puzzle:
    http://static.googleusercontent.com/media/services.google.com/en//blog_resources/Google_CodeJam_Practice.pdf

Usage: make_data [-h <max_height>] [-w <max_width>] <number_buildings>

where <number_buildings> is the number of buildings in the generated dataset,
      <max_height>       is the maximum height of the buildings (default 99,999,999)
      <max_width>        is the maximum width of the buildings (default 999)

The generated data will be written to stdout.

Note, the generated building widths and heights will NOT be zero!
"""

import random


DefaultMaxWidth = 999
DefaultMaxHeight = 99999999

def main(n, width, height):
    """Generate random data for the Big City Skyline problem.

    n       the number of buildings to generate
    width   is the maximumm width of buildings
    height  is the maximum height of a building

    Returns the area of the biggest possible block.
    """

    print('%d' % n)
    for _ in range(n):
        print('%d %d'
              % (random.randrange(width-1)+1, random.randrange(height-1)+1))

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
    
    # parse the params
    argv = sys.argv[1:]
    
    try:
        (opts, args) = getopt.getopt(argv, 'h:w:', ['height=', 'width='])
    except getopt.error:
        usage()
        sys.exit(1)
    
    width = DefaultMaxWidth
    height = DefaultMaxHeight
    
    for (opt, param) in opts:
        if opt in ['-h', '--height']:
            try:
                height = int(param)
            except ValueError:
                usage("-h param '%s' is bad" % param)
                sys.exit(1)
        elif opt in ['-w', '--width']:
            try:
                width = int(param)
            except ValueError:
                usage("-w param '%s' is bad" % param)
                sys.exit(1)

    # get number of buildings
    if len(args) != 1:
        usage("The number of buildings is missing")
        sys.exit(1)

    try:
        n = int(args[0])
    except ValueError:
        usage("The number of buildings must be a number, got '%s'" % args[0])
        sys.exit(1)
    
    # run the program code
    main(n, width, height)
