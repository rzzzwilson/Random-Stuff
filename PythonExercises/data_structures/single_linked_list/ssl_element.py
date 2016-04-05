#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Procedural implementation of a singly-linked list.

We say 'procedural' above as the code **is** procedural.  We use a class only
to store the 'value' and 'next' data.
"""

######
# Define an element object holding a value and a reference to the next element.
######

class SSL(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return '<SSL: .value=%s, .next=%s>' % (str(self.value), str(self.next))

######
# Functions to manipulate an SSL.
######

def _find_last(ssl):
    """Internal function to find last element in an SSL.

    Returns a reference to the last element in the given SSL.
    Returns None if the SSL is empty.
    """

    if ssl is None:
        return None
    while ssl.next is not None:
        ssl = ssl.next
    return ssl

def length(ssl):
    """Return the count of elements in 'ssl'."""

    count = 0

    while ssl is not None:
        count += 1
        ssl = ssl.next

    return count

def add_front(ssl, value):
    """Add a new element containing 'value' at the front of an SSL.
    
    Returns a reference to the new head of the SSL.
    """

    new_ssl = SSL(value, ssl)
    return new_ssl

def add_end(ssl, value):
    """Add a new element containing 'value' at the end of an SSL.
    
     Returns a reference to the head of the SSL.
     Just to be the same as add_front().
     """

    # find last element of the SSL
    last = _find_last(ssl)
    if last is None:
        # SSL is empty
        return SSL(value)

    # add new element to end
    last.next = SSL(value)
    return ssl

def find(ssl, val):
    """Find element value 'val' in an SSL.

    ssl   the SSL to search in
    val   the element value to find

    Returns a reference to the element containing 'val'.  Return None if
    not found.

    The SSL is not assumed to be sorted.
    """

    while ssl is not None:
        if ssl.value == val:
            return ssl
        ssl = ssl.next

    return None

def add_after(ssl, find_value, value):
    """Add an element containing 'value' after the element containing 'find_value'.
  
    Return a reference to the found element.
    If the element containing 'find_value' is not found, return None.

    Adds after the first element found, not any subsequent elements with the
    same value.
    """

    f = find(ssl, find_value)
    if f is not None:
        f.next = SSL(value, f.next)
        return f
    return None

def remove(ssl, find_value):
    """Find and remove element with value 'find_value' in an SSL.

    ssl   the SSL to search in
    find_value  the element value to find and remove

    Returns a reference to the possibly modified SSL.  This may be different
    from the original 'ssl' reference as the first element may be removed.
    """

    # a reference to the previous element before the 'ssl' element
    last = None
    scan = ssl

    while scan is not None:
        if scan.value == find_value:
            if last is None:
                # found at the first element
                return scan.next
            # found within SSL, remove & return original 'ssl'
            last.next = scan.next
            return ssl
        last = scan
        scan = scan.next

    return ssl

def remove_first(ssl):
    """Remove the first element of an SSL.
    
    Return the new SSL head reference.
    """

    # if SSL is empty, do nothing
    if ssl is None:
        return None

    # return reference to second element reference
    return ssl.next

def remove_last(ssl):
    """Remove the last element of an SSL.
    
    Returns a reference to the modified SSL.  Note that SSL may only
    contain one element to begin with.
    """

    # find last and second-last elements in SSL
    prev = None
    scan = ssl

    while scan is not None:
        if scan.next is None:
            if prev is None:
                # only one element in SSL
                return None
            # remove last element & return original 'ssl'
            prev.next = None
            return ssl
        prev = scan
        scan = scan.next

def __str__(ssl):
    """Convert an SSL into a 'list' string representation."""

    result = []

    while ssl is not None:
        result.append(ssl.value)
        ssl = ssl.next

    return str(result)
