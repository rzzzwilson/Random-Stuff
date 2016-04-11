#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The MatrixFind problem.  Read README.rst for the details.

0. Set current position to (0, 0), the top-left cell (must be the lowest value cell)
1. If the current position is on the matrix, goto step 4
2. If the stack is empty, return False
3. Pop the stack to current, goto step 1
4. If matrix(current) == required, return T
5. Push current (x+=1), current <- (X,Y=1), goto 1
"""


def matrix_find(matrix, required):
    """Return True if 'required' appears in 'matrix'.

    matrix    a 2D matrix sorted (ascending) both by rows and columns
    required  the value it is desired to find

    Return True if 'required' appears in 'matrix'.
    """

    # remember the axis sizes
    max_x = len(matrix)
    max_y = len(matrix[0])

    # the stack is implemented as a list
    stack = []

    # set current position to top-left (smallest) element
    # step 0
    x = 0
    y = 0

    # now do some searching
    while True:
        # step 1
        if not (x < max_x and y < max_y):
            # step 2
            if len(stack) < 1:
                return False
            # step 3
            (x, y) = stack.pop()
            continue

        # step 4
        if matrix[x][y] == required:
            return True

        # step 5
        stack.append((x+1, y))
        y += 1
