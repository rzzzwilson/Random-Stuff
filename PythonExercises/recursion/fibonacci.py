import sys
import time

"""
Use it like this:

$ python fibonacci.py 40
Fibonacci(40)=102334155     took 31.8008261s
"""

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
