import time

num = int(input('Enter number: '))

def fib_memo(n, memo=None):
    if memo is None:
        memo = {0: 1, 1: 1}
    if n not in memo:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

start = time.time()
memo_result = fib_memo(num)
memo_delta = time.time() - start
print('memo(%d)=%d, delta=%.6f' % (num, memo_result, memo_delta))

gmemo = {0: 1, 1: 1}
def fib_gmem(n):
    if n not in gmemo:
        gmemo[n] = fib_gmem(n-1) + fib_gmem(n-2)
    return gmemo[n]

start = time.time()
gmem_result = fib_gmem(num)
gmem_delta = time.time() - start
print('gmem(%d)=%d, delta=%.6f' % (num, gmem_result, gmem_delta))

def fib(n):
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)

start = time.time()
result = fib(num)
delta = time.time() - start
print(' fib(%d)=%d, delta=%.6f' % (num, result, delta))

print('mratio=%.2f' % (delta/memo_delta))
print('gratio=%.2f' % (delta/gmem_delta))
