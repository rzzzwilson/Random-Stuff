#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A simple case.

The variable exists in the global scope, read-only access.
"""

variable = 0

def test_func():
    try:
        print('local: variable=%d' % variable)
    except NameError:
        print("local: variable isn't defined")

test_func()
