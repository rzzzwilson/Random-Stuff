"""
Simple example of using git-style command args.

Usage:  test.py <command> [<args>]

where <command> may be 'union', 'size' or 'help'
  and <args>    are any args required for the command
"""

import sys


def union_handler(args):
    print('union_handler() called, args=%s' % str(args))
    # parse and process args

def size_handler(args):
    print('size_handler() called, args=%s' % str(args))
    # parse and process args

def help_handler(args):
    print('help_handler() called, args=%s' % str(args))
    print(__doc__)
    # parse and process args

# the main code goes here
# 'args' is a list of arguments in the style of sys.argv
def main(args):
    print('main() called, args=%s' % str(args))

    if len(args) < 1:
        print(__doc__)
    else:
        command = args[0].lower()
        if command == 'union':
            union_handler(args[1:])
        elif command == 'size':
            size_handler(args[1:])
        elif command == 'help':
            help_handler(args[1:])
        else:
            print('Unrecognized command: %s' % args[0])
            print(__doc__)

# run the program code
main(sys.argv[1:])
