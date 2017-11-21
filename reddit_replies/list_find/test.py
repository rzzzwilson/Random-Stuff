#!/usr/bin/env python3

"""
Code to investigate how to find an element of a list given just
a condition.  That is, given a condition like "x > 5" find the
first element of a list for which the condition is true.
"""

import inspect


def cond_find(the_list, cond):
    """Return the index of the first element in a list that satisfies a condition.

    the_list  list we will search
    cond      a lambda like "lambda x: x > 5"

    Returns the index of the first element satisifying the condition.
    Raises a ValueError exception if no element satisfies the condition.
    """

    # construct a list of True/False using the condition
    tf_list = [cond(x) for x in the_list]
    if not any(tf_list):
        code = inspect.getsource(cond)
        raise ValueError('Element not found: %s' % code)
    return tf_list.index(True)


l = [1, 2, 3, 4, 5, 6, 8, 12]
index = cond_find(l, lambda x: x> 5)
print('l=%s, index=%d' % (str(l), index))

index = cond_find(l, lambda x: x < 0)
