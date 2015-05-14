#!/usr/bin/env python

"""
Test relative speed of:
    value = 1
    if flag:
        value = 2
against:
    value = 2 if flag else 1
"""

import time


LOOPS = 100000000
flag = False

start = time.time()
for _ in xrange(LOOPS):
    value = 1
    if flag:
        value = 2
delta = time.time() - start
print('if     took %.2fs' % delta)

start = time.time()
for _ in xrange(LOOPS):
    value = 2 if flag else 1
delta = time.time() - start
print('ifelse took %.2fs' % delta)

