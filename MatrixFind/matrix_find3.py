#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The MatrixFind problem.  Read README.rst for the details.

This version runs down the diagonal from (0, 0) looking for a value matrix(x+1,y+1)
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

        value = matrix[x][y]

        if value == required:
            return True

        if value > required:
            # step back to previous diag square
            x -= 1
            y -= 1

            # scan horizontally for required
            xx = x
            while xx < max_x:
                scan_value = matrix[xx][y]
                if scan_value == required:
                    return True
                if scan_value > required:
                    break
                xx += 1

            # scan vertically for required
            yy = y
            while yy < max_y:
                scan_value = matrix[x][yy]
                if scan_value == required:
                    return True
                if scan_value > required:
                    return False
                yy += 1

        x += 1
        y += 1

    return False


    return mf(x, y, matrix, required, max_x, max_y)
