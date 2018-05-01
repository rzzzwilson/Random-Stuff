import time
import platform

print('Python %s' % platform.python_version())

def fib(n):
    if n in [0, 1]:
        return n
    return fib(n-1) + fib(n-2)

fib_dict = {0:0, 1:1}

def mem_fib(n):
    if n not in fib_dict:
        fib_dict[n] = mem_fib(n-1) + mem_fib(n-2)
    return fib_dict[n]

def iter_fib(n):
    prev = 0
    result = 1
    for _ in range(2, n+1):
        (prev, result) = (result, result+prev)
    return result

n = 100

#start = time.time()
#result = fib(n)
#delta1 = time.time() - start
#print('     fib(%d)=%d, time=%03.8fs' % (n, result, delta1))

start = time.time()
result = mem_fib(n)
delta2 = time.time() - start
print(' mem_fib(%d)=%d, time=%03.8fs' % (n, result, delta2))
#print('speedup is about %d times' % int(delta1/delta2))

start = time.time()
result = iter_fib(n)
delta = time.time() - start
print('iter_fib(%d)=%d, time=%03.8fs' % (n, result, delta))

