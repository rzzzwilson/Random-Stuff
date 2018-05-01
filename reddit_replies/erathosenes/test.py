import time

def get_primes_and_factorization(N):
    lp = [0] * N
    pr = []
    for i in range(2, N):
        if not lp[i]:
            lp[i] = i
            pr.append(i)
        for (j, pr_j) in enumerate(pr):
            if pr_j <= lp[i] and i * pr_j <= N - 1:
                lp[i * pr_j] = pr_j
            else:
                break
    return pr

for N in range(1000000, 10000001, 1000000):
    start = time.time()
    primes = get_primes_and_factorization(N)
    delta = time.time() - start
    print(f'N={N}, len(primes)={len(primes)}, took {delta:6.2} s')
