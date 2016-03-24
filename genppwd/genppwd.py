#!/bin/env python
# -*- coding: utf-8 -*-

"""
This is a program to generate pronouncable passwords.

Usage:  genppwd [-h] [-l <length>] [-n] [-u]

where -h           prints help and the stops,
      -l <length>  generates a password of length <length>
                   (the default length is 14 characters)i
      -n           randomly convert some alphabetics to numerics,
      -u           randomly uppercase some letters.

The password is prnted to standard output.
"""

import random


# default password length
DefaultLength = 14

# allowable vowels and consonants
Vowels = 'aeiou'
Consonants = 'bdfghklmnprstvwyz'

def pwgen():
    """a generator that creates consonant+vowel... output."""

    while True:
        yield random.choice(Consonants) + random.choice(Vowels)

def main(length, numbers, upper):
    """Generate a pronouncable password."""

    pw = ''
    pwgen_series = pwgen()
    while len(pw) < length:
        pw += pwgen_series.next()

    print(pw[:length])

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
        log(msg)
        tkinter_error(msg)
        sys.exit(1)

    # plug our handler into the python system
    sys.excepthook = excepthook

    # parse the CLI params
    argv = sys.argv[1:]

    try:
        (opts, args) = getopt.getopt(argv, 'hl:nu', ['help', '--length=',
                                                     '--numbers', '--upper'])
    except getopt.error:
        usage()
        sys.exit(1)

    length = DefaultLength
    numbers = False
    upper = False

    for (opt, param) in opts:
        if opt in ['-h', '--help']:
            usage()
            sys.exit(0)
        elif opt in ['-l', '--length']:
            try:
                length = int(param)
            except ValueError:
                usage("'-l' option expects a numeric length, got '%s'" % str(param))
                sys.exit(1)
        elif opt in ['-n', '--numbers']:
            numbers = True
        elif opt in ['-u', '--upper']:
            upper = True


    # run the program code
    result = main(length, numbers, upper)
    sys.exit(result)

