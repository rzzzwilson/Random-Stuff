#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The MatrixFind problem.  Read README.rst for the details.

0. Set current position to (0, 0), the top-left cell (must be the lowest value cell)
1. If the current position is on the matrix, goto step 4
2. If the stack is empty, return False
3. Pop the stack to current
4. If M(current) == required, return T
5. Push current (x+=1), current <- (X,Y=1), goto 1
"""


def log(msg):
    pass
#    print(msg)

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
    log('step 0: x=%d, y=%d' % (x, y))

    # now do some searching
    while True:
        log('loop: stack=%s' % str(stack))
        # step 1
        if not (x < max_x and y < max_y):
            log('step 1: x=%d, y=%d, current not on matrix' % (x, y))
            # step 2
            if len(stack) < 1:
                log('step 2: stack empty, return False')
                return False
            # step 3
            (x, y) = stack.pop()
            log('step 3: pop stack, x=%d, y=%d' % (x, y))

        # step 4
        if matrix[x][y] == required:
            log('step 4: found required, returning True')
            return True

        # step 5
        stack.append((x+1, y))
        y += 1
        log('step 5: push current onto stack, new x=%d, y=%d' % (x, y))




def test_matrix_find():
    #          ---> Y
    matrix = [[1, 1, 3, 4],	# .
              [2, 2, 4, 5],	# .
              [2, 3, 4, 6],	# V
              [2, 3, 4, 7],	# 
              [3, 4, 4, 8],	# X
              [4, 5, 6, 9]]

    result = matrix_find(matrix, 7)
    if result:
        print('Value 7 was found in matrix')
    else:
        print('Value 7 was NOT found in matrix')

test_matrix_find() 

