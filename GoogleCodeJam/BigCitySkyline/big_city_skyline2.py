#!/bin/env python
# -*- coding: utf-8 -*-

"""
This is a program to solve the Google Code Jam "Big City Skyline" puzzle:
    http://static.googleusercontent.com/media/services.google.com/en//blog_resources/Google_CodeJam_Practice.pdf

Usage: big_city_skyline [-d] <input_file>

where the -d option turns on debugging prints.

This version uses a dictionary open_blocks = {<height>: start_column, ...}.
"""

import copy


# global flag - debug prints if True
Debug = False


def log(msg):
    """Print message if allowed."""

    if Debug:
        print(msg)


def build_city(width_height):
    """Solve the Big City Skyline problem.

    width_height  a list of (width, height) tuples

    Return the area of the largest block.
    """

    log('build_city: width_height=%s' % str(width_height))

    # a dict holding all open blocks
    open_blocks = {}

    # the area of the biggest closed block
    closed_area = None

    # height of last buiding added
    last_height = None

    # current column number
    current_column = 0

    for (w, h) in width_height:
        log('############# Adding block: width=%d, height=%d, current_column=%d' % (w, h, current_column))
        if last_height is None:
            log('First block')
            # first building, initialize
            open_blocks[h] = 0
            last_height = h
            current_column = w
        else:
            if h > last_height:
                log('Bigger height block')
                # start a new open block
                open_blocks[h] = current_column
                # extend all open blocks (nothing to do)
                # update state
                last_height = h
                current_column += w
            elif h == last_height:
                log('Same height block')
                # extend all open blocks (nothing to do)
                # update state
                last_height = h
                current_column += w
            else:       # h < last_height
                log('Smaller height block')
                # close open blocks > h, remember largest
                # as we can't modify dict 'open_blocks' during the loop
                delete = []     # remember height of entries to delete
                update = {}     # remember updates to the dictionary

                # step through dict, handling blocks higher than newest building
                for (bh, sc) in open_blocks.iteritems():
                    log('1. looking at block: bh=%s, sc=%d' % (bh, sc))
                    if bh > h:
                        log('1. closing block: bh=%s, sc=%d' % (bh, sc))
                        area = (current_column - sc) * bh
                        delete.append(bh)
                        if closed_area is None or closed_area < area:
                            closed_area = area 
                            log('1. Becomes new closed_area: %s' % str(closed_area))
                        # lower blocks, only keep longest (smallest start_column)
                        if h > 0:
                            if h in update:
                                if  sc < update[h]:
                                    update[h] = sc
                            else:
                                update[h] = sc

                # now delete dict entries we want to forget
                log('deleting in open_blocks: %s' % str(delete))
                for bh in delete:
                    del open_blocks[bh]

                # and add new entries
                log('updating in open_blocks: %s' % str(update))
                open_blocks.update(update)

                log('1. after closing: closed_area=%d' % closed_area)

                # update state
                last_height = h
                current_column += w

        log('After:\tcurrent_column=%d\n\topen_blocks: %s\n\tclosed_area: %s'
              % (current_column, str(open_blocks), str(closed_area)))

    # return area of largest block
    result = closed_area
    for (bh, sc) in open_blocks.iteritems():
        area = (current_column - sc) * bh
        if area > result:
            result = area

    return result


def main(input_file, debug=False):
    """Solve the Big City Skyline problem.

    input_file  the input data file
    debug       True if debugging prints happen

    The solution is written to standard output:
        y
    where y is the area of the largest possible block.

    Note that the problem statement specifies that the number of buildings N
    is on the first line and the N width/height pairs occupy the second line.
    Because python makes this easy, we allow newlines anywhere in the input
    except within a number.
    """

    global Debug
    Debug = debug
    
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

    return build_city(width_height)

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
        (opts, args) = getopt.getopt(argv, 'dh', ['debug', 'help'])
    except getopt.error:
        usage()
        sys.exit(1)

    debug = False

    for (opt, param) in opts:
        if opt in ['-h', '--help']:
            usage()
            sys.exit(0)
        elif opt in ['-d', '--debug']:
            debug = True

    # check for the input file
    if len(args) != 1:
        usage()
        sys.exit(1)
    input_file = args[0]

    # run the program code
    result = main(input_file, debug)
    print(str(result))
    sys.exit(0)

