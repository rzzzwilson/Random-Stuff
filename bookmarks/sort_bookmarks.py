#!/usr/bin/env python3

"""
Sort a bookmarks data file.

Usage: sort_bookmarks.py <data file> <sorted file>

where <data file>    is the bookmarks data file to sort
where <sorted file>  is the path to the sorted output bookmark data file

If the <sorted file> already exists the program will abort.
"""

import sys
import os
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

if len(args) != 2:
    usage()
    sys.exit(1)

input_file = args[0]
sorted_file = args[1]

# check that the output file doesn't exist
if os.path.isfile(sorted_file) or os.path.isdir(sorted_file):
    print(f"Sorry, output file '{sorted_file}' already exists, aborting.")
    sys.exit(1)

# read the input data file
with open(input_file, 'r') as fd:
    lines = fd.readlines()

# sort the data
data = [l.strip().split('\t') for l in lines]
data.sort()

# write the sorted data to the output file
with open(sorted_file, 'w') as fd:
    for d in data:
        fd.write('\t'.join(d) + '\n')

