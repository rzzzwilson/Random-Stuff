#!/usr/bin/env python

"""
Code to take a string and print the longest sub-sequence
that is in alphabetical order.
"""

def longest(s):
    prev = None
    for (i, c) in enumerate(s):
        if prev and c < prev:
            return s[:i] if len(s[:i]) > len(longest(s[i:])) else longest(s[i:])
        prev = c
    return s

if __name__ == '__main__':
    s = 'azcbobobegghakl'
    print('%s->%s' % (s, longest(s)))

    s = 'khdieuryfpbieuypbdfjlruuuuufvoidufvnodubeoriuybvspuybrpuyvbor'
    print('%s->%s' % (s, longest(s)))
