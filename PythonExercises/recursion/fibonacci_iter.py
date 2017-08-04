import sys
import time

"""
Use it like this:

$ python fibonacci_iter.py 40
Fibonacci(40)=102334155     took 31.8008261s
"""

FibMemo = {0: 0, 1: 1}     # memo + base cases
FibMemoMax = 1

def fibonacci_iter(n):
    global FibMemoMax
    while FibMemoMax < n:
        FibMemoMax += 1
        print
        FibMemo[FibMemoMax] = FibMemo[FibMemoMax-1] + FibMemo[FibMemoMax-2]

    return FibMemo[n]

number = int(sys.argv[1])

start = time.time()
fib_n = fibonacci_iter(number)
delta = time.time() - start

print('fibonacci_iter(%d)=%d     took %.7fs' % (number, fib_n, delta))
