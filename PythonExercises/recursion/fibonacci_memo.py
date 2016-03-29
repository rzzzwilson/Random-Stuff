import sys
import time

"""
Use it like this:

$ python fibonacci_memo.py 40
Fibonacci(40)=102334155     took 31.8008261s
"""

fib_memo = {0: 0, 1: 1}     # memo + base cases

def fibonacci_memo(n):
    if n not in fib_memo:
        fib_memo[n] = fibonacci_memo(n-1) + fibonacci_memo(n-2)
    return fib_memo[n]

number = int(sys.argv[1])

start = time.time()
fib_n = fibonacci_memo(number)
delta = time.time() - start

print('fibonacci_memo(%d)=%d     took %.7fs' % (number, fib_n, delta))
