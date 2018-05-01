import timeit

def loop10():
    Sum = 0
    for x in range(10):
        for y in range(10):
            Sum = Sum - y

print(timeit.timeit(loop10))
