#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tuple implementation of a singly-linked list.

We actually use python lists instead of tuple, as tuples are immutable.
Two element lists *are*tuples, in the mathematical sense.
"""

######
# Functions to manipulate an SLL.
######

def _find_last(sll):
    """Internal function to find last tuple in an SLL.

    Returns a reference to the last tuple in the given SLL.
    Returns None if the SLL is empty.
    """

    if sll is None:
        return None
    while sll[1] is not None:
        sll = sll[1]
    return sll

def length(sll):
    """Return the count of tuples in 'sll'."""

    count = 0

    while sll is not None:
        count += 1
        sll = sll[1]

    return count

def add_front(sll, value):
    """Add a new tuple containing 'value' at the front of an SLL.

    Returns a reference to the new head of the SLL.
    """

    return [value, sll]

def add_back(sll, value):
    """Add a new tuple containing 'value' at the end of an SLL.

     Returns a reference to the head of the SLL.
     Just to be the same as add_front().
     """

    # find last tuple of the SLL
    last = _find_last(sll)
    if last is None:
        # SLL is empty
        return [value, None]

    # add new tuple to end
    last[1] = [value, None]
    return sll

def find(sll, val):
    """Find tuple value 'val' in an SLL.

    sll   the SLL to search in
    val   the tuple value to find

    Returns a reference to the tuple containing 'val'.  Return None if
    not found.

    The SLL is not assumed to be sorted.
    """

    while sll is not None:
        if sll[0] == val:
            return sll
        sll = sll[1]

    return None

def add_after(sll, find_value, value):
    """Add an tuple containing 'value' after the tuple containing 'find_value'.

    Return a reference to the found tuple.
    If the tuple containing 'find_value' is not found, return None.

    Adds after the first tuple found, not any subsequent tuples with the
    same value.
    """

    f = find(sll, find_value)
    if f is not None:
        f[1] = [value, f[1]]
        return sll
    return None

def remove(sll, find_value):
    """Find and remove tuple with value 'find_value' in an SLL.

    sll         the SLL to search in
    find_value  the tuple value to find and remove

    Returns a reference to the possibly modified SLL.  This may be different
    from the original 'sll' reference as the first tuple may be removed.
    """

    # a reference to the previous tuple before the 'sll' tuple
    last = None
    scan = sll

    while scan is not None:
        if scan[0] == find_value:
            if last is None:
                # found at the first tuple
                return scan[1]
            # found within SLL, remove & return original 'sll'
            last[1] = scan[1]
            return sll
        last = scan
        scan = scan[1]

    return sll

def remove_first(sll):
    """Remove the first tuple of an SLL.

    Return the new SLL head reference.
    """

    # if SLL is empty, do nothing
    if sll is None:
        return None

    # return reference to second tuple
    return sll[1]

def remove_last(sll):
    """Remove the last tuple of an SLL.

    Returns a reference to the modified SLL.  Note that SLL may only
    contain one tuple to begin with.
    """

    # find last and second-last tuples in SLL
    # can't use _find_last() as we also need predecessor
    prev = None
    scan = sll

    while scan is not None:
        if scan[1] is None:
            if prev is None:
                # only one tuple in SLL
                return None
            # remove last tuple & return original 'sll'
            prev[1] = None
            return sll
        prev = scan
        scan = scan[1]

    # get here if sll is None
    return None

def map_fun(sll, func, *args):
    """Apply func(*args) to each element value in the sll."""

    scan = sll

    while scan is not None:
        scan[0] = func(scan[0], *args)
        scan = scan[1]

    return sll

def __str__(sll):
    """Convert an SLL into a 'list' string representation."""

    result = []

    while sll is not None:
        result.append(sll[0])
        sll = sll[1]

    return str(result)
