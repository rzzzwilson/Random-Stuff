#!/usr/bin/env python

"""Run string concatenation speed tests.

Usage: test2.py [-g]

where -g  turns the garbage collector OFF, default is ON.

Sort of the same as test.py, but try to 'hide' the string concatenation
from python optimization.  The basic idea is to take the code normally executed
inside the loop and move it outside where it is compiled.  Then inside the loop
just 'exec' the compiled code.  This appears to be enough to defeat the
optimixation.
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


#TIMES = 50000000
TIMES = 500000


def concat_naive(times):
    a = ''
    code = compile('a += str(n)', '<string>', 'exec')
    start = time.time()
    for n in xrange(times):
        exec(code)
    delta = time.time() - start
    return delta

# *REALLY* slow!
def concat_mutable(times):
    a = MutableString()
    code = compile('a += str(n)', '<string>', 'exec')
    start = time.time()
    for n in xrange(times):
        exec(code)
    delta = time.time() - start
    return delta

def concat_array(times):
    a = array('c')
    code = compile('a.fromstring(str(n))', '<string>', 'exec')
    start = time.time()
    for n in xrange(times):
        exec(code)
#        a.fromstring(str(n))
    a = ''.join(a)
    delta = time.time() - start
    return delta

def concat_join(times):
    a = []
    code = compile('a.append(str(n))', '<string>', 'exec')
    start = time.time()
    for n in xrange(times):
        exec(code)
#        a.append(str(n))
    a = ''.join(a)
    delta = time.time() - start
    return delta

def concat_stringio(times):
    a = StringIO()
    code = compile('a.write(str(n))', '<string>', 'exec')
    start = time.time()
    for n in xrange(times):
        exec(code)
#        a.write(str(n))
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
    import sys

    def usage(msg=None):
        if msg:
            print('#'*60)
            print(msg)
            print('#'*60 + '\n')
        print(__doc__)

    # look for the '-g' option
    gc_off = False
    if len(sys.argv) > 2:
        usage()
        sys.exit(1)
    if len(sys.argv) == 2:
        if sys.argv[1] == '-g':
            # turn OFF garbage collector
            import gc
            gc.disable()
            gc_off = True
        else:
            usage()
            sys.exit(1)

    time.sleep(0.5)
    print('Using Python %s on %s' % (platform.python_version(), platform.platform()))
    print('For %d concatenations, GC is %s:' % (TIMES, 'OFF' if gc_off else 'ON'))
    result = concat_naive(TIMES)
    print('        naive: %5.2fs' % result)
    time.sleep(1)
#    result = concat_array(TIMES)
#    print('        array: %5.2fs' % result)
#    time.sleep(1)
    result = concat_join(TIMES)
    print('         join: %5.2fs' % result)
    time.sleep(1)
    result = concat_stringio(TIMES)
    print('     stringio: %5.2fs' % result)
    time.sleep(1)
    result = concat_comprehension(TIMES)
    print('comprehension: %5.2fs' % result)
    time.sleep(1)
