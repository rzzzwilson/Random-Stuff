#!/usr/bin/env python

"""Which is faster to unpack, tuple or namedtuple?"""


import time
import platform
from collections import namedtuple


TIMES = 10000000

def unpack_tuple(times):
    my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
    start = time.time()
    for n in xrange(times):
        (a01, a02, a03, a04, a05, a06, a07, a08, a09, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20) = my_tuple
    delta = time.time() - start
    return delta

def unpack_named_tuple(times):
    ntuple = namedtuple('ntuple', ['a01', 'a02', 'a03', 'a04', 'a05', 'a06', 'a07', 'a08', 'a09', 'a10',
                                   'a11', 'a12', 'a13', 'a14', 'a15', 'a16', 'a17', 'a18', 'a19', 'a20'])
    my_tuple = ntuple(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
    start = time.time()
    for n in xrange(times):
        a01 = my_tuple.a01
        a02 = my_tuple.a02
        a03 = my_tuple.a03
        a04 = my_tuple.a04
        a05 = my_tuple.a05
        a06 = my_tuple.a06
        a07 = my_tuple.a07
        a08 = my_tuple.a08
        a09 = my_tuple.a09
        a10 = my_tuple.a10
        a11 = my_tuple.a11
        a12 = my_tuple.a12
        a13 = my_tuple.a13
        a14 = my_tuple.a14
        a15 = my_tuple.a15
        a16 = my_tuple.a16
        a17 = my_tuple.a17
        a18 = my_tuple.a18
        a19 = my_tuple.a19
        a20 = my_tuple.a20
    delta = time.time() - start
    return delta

def unpack_named_tuple_single(times):
    ntuple = namedtuple('ntuple', ['a01', 'a02', 'a03', 'a04', 'a05', 'a06', 'a07', 'a08', 'a09', 'a10',
                                   'a11', 'a12', 'a13', 'a14', 'a15', 'a16', 'a17', 'a18', 'a19', 'a20'])
    my_tuple = ntuple(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
    start = time.time()
    for n in xrange(times):
        a02 = my_tuple.a02
    delta = time.time() - start
    return delta

print('Using Python %s on %s' % (platform.python_version(), platform.platform()))
print('For %d concatenations:' % TIMES)

result = unpack_tuple(TIMES)
print('            tuple: %5.2fs' % result)
time.sleep(1)

result = unpack_named_tuple(TIMES)
print('       namedtuple: %5.2fs' % result)
time.sleep(1)

result = unpack_named_tuple_single(TIMES)
print('namedtuple single: %5.2fs' % result)
