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
    global a
    a = ''
    start = time.time()
    for n in xrange(times):
        a += str(n)
    delta = time.time() - start
    return (a, delta)

# *REALLY* slow!
def concat_mutable(times):
    global a
    a = MutableString()
    start = time.time()
    for n in xrange(times):
        a += str(n)
    delta = time.time() - start
    return (a, delta)

def concat_array(times):
    global a
    a = array('c')
    start = time.time()
    for n in xrange(times):
        a.fromstring(str(n))
    a = ''.join(a)
    delta = time.time() - start
    return (a, delta)

def concat_join(times):
    global a
    a = []
    start = time.time()
    for n in xrange(times):
        a.append(str(n))
    a = ''.join(a)
    delta = time.time() - start
    return (a, delta)

def concat_stringio(times):
    global a
    a = StringIO()
    start = time.time()
    for n in xrange(times):
        a.write(str(n))
    a = a.getvalue()
    delta = time.time() - start
    return (a, delta)

def concat_comprehension(times):
    global a
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

    # our own handler for uncaught exceptions
    def excepthook(type, value, tb):
        msg = '\n' + '=' * 80
        msg += '\nUncaught exception:\n'
        msg += ''.join(traceback.format_exception(type, value, tb))
        msg += '=' * 80 + '\n'
        print(msg)
        sys.exit(1)

    # plug our handler into the python system
    sys.excepthook = excepthook


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
    (naive_str, result) = concat_naive(TIMES)
    print('        naive: %5.2fs' % result)
    with open('naive_str.data', 'w') as fd:
        fd.write(naive_str)
    del naive_str
    time.sleep(1)
#    result = concat_array(TIMES)
#    print('        array: %5.2fs' % result)
#    time.sleep(1)
    (join_str, result) = concat_join(TIMES)
    print('         join: %5.2fs' % result)
    with open('join_str.data', 'w') as fd:
        fd.write(join_str)
    del join_str
    time.sleep(1)
    (stringio_str, result) = concat_stringio(TIMES)
    print('     stringio: %5.2fs' % result)
    with open('stringio_str.data', 'w') as fd:
        fd.write(stringio_str)
    del stringio_str
    time.sleep(1)
    (comprehension_str, result) = concat_comprehension(TIMES)
    print('comprehension: %5.2fs' % result)
    with open('comprehension_str.data', 'w') as fd:
        fd.write(comprehension_str)
    del comprehension_str
    time.sleep(1)
