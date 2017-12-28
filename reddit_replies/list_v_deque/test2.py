import collections
import copy

aList  = list(range(10000)) 
aDeque = collections.deque(range(10000))

def test1():
   a = copy.copy(aList)
   for x in range(len(a)):
      del a[0]

def test2():
   a = copy.copy(aDeque)
   for x in range(len(a)):
      del a[0]

#python -m timeit -s"import test" "test.test1()"
#100 loops, best of 3: 11.4 msec per loop
#python -m timeit -s"import test" "test.test2()"
#1000 loops, best of 3: 587 usec per loop
