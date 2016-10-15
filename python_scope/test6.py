#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A simple case.

The variable exists in the global scope, try to change without 'global' statement.

Note that we don't get an error.  We create a local variable and set it to 99.
This has no effect on the global 'variable'.
"""

variable = 0

def test_func():
    variable = 99

    try:
        print('local: variable=%d' % variable)
    except NameError:
        print("local: variable isn't defined")

test_func()

print('global: variable=%d' % variable)
