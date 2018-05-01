def is_prime(p, old_primes):
    """Return True if 'p' is prime.

    'old_primes' is list of primes so far.
    """

    if old_primes[p]:
        return True     # already found prime

    if (p % 2) == 0:    # check 2 divisor first
        return False

    # now check if any older primes can divide evenly
    for i in range(3, int(p**0.5)+1, 2):
        if (p % i) == 0:
            return False

    # 'p' is prime, remember in 'old_primes' and return True
    old_primes[p] = True
    return True

def step(g, m, n):
    """Find two primes p and p' in [m, n] such that p' = p + g.

    Return result pair [p, p'] where p < p'.
    Return None if no step pair found.
    """

    # list of which integers are primes
    primes = [False] * (n+1)

    # scan upwards from 'm' looking for primes
    if (m % 2) == 0:    # if 'm' is even, move up to next odd
        m += 1

    for x in range(m, n-g+1, 2):
        if is_prime(x, primes) and is_prime(x+g, primes):
            return [x, x+g]
