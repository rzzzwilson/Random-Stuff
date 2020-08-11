"""
Use it like this:

$ python3 fibonacci.py 40
fibonacci(40)=102334155     took 67.0459089s
"""

import sys
import time


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

number = int(sys.argv[1])

start = time.time()
fib_n = fibonacci(number)
delta = time.time() - start

print('     fibonacci(%d)=%d     took %.7fs' % (number, fib_n, delta))
