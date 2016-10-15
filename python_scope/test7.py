#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A simple case.

The variable exists in the global scope, try to change using 'global' statement.
"""

variable = 0

def test_func():
    global variable

    variable = 99

    try:
        print('local: variable=%d' % variable)
    except NameError:
        print("local: variable isn't defined")

test_func()

print('global: variable=%d' % variable)
