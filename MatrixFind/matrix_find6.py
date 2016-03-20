#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The MatrixFind problem.  Read README.rst for the details.

This version uses the expanded 'limit view' approach.

We use a recursive approach to allow an oranges-with-oranges comparison with
earlier versions.
"""


def sub_matrix_find(matrix, left_col, right_col, top_row, bot_row, required):
    """The "limit view" algorithm.
    
    matrix     the matrix to search
    left_col   index of the column at the left of the view
    right_col  index of the column at the right of the view
    top_row    index of the column at the top of the view
    bot_row    index of the column at the bottom of the view
    required   the value to be found

    Return True if element value 'required' is found, else False.
    """

    # step 1.  scan top row
    for x in range(left_col, right_col+1):
        value = matrix[x][top_row]
        if value == required:
            return True
        if value > required:
            right_col = x - 1
            if right_col < left_col:
                return False
            break

    # step 2.  scan bottom row
    for x in range(right_col, left_col-1, -1):
        value = matrix[x][bot_row]
        if value == required:
            return True
        if value < required:
            left_col = x + 1
            if left_col > right_col:
                return False
            break

    # step 3.  scan left column
    for y in range(top_row, bot_row+1):
        value = matrix[left_col][y]
        if value == required:
            return True
        if value > required:
            bot_row = y - 1
            if bot_row < top_row:
                return False
            break

    # step 4.  scan right column
    for y in range(bot_row, top_row-1, -1):
        value = matrix[right_col][y]
        if value == required:
            return True
        if value < required:
            top_row = y + 1
            if top_row > bot_row:
                return False
            break

    return sub_matrix_find(matrix, left_col, right_col, top_row, bot_row, required)


def matrix_find(matrix, required):
    """High-level function to call sub_matrix_find().
    
    matrix    the matrix to search
    required  the value to be found

    Return True if element value 'required' is found, else False.
    """

    # get the axis max sizes
    max_x = len(matrix) - 1
    max_y = len(matrix[0]) - 1

    result = sub_matrix_find(matrix, 0, max_x, 0, max_y, required)
    return result

