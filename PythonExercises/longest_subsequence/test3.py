#!/usr/bin/env python

"""
Code to take a string and print the longest sub-sequence
that is in alphabetical order.
"""

def longest(s):
    prev = None
    for (i, c) in enumerate(s):
        if prev and c < prev:
            head = s[:i]
            tail = s[i:]
            longest_tail = longest(tail)
            return head if len(head) > len(longest_tail) else longest_tail
        prev = c
    return s


s = 'azcbobobegghakl'
print('%s->%s' % (s, longest(s)))

s = 'khdieuryfpbieuypbdfjlruuuuufvoidufvnodubeoriuybvspuybrpuyvbor'
print('%s->%s' % (s, longest(s)))
