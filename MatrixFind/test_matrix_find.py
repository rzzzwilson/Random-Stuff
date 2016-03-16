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

#import matrix_find
#import matrix_find2 as matrix_find
import matrix_find3 as matrix_find


def test_matrix_find(required):
    #          ---> Y
    matrix = [[1, 1, 3, 4],	# .
              [2, 2, 4, 5],	# .
              [2, 3, 4, 6],	# V
              [2, 3, 4, 7],	# 
              [3, 4, 4, 8],	# X
              [4, 5, 6, 9]]

    if matrix_find.matrix_find(matrix, required):
        print('Value %d was found in matrix' % required)
    else:
        print('Value %d was NOT found in matrix' % required)

def test_matrix_find2(required):
    #          ---> Y
    matrix = [[1, 1, 3, 4],	# .
              [3, 3, 4, 5],	# .
              [3, 3, 4, 6],	# V
              [3, 3, 4, 7],	# 
              [3, 4, 4, 8],	# X
              [4, 5, 6, 9]]

    if matrix_find.matrix_find(matrix, required):
        print('Value %d was found in matrix' % required)
    else:
        print('Value %d was NOT found in matrix' % required)

for _ in range(1000000):
    test_matrix_find(7) 
    test_matrix_find(17) 
    test_matrix_find2(2) 
