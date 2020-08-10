import sys
import time

"""
Use it like this:

$ python3 fibonacci_iter.py 40
fibonacci_iter(40)=102334155     took 0.0000069s

This uses a standard iterative approach, no recursion.
"""

def fibonacci_iter(n):
    (a, b) = (0, 1)
    for _ in range(n):
        (a, b) = (b, a+b)
    return a

number = int(sys.argv[1])

start = time.time()
fib_n = fibonacci_iter(number)
delta = time.time() - start

print('fibonacci_iter(%d)=%d     took %.7fs' % (number, fib_n, delta))
