#!/usr/bin/env python

"""Run simple string concatenation speed tests."""


import time
import platform
from UserString import MutableString
from array import array
from cStringIO import StringIO


TIMES = 50000000

def concat_naive(times):
    a = ''
    start = time.time()
    for n in xrange(times):
        a += str(n)
    delta = time.time() - start
    return delta

# *REALLY* slow!
def concat_mutable(times):
    a = MutableString()
    start = time.time()
    for n in xrange(times):
        a += str(n)
    delta = time.time() - start
    return delta

def concat_array(times):
    a = array('c')
    start = time.time()
    for n in xrange(times):
        a.fromstring(str(n))
        #a.extend(str(n))	# slower
    a = ''.join(a)
    delta = time.time() - start
    return delta

def concat_join(times):
    a = []
    start = time.time()
    for n in xrange(times):
        a.append(str(n))
    a = ''.join(a)
    delta = time.time() - start
    return delta

def concat_stringio(times):
    a = StringIO()
    start = time.time()
    for n in xrange(times):
        a.write(str(n))
    a = a.getvalue()
    delta = time.time() - start
    return delta

def concat_comprehension(times):
    start = time.time()
    a = [str(n) for n in xrange(times)]
    a = ''.join(a)
    delta = time.time() - start
    return delta

if __name__ == '__main__':
    print('Using Python %s on %s' % (platform.python_version(), platform.platform()))
    print('For %d concatenations:' % TIMES)
    result = concat_naive(TIMES)
    print('        naive: %5.2fs' % result)
    time.sleep(1)
    result = concat_array(TIMES)
    print('        array: %5.2fs' % result)
    time.sleep(1)
    result = concat_join(TIMES)
    print('         join: %5.2fs' % result)
    time.sleep(1)
    result = concat_stringio(TIMES)
    print('     stringio: %5.2fs' % result)
    time.sleep(1)
    result = concat_comprehension(TIMES)
    print('comprehension: %5.2fs' % result)
#    time.sleep(1)
#    result = concat_mutable(TIMES)
#    print('      mutable: %5.2fs' % result)
    time.sleep(1)
