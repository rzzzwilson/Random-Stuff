#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A simple case.

The variable exists in the global scope, try to change using 'global' statement.
We put the 'global' statement at the end of the function, showing that the
compiler notices the statement and makes 'variable' global for the whole
function scope.  We *do* get a warning, though.
"""

variable = 0

def test_func():
    variable = 99

    try:
        print('local: variable=%d' % variable)
    except NameError:
        print("local: variable isn't defined")

    global variable

test_func()

print('global: variable=%d' % variable)
