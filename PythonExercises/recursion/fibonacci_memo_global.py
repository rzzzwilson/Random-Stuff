"""
Use it like this:

$ python3 fibonacci_memo_global.py 40
fibonacci_memo(40)=102334155     took 0.0000539s
"""


fib_memo = {0: 0, 1: 1}     # memo + base cases

def fibonacci(n):
    if n not in fib_memo:
        fib_memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return fib_memo[n]

if __name__ == '__main__':
    import sys
    import time
    
    number = int(sys.argv[1])
    
    start = time.time()
    fib_n = fibonacci(number)
    delta = time.time() - start
    
    print('fibonacci_memo_global(%d)=%d     took %.7fs' % (number, fib_n, delta))
