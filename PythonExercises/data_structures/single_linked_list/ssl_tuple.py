#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tuple implementation of a singly-linked list.

We actually use python lists instead of tuple, as tuples are immutable.
"""

######
# Functions to manipulate an SSL.
######

def _find_last(ssl):
    """Internal function to find last tuple in an SSL.

    Returns a reference to the last tuple in the given SSL.
    Returns None if the SSL is empty.
    """

    if ssl is None:
        return None
    while ssl[1] is not None:
        ssl = ssl[1]
    return ssl

def length(ssl):
    """Return the count of tuples in 'ssl'."""

    count = 0

    while ssl is not None:
        count += 1
        ssl = ssl[1]

    return count

def add_front(ssl, value):
    """Add a new tuple containing 'value' at the front of an SSL.

    Returns a reference to the new head of the SSL.
    """

    return [value, ssl]

def add_end(ssl, value):
    """Add a new tuple containing 'value' at the end of an SSL.

     Returns a reference to the head of the SSL.
     Just to be the same as add_front().
     """

    # find last tuple of the SSL
    last = _find_last(ssl)
    if last is None:
        # SSL is empty
        return [value, None]

    # add new tuple to end
    last[1] = [value, None]
    return ssl

def find(ssl, val):
    """Find tuple value 'val' in an SSL.

    ssl   the SSL to search in
    val   the tuple value to find

    Returns a reference to the tuple containing 'val'.  Return None if
    not found.

    The SSL is not assumed to be sorted.
    """

    while ssl is not None:
        if ssl[0] == val:
            return ssl
        ssl = ssl[1]

    return None

def add_after(ssl, find_value, value):
    """Add an tuple containing 'value' after the tuple containing 'find_value'.

    Return a reference to the found tuple.
    If the tuple containing 'find_value' is not found, return None.

    Adds after the first tuple found, not any subsequent tuples with the
    same value.
    """

    f = find(ssl, find_value)
    if f is not None:
        f[1] = [value, f[1]]
        return ssl
    return None

def remove(ssl, find_value):
    """Find and remove tuple with value 'find_value' in an SSL.

    ssl         the SSL to search in
    find_value  the tuple value to find and remove

    Returns a reference to the possibly modified SSL.  This may be different
    from the original 'ssl' reference as the first tuple may be removed.
    """

    # a reference to the previous tuple before the 'ssl' tuple
    last = None
    scan = ssl

    while scan is not None:
        if scan[0] == find_value:
            if last is None:
                # found at the first tuple
                return scan[1]
            # found within SSL, remove & return original 'ssl'
            last[1] = scan[1]
            return ssl
        last = scan
        scan = scan[1]

    return ssl

def remove_first(ssl):
    """Remove the first tuple of an SSL.

    Return the new SSL head reference.
    """

    # if SSL is empty, do nothing
    if ssl is None:
        return None

    # return reference to second tuple
    return ssl[1]

def remove_last(ssl):
    """Remove the last tuple of an SSL.

    Returns a reference to the modified SSL.  Note that SSL may only
    contain one tuple to begin with.
    """

    # find last and second-last tuples in SSL
    # can't use _find_last() as we also need predecessor
    prev = None
    scan = ssl

    while scan is not None:
        if scan[1] is None:
            if prev is None:
                # only one tuple in SSL
                return None
            # remove last tuple & return original 'ssl'
            prev[1] = None
            return ssl
        prev = scan
        scan = scan[1]

    # get here if ssl is None
    return None

def __str__(ssl):
    """Convert an SSL into a 'list' string representation."""

    result = []

    while ssl is not None:
        result.append(ssl[0])
        ssl = ssl[1]

    return str(result)
