import timeit

def loop100():
    Sum = 0
    for x in range(100):
        Sum = Sum - x

print(timeit.timeit(loop100))
