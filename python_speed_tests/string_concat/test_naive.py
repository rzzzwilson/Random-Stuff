#!/usr/bin/env python

"""
Run simple naive string concatenation speed test.

Usage: test.py
"""


import time
import platform
from array import array
try:
    from cStringIO import StringIO
except ImportError:
    # python3 - make changes
    import io
    global StringIO
    StringIO = io.StringIO
    xrange = range


TIMES = 50000000

def concat_naive(times):
    a = ''
    start = time.time()
    for n in xrange(times):
        a += str(n)
    delta = time.time() - start
    return (a, delta)

# *REALLY* slow!
def concat_mutable(times):
    a = MutableString()
    start = time.time()
    for n in xrange(times):
        a += str(n)
    delta = time.time() - start
    return (a, delta)

def concat_array(times):
    a = array('c')
    start = time.time()
    for n in xrange(times):
        a.fromstring(str(n))
        #a.extend(str(n))	# slower
    a = ''.join(a)
    delta = time.time() - start
    return (a, delta)

def concat_join(times):
    a = []
    start = time.time()
    for n in xrange(times):
        a.append(str(n))
    a = ''.join(a)
    delta = time.time() - start
    return (a, delta)

def concat_stringio(times):
    a = StringIO()
    start = time.time()
    for n in xrange(times):
        a.write(str(n))
    a = a.getvalue()
    delta = time.time() - start
    return (a, delta)

def concat_comprehension(times):
    start = time.time()
    a = [str(n) for n in xrange(times)]
    a = ''.join(a)
    delta = time.time() - start
    return (a, delta)

if __name__ == '__main__':
    import sys

    def usage(msg=None):
        if msg:
            print('#'*60)
            print(msg)
            print('#'*60 + '\n')
        print(__doc__)

    print(f'Using Python {platform.python_version()} on {platform.platform()}')
    print(f'For {TIMES} concatenations:')
    (naive_str, result) = concat_naive(TIMES)
    print(f'        naive: {result:5.2f}s')
    with open('naive_str.data', 'w') as fd:
        fd.write(naive_str)
