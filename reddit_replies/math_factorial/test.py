    
    """
    Is math.factorial() linear?
    """
    
    import math
    import time
    LOOPS = 10000
    last_delta = None
    print(f'Timing over {LOOPS} iterations')
    for n in [2**x for x in range(1, 16)]:
        start = time.time()
        for _ in range(LOOPS):
            math.factorial(n)
        delta = time.time() - start
        if last_delta:
            slowdown = delta / last_delta
            print(f'f({n:5d}) took {delta:7.3f}s, which is {slowdown:.1f} times slower than previous')
        else:
            print(f'f({n:5d}) took {delta:7.3f}s')
        last_delta = delta
