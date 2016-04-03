#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Procedural implementation of a singly-linked list.

We say 'procedural' above as the code **is** procedural.  We use a class only
to represent an element.
"""


class SSL(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def length(ssl):
    """Return the count of elements in 'ssl'."""

    count = 0

    while ssl is not None:
        count += 1
        ssl = ssl.next

    return count

def find(ssl, find):
    """Find element value 'find' in an SSL.

    ssl   the SSL to search in
    find  the element value to find

    Returns a reference to the element containing 'find'.  Return None if
    not found.
    """

    while ssl is not None:
        if ssl.value == find:
            return ssl
        ssl = ssl.next

    return None

def ssl_remove(ssl, find):
    """Find and remove element with value 'find' in an SSL.

    ssl   the SSL to search in
    find  the element value to find and remove

    Returns a reference to the removed element containing 'find'.  Returns None
    if not found.
    """

    # a reference to the previous element before the 'ssl' element
    last = None

    while ssl is not None:
        if ssl.value == find:
            if last is not None:
                last.next = ssl
            else:

            return
        last = ssl
        ssl = ssl.next

    return None

def __str__(ssl):
    """Convert an SSL into a 'list' string."""

    result = []

    while ssl is not None:
        result.append(ssl.value)
        ssl = ssl.next
    result.reverse()

    return str(result)
