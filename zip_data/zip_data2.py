#!/usr/bin/env python3

"""
Add a file to the given ZIP file and then read data from all files in a ZIP file.

Just take the ZIP file we are given on the command line, write a new file to it
and then print the contents of each file in the ZIP.

Usage: zip_data2.py <zip_filename>
"""

import sys
import zipfile
import io


# the new filename in the ZIP file
NewFilename = 'new_file.dat'

# the lines of text to write to the new file
Lines = ('From "Lays of Ancient Rome" by Macaulay:\n'
         'Then out spake brave Horatius,\n'
         'The Captain of the Gate:\n'
         '"To every man upon this earth\n'
         'Death cometh soon or late.\n'
         'And how can man die better\n'
         'Than facing fearful odds,\n'
         'For the ashes of his fathers,\n'
         'And the temples of his Gods."\n'
        )


def usage(msg=None):
    if msg:
        print('*' * 60)
        print(msg)
        print('*' * 60)
    print(__doc__)

# check we have the right number of args
if len(sys.argv) != 2:
    usage('Incorrect number of parameters!')
    sys.exit(1)

# get ZIP filename
zip_file = sys.argv[1]

# list files in the ZIP before adding
print(f'Before: files in ZIP file {zip_file}:')
with zipfile.ZipFile(zip_file, 'r') as zf:
    for fn in zf.namelist():
        print(f'    {fn}:')

# delete any possible file that has name of new file
# can't do that!?
# we have to create a new ZIP file and replace old file with new.

# add new file to the ZIP
with zipfile.ZipFile(zip_file, mode='a') as zf:
    print(f"\nAdding a new file '{NewFilename}'")
    zf.writestr(NewFilename, Lines, compress_type=None)

# list files in the ZIP after adding
print(f'\nAfter:  files in ZIP file {zip_file}:')
with zipfile.ZipFile(zip_file, 'r') as zf:
    for fn in zf.namelist():
        print(f'    {fn}:')

# print files in the ZIP file, along with contents of each
print(f"\nFiles in '{zip_file}' and their contents:")
with zipfile.ZipFile(zip_file, 'r') as zf:
    for fn in zf.namelist():
        print(f'    {fn}:')
        try:
            data = zf.read(fn).decode("utf-8")
        except KeyError:
            print(f'ERROR: Did not find {fn} in zip file {zip_file}')
        else:
            data_split = data.split('\n')
            for line in data_split:
                print(f'        {line}')

