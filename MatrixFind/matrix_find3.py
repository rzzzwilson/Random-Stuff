#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The MatrixFind problem.  Read README.rst for the details.

This version runs down the diagonal fro (0, 0) looking for a value matrix(x+1,y+1)
that is greater than the required value.  If we find required, we stop of course.

Once we stop runing down the diagonal we scan horizontally in X until found or end.
If found, return True.  Otherwise we scan vertically until end or found.

This iterative solution shoulld take O(n) time.
"""


def matrix_find(matrix, required):
    # remember the axis sizes
    max_x = len(matrix)
    max_y = len(matrix[0])

    x = 0
    y = 0

    while True:
        if x >= max_x or y >= max_y:
            return False

        if  (x+1) < max_x and (y+1) < max+y:
            if 
    while y < max_y:
        if matrix[scan_x][y] <= required:
            if matrix[scan_x][y] == required:
                return True
        y += 1

    return mf(x, y, matrix, required, max_x, max_y)
