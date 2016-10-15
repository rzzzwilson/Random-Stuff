#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A simple case.

The variable doesn't exist in global scope.
"""

try:
    print('global: variable=%d' % variable)
except NameError:
    print("global: variable isn't defined")
