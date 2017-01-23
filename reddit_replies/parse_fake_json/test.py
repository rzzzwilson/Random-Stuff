#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://www.reddit.com/r/learnpython/comments/5plfhb/beginner_need_help_parsing_json/
"""

import sys


# the test data
Data = "[{u'id': 234207492300014L, u'name': u'General:'}, {u'id': 141253567024793L, u'name': u'Misc'}]"
print('Data=%s' % Data)

# parse the list of dicts
x = Data.strip()        # paranoid enough?
x = Data.replace(', {', '|{')
print('x=%s' % x)
if x[0] != '[' or x[-1] != ']':
    print('ERROR: badly formed data')
    sys.exit(10)
x = x[1:-1]

# split into list of dictionaries
y = x.split('|')
print('y=%s' % str(y))

# eval each dictionary string
for d in y:
    print('d=%s' % d)
    z = eval(d)
    print('\t.id=%s' % z['id'])
    print('\t.name=%s' % z['name'])
