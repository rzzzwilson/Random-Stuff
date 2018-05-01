"""
Test the regex approach.
"""

import re

pattern = '(?:(?:(?P<hours>\d\d?)?[:]?(?P<minutes>[0-5]?\d):)(?P<seconds>[0-5]\d)) (?P<duration>\d\d?)'
pat = re.compile(pattern)

with open('times.txt', 'r') as t:
    lines = t.read().strip().splitlines()

for (lnum, line) in enumerate(lines):
    match = re.search(pat, line)
    print(f"line='{line}, match={match}")
