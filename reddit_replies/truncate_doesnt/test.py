#!/usr/bin/env python

"""
Test that file.truncate() actually works.
"""

import sys
import os.path


filename = 'test.txt'

def dump_file(fname, msg):
    """Dump the text of a file."""

    print(msg)
    print 'file %s:' % fname,
    with open(fname, 'r') as f:
        print(f.read())

# make sure we don't destroy something important
if os.path.isfile(filename):
    print("Sorry, can't run since would overwrite existing file '%s'" % filename)
    sys.exit()

# create a file with some text in it
with open(filename, 'w') as f:
    f.write('ABCDEF')

dump_file(filename, 'Before truncate')

# try to truncate the file
openfile = open(filename, 'r+')
openfile.truncate(0)
#openfile.close()        # comment this out and the file is still truncated
#
#dump_file(filename, 'After truncate')
