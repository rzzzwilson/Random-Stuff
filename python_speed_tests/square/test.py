#!/usr/bin/env python

"""Which is faster, x*x or x**2?"""


import time
import platform


TIMES = 50000000

def simplesimple(times):
    x = 3
    start = time.time()
    for n in xrange(times):
        z = x*x
    delta = time.time() - start
    return delta

def powersimple(times):
    x = 3
    start = time.time()
    for n in xrange(times):
        z = x**2
    delta = time.time() - start
    return delta

def simple(times):
    x = 3
    y = 2
    start = time.time()
    for n in xrange(times):
        z = (x+y)*(x+y)
    delta = time.time() - start
    return delta

def power(times):
    x = 3
    y = 2
    start = time.time()
    for n in xrange(times):
        z = (x+y)**2
    delta = time.time() - start
    return delta

print('Using Python %s on %s' % (platform.python_version(), platform.platform()))
print('For %d concatenations:' % TIMES)

result = simplesimple(TIMES)
print('        x*x: %5.2fs' % result)
time.sleep(1)

result = powersimple(TIMES)
print('       x**2: %5.2fs' % result)
time.sleep(1)

result = simple(TIMES)
print('(x+y)*(x+y): %5.2fs' % result)
time.sleep(1)

result = power(TIMES)
print('   (x+y)**2: %5.2fs' % result)
time.sleep(1)

