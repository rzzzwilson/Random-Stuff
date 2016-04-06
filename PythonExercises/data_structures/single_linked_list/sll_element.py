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

class SLL(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return '<SLL: .value=%s, .next=%s>' % (str(self.value), str(self.next))

######
# Functions to manipulate an SLL.
######

def _find_last(sll):
    """Internal function to find last element in an SLL.

    Returns a reference to the last element in the given SLL.
    Returns None if the SLL is empty.
    """

    if sll is None:
        return None
    while sll.next is not None:
        sll = sll.next
    return sll

def length(sll):
    """Return the count of elements in 'sll'."""

    count = 0

    while sll is not None:
        count += 1
        sll = sll.next

    return count

def add_front(sll, value):
    """Add a new element containing 'value' at the front of an SLL.
    
    Returns a reference to the new head of the SLL.
    """

    return SLL(value, sll)

def add_end(sll, value):
    """Add a new element containing 'value' at the end of an SLL.
    
     Returns a reference to the head of the SLL.
     Just to be the same as add_front().
     """

    # find last element of the SLL
    last = _find_last(sll)
    if last is None:
        # SLL is empty
        return SLL(value)

    # add new element to end
    last.next = SLL(value)
    return sll

def find(sll, val):
    """Find element value 'val' in an SLL.

    sll   the SLL to search in
    val   the element value to find

    Returns a reference to the element containing 'val'.  Return None if
    not found.

    The SLL is not assumed to be sorted.
    """

    while sll is not None:
        if sll.value == val:
            return sll
        sll = sll.next

    return None

def add_after(sll, find_value, value):
    """Add an element containing 'value' after the element containing 'find_value'.
  
    Return a reference to the found element.
    If the element containing 'find_value' is not found, return None.

    Adds after the first element found, not any subsequent elements with the
    same value.
    """

    f = find(sll, find_value)
    if f is not None:
        f.next = SLL(value, f.next)
        return sll
    return None

def remove(sll, find_value):
    """Find and remove element with value 'find_value' in an SLL.

    sll         the SLL to search in
    find_value  the element value to find and remove

    Returns a reference to the possibly modified SLL.  This may be different
    from the original 'sll' reference as the first element may be removed.
    """

    # a reference to the previous element before the 'sll' element
    last = None
    scan = sll

    while scan is not None:
        if scan.value == find_value:
            if last is None:
                # found at the first element
                return scan.next
            # found within SLL, remove & return original 'sll'
            last.next = scan.next
            return sll
        last = scan
        scan = scan.next

    return sll

def remove_first(sll):
    """Remove the first element of an SLL.
    
    Return the new SLL head reference.
    """

    # if SLL is empty, do nothing
    if sll is None:
        return None

    # return reference to second element
    return sll.next

def remove_last(sll):
    """Remove the last element of an SLL.
    
    Returns a reference to the modified SLL.  Note that SLL may only
    contain one element to begin with.
    """

    # find last and second-last elements in SLL
    prev = None
    scan = sll

    while scan is not None:
        if scan.next is None:
            if prev is None:
                # only one element in SLL
                return None
            # remove last element & return original 'sll'
            prev.next = None
            return sll
        prev = scan
        scan = scan.next

    # get here if sll is None
    return None

def __str__(sll):
    """Convert an SLL into a 'list' string representation."""

    result = []

    while sll is not None:
        result.append(sll.value)
        sll = sll.next

    return str(result)
