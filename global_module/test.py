#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test the singleton module:
    . add some attributes
    . call function in another module that sets a singleton attribute
    . dump all singleton attributes
    . save state into a file for test3.py
"""

import singleton
import test2

singleton.tom = 'tom'
singleton.dick = 2
singleton.harry = (3.0, 'harry')

test2.test2({1:'one'})
print('singleton.test2=%s' % str(singleton.test2))

print('singleton: %s' % str(dir(singleton)))

payload = singleton.payload()
for (k, v) in payload.items():
    print('singleton.%s=%s\t%s' % (k, str(v), type(v)))

singleton.save()
