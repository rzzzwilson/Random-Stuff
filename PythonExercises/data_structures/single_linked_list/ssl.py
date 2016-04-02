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


def ssl_len(ssl):
    """Return the count of elements in list 'ssl'."""

    count = 0
    while ssl is not None:
        count += 1
        ssl = ssl.next
    return count

def ssl2list(ssl):
    """Convert an SSL into a list."""

    result = []
    while ssl is not None:
        result.append(ssl.value)
        ssl = ssl.next
    result.reverse()
    return result
