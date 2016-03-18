#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Time the original solution to the MatrixFind problem.
"""

import time


LOOP = 1000000


def time_simple_find(required):
    #          ---> Y
    matrix = [[1, 1, 3, 4],	# .
              [2, 2, 4, 5],	# .
              [2, 3, 4, 6],	# V
              [2, 3, 4, 7],	# 
              [3, 4, 4, 8],	# X
              [4, 5, 6, 9]]

    start = time.time()
    for _ in xrange(LOOP):
        mf.matrixFind(matrix, required)
    delta = time.time() - start
    print('%13s:   find %d, %d times took %7.3fs' % (ModuleName, required, LOOP, delta))

def time_notsimple_find(required):
    #          ---> Y
    matrix = [[0, 0, 0, 0, 1, 1, 1, 2],	    # .
              [0, 0, 1, 1, 2, 3, 7, 8],	    # .
              [1, 1, 2, 3, 4, 6, 8, 8],	    # .
              [2, 3, 3, 6, 6, 6, 8, 9],	    # v
              [2, 3, 3, 8, 8, 8, 8, 9],	    # 
              [2, 3, 4, 8, 8, 8, 8, 9],	    # 
              [2, 3, 5, 8, 8, 8, 9, 10],    # X
              [2, 3, 6, 8, 9, 9, 9, 10]]

    start = time.time()
    for _ in xrange(LOOP):
        mf.matrixFind(matrix, required)
    delta = time.time() - start
    print('%13s:   find %d, %d times took %7.3fs' % (ModuleName, required, LOOP, delta))


################################################################################

global Module, ModuleName

import mf
ModuleName = 'mf'
time_simple_find(7)
time_notsimple_find(7)
