#!/bin/env python
# -*- coding: utf-8 -*-

"""
An attempt to answer the reddit question:
    https://www.reddit.com/r/learnpython/comments/6rvs5c/recursive_exercise_help/

The statement of what is required:

def pack(L, n):
    '''Return the subset of L with the largest sum up to n
    >>> s = [4,1,3,5]
    >>> pack(s, 7)
    {3, 4}
    >>> pack(s, 6)
    {1, 5}
    >>> pack(s, 11)
    {1, 4, 5}
    '''
"""

def pack (L, n):
    """Function to return a set containing elements that sum to <= n.

    L  the list to take elements from
    n  the maximal number to sum elements to

    Returns a set containing zero or more elements of 'L' that
    sum to <= 'n'.
    """

    # base case - just return an empty set
    if not L:
        return set()

    if L[0] <= n:
        # assuming L[0] will be in result, calculate results
        all_subset = pack(L[1:], n - L[0])  # possible result tail
        all_result = {L[0]}                 # possible result header
        all_result.update(all_subset)       # get possible final result
        all_sum = sum(all_result)           # get possible result sum

        # if we already have 'n', go no further (optimization)
        if all_sum == n:
            return all_result

        # see if pack() on L[1:] gets a better result than above
        # call these 'alternate' results - hence the 'alt' below
        max_alt_subset = {}     # holds best result from below
        max_alt_sum = all_sum   # the sum we have to beat

        alt_subset = L[1:]      # the initial subset
        while alt_subset:
            # get a pack() for this tail and sum of result
            alt_pack_subset = pack(alt_subset, n)
            alt_sum_subset = sum(alt_pack_subset)

            # if this is an improvement, save results
            if alt_sum_subset > max_alt_sum:
                max_alt_subset = alt_pack_subset
                max_alt_sum = alt_sum_subset

            # try next smallest tail
            alt_subset = alt_subset[1:]

        if max_alt_sum > all_sum:
            # we got a better result from tail alone
            return max_alt_subset

        # otherwise return the first result which includes L[0]
        return all_result
    else:
        # first element > n, try tail only
        return pack(L[1:], n)
