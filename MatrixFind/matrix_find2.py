#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The MatrixFind problem.  Read README.rst for the details.

This version uses the python stack rather than an explicit stack.  This means we do:
    matrix_find(x+1, y, matrix, required)
rather than:
    stack.append((x+1, y))
and the appropriate changes for the pop().

1. if the current position not in the matrix, return False
2. if the current value == required, return True
3. if mf(x, y+1, ...) is True, return True
4. return mf(x+1, y, ...)
"""


def mf(x, y, matrix, required, max_x, max_y):
    """Return True if 'required' appears in 'matrix'.

    x, y      the current position
    matrix    a 2D matrix sorted (ascending) both by rows and columns
    required  the value it is desired to find
    max_x     maximum index in the X direction
    max_y     maximum index in the Y direction

    Return True if 'required' appears in 'matrix'.
    """

    if not (x < max_x and y < max_y):
        return False

    if matrix[x][y] == required:
        return True

    result = mf(x, y+1, matrix, required, max_x, max_y)
    if result:
        return True

    return mf(x+1, y, matrix, required, max_x, max_y)

def matrix_find(matrix, required):
    # remember the axis sizes
    max_x = len(matrix)
    max_y = len(matrix[0])

    return mf(0, 0, matrix, required, max_x, max_y)
