"""
Read in a file with any type of newline (\\n, \\r, \\r\\n)
and write out a file with newlines standard for this platform.

Usage: convert.py <input_file> <output_file>
"""

import sys


if len(sys.argv) != 3:
    print(__doc__)
    sys.exit(1)

in_file = sys.argv[1]
out_file = sys.argv[2]

with open(in_file, 'r') as f_in, open(out_file, 'w') as f_out:
    f_out.write(f_in.read())
