#!/usr/bin/env python

"""
Compare relative speeds of dict and defaultdict in various uses.
"""

import time
import collections

string = 'The quick brown fox jumps over the lazy dog'*1000000

# compare methods
accum_setdefault = {}
start = time.time()
for key in string:
    accum_setdefault.setdefault(key, 0)
    accum_setdefault[key] += 1
delta = time.time() - start
print(' dict: took %.2fs' % delta)

accum_get = {}
start = time.time()
for key in string:
    accum_get[key] = accum_get.get(key, 0) + 1
delta = time.time() - start
print('  get: took %.2fs' % delta)

accum_defaultdict = collections.defaultdict(int)
start = time.time()
for key in string:
    accum_defaultdict[key] += 1
delta = time.time() - start
print('ddict: took %.2fs' % delta)

accum_try = {}
start = time.time()
for key in string:
    try:
        accum_try[key] += 1
    except KeyError:
        accum_try[key] = 1
delta = time.time() - start
print('  try: took %.2fs' % delta)

# check all results are the same
items_setdefault = accum_setdefault.items()
items_setdefault = sorted(items_setdefault)

items_get = accum_get.items()
items_get = sorted(items_get)

items_defaultdict = accum_defaultdict.items()
items_defaultdict = sorted(items_defaultdict)

items_try = accum_try.items()
items_try = sorted(items_try)

if items_setdefault != items_get:
    print('items_setdefault != items_get')
elif items_get != items_defaultdict:
    print('items_get != items_defaultdict')
elif items_defaultdict != items_try:
    print('items_defaultdict != items_try')
else:
    print('All methods produce identical dictionaries')

