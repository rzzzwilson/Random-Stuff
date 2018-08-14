#!/usr/bin/env python3

"""
Read data from multiple files in a zip file.

Just take the ZIP file we are given on the command line and list
all files in the ZIP file and then print the contents of each file.

Usage: zip_data1.py <zip_filename>
"""

import sys
import zipfile

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
print(f'Files in ZIP file {zip_file}:')

# print files in the ZIP file, along with contents of each
with zipfile.ZipFile(zip_file, 'r') as zf:
    help(zf)
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
