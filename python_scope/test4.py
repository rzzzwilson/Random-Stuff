#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A simple case.

The variable does exist in the local scope of a function.
"""

def test_func():
    variable = 0
    try:
        print('local: variable=%d' % variable)
    except NameError:
        print("local: variable isn't defined")

test_func()
