"""
Use it like this:

$ python3 fibonacci_tail.py 40
fibonacci_tail(40)=102334155     took 0.0000241s

This version uses tail recursion.
See https://www.youtube.com/watch?v=_JtPhF8MshA

Due to the flexibility of python we can write the fibonacci()
function as if it were the "go()" function in the video.
"""

import sys
import time


def fibonacci(num, a=0, b=1):
    if num == 0:
        return a
    if num == 1:
        return b
    return fibonacci(num-1, b, a+b)

number = int(sys.argv[1])

start = time.time()
fib_n = fibonacci(number)
delta = time.time() - start

print('fibonacci_tail(%d)=%d     took %.7fs' % (number, fib_n, delta))
