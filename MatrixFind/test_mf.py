#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test the mf.py code.
"""

import mf

def test_mf(required):
    #          ---> Y
    matrix = [[1, 1, 3, 4],     # .
              [2, 2, 4, 5],     # .
              [2, 3, 4, 6],     # V
              [2, 3, 4, 7],     # 
              [3, 4, 4, 8],     # X
              [4, 5, 6, 9]]

    result = mf.matrixFind(matrix, required)
    if result:
        print('Value %d was found in matrix' % required)
    else:
        print('Value %d was NOT found in matrix' % required)

def test_mf2(required):
    #          ---> Y
    matrix = [[1, 1, 3, 4], # .
              [3, 3, 4, 5], # .
              [3, 3, 4, 6], # V
              [3, 3, 4, 7], # 
              [3, 4, 4, 8], # X
              [4, 5, 6, 9]]

    result = mf.matrixFind(matrix, required)
    if result:
        print('Value %d was found in matrix' % required)
    else:
        print('Value %d was NOT found in matrix' % required)

for _ in range(1000000):
    test_mf(7) 
    test_mf(17) 
    test_mf2(2) 

