#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The MatrixFind problem.  Read README.rst for the details.

This version uses the divide-and-conquer approach.
"""


def sub_matrix_find(matrix, start_x, start_y, max_x, max_y, required):
    """Divide and conquer.
    
    matrix    the matrix to search
    start_x   the X coordinate of the top-left corner element
    start_y   the Y coordinate of the top-left corner element
    max_x     the X coordinate of the bottom-right corner element
    max_y     the Y coordinate of the bottom-right corner element
    required  the value to be found

    Return True if element value 'required' is found, else False.
    """

    global Count

    # check still on matrix
    if start_x > max_x or start_y > max_y:
        return False

    # scan diagonally from (start_x, start_y)
    x = start_x
    y = start_y
    while True:
        value = matrix[x][y]
        Count += 1
        if value == required:
            return True
        if value > required:    # required not found
            # search the top-right sub-matrix
            result = sub_matrix_find(matrix, x, start_y, max_x, y-1, required)
            if result:
                return True
            # search bottom-left sub-matrix
            return  sub_matrix_find(matrix, start_x, y, x-1, max_y, required)

        x += 1
        y += 1

        if x > max_x:
            return sub_matrix_find(matrix, start_x, y, max_x, max_y, required)
        if y > max_y:
            return sub_matrix_find(matrix, x, start_y, max_x, max_y, required)

def matrix_find(matrix, required):
    """High-level function to call sub_matrix_find().
    
    matrix    the matrix to search
    required  the value to be found

    Return True if element value 'required' is found, else False.
    """

    global Count

    Count = 0

    # get the axis max sizes
    max_x = len(matrix) - 1
    max_y = len(matrix[0]) - 1

    result = sub_matrix_find(matrix, 0, 0,  max_x, max_y, required)
    print('Count=%d, M=%d, N=%d' % (Count, max_x, max_y))
    return result

