#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tuple implementation of a singly-linked list.
"""


def length(ssl):
    """Return the count of elements in 'ssl'."""

    count = 0

    while ssl is not None:
        count += 1
        ssl = ssl[1]

    return count

def add_prefix(ssl, value):
    """Add an element containing 'value' to the front of the SSL."""

    return (value, ssl)

def add_suffix(ssl, value):
    """Add an element containing 'value' to the end of the SSL."""

    if self.ssl is None:
        # list is empty, add at front
        self.ssl = element(value)
    else:
        scan = self.ssl
        while scan.next is not None:
            scan = scan.next
        scan.next = element(value)

def find(ssl, find):
    """Find element value 'find' in an SSL.

    ssl   the SSL to search in
    find  the element value to find

    Returns a reference to the element containing 'find'.  Return None if
    not found.
    """

    while ssl is not None:
        if ssl[0] == find:
            return ssl
        ssl = ssl[1]

    return None

def remove(ssl, find):
    """Find and remove element with value 'find' in an SSL.

    ssl   the SSL to search in
    find  the element value to find and remove

    Returns a reference to the removed element containing 'find'.  Returns None
    if not found.
    """

    # a reference to the previous element before the 'ssl' element
    last = None

    while ssl is not None:
        if ssl[0] == find:
            if last is not None:
                last[1] = ssl
            else:

            return
        last = ssl
        ssl = ssl[0]

    return None

def __str__(ssl):
    """Convert an SSL into a 'list' string."""

    result = []

    while ssl is not None:
        result.append(ssl[0])
        ssl = ssl[1]
    result.reverse()

    return str(result)
