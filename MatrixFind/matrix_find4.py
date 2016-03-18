#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The MatrixFind problem.  Read README.rst for the details.

This version uses brute-force - flatten the matrix and then check with 'in'.
"""

import itertools


def matrix_find(matrix, required):
    """Just brute-force!"""

    return required in list(itertools.chain.from_iterable(matrix))
