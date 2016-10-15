#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A more complicated case.

The variable exists in the global scope.  We hacve two nested functions,
each which changes a local variable 'variable'.
"""

variable = 0

def test_func():

    def nested_func():
        try:
            print('        nested local: variable=%d' % variable)
        except NameError:
            print("        nested local: variable isn't defined")

        variable = 9999

        try:
            print('        nested local: variable=%d' % variable)
        except NameError:
            print("        nested local: variable isn't defined")

    try:
        print('    local: variable=%d' % variable)
    except NameError:
        print("    local: variable isn't defined")

    variable = 9

    try:
        print('    local: variable=%d' % variable)
    except NameError:
        print("    local: variable isn't defined")

    nested_func()

    variable = 99

    try:
        print('    local: variable=%d' % variable)
    except NameError:
        print("    local: variable isn't defined")

print('global: variable=%d' % variable)

test_func()

print('global: variable=%d' % variable)
