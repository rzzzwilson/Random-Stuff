"""
Code to compare relative speeds of using lists and deques.  Runs under
either python2 or python 3.  From this post on reddit:

https://www.reddit.com/r/learnpython/comments/7mmenq/use_deque_instead_of_list_always/
"""

import copy
import time
import collections

#Sizes = [10, 100, 1000, 10000, 100000, 1000000]
Sizes = [10, 100, 1000, 10000, 100000]

def obj_del_start(list_deque, size, obj_type):
    a = copy.copy(list_deque)
    while a:
        del a[0]

def obj_del_end(list_deque, size, obj_type):
   a = copy.copy(list_deque)
   while a:
        del a[-1]

def obj_pop(list_deque, size, obj_type):
    a = copy.copy(list_deque)
    while a:
        a.pop()

def obj_append(list_deque, size, obj_type):
    a = obj_type()
    for x in py_range(size):
        a.append(x)

def obj_insert(list_deque, size, obj_type):
    a = obj_type()
    for x in py_range(size):
        a.insert(0, x)


try:
    # assume python 2
    py_range = xrange
    PythonName = 'python2'
    extra_tests = None
except NameError:
    # we are running python 3
    py_range = range
    PythonName = 'python3'
    extra_tests = [('a.insert(0)', obj_insert)]

Tests = [('del a[0]', obj_del_start),
         ('del a[-1]', obj_del_end),
         ('a.pop()', obj_pop),
         ('a.append()', obj_append),
# added dynamically if exists
#         ('a.insert()', obj_insert),
        ]
if extra_tests:
    Tests.extend(extra_tests)

for (test_str, test) in Tests:
    print('    Doing "%s" on a list and deque using %s'
          % (test_str, PythonName))
    print('    %s' % ('-' * 65))
    for size in Sizes:
        aList = list(py_range(size)) 
        aDeque = collections.deque(py_range(size))
       
        start = time.time()
        test(aList, size, list)
        l_delta = time.time() - start
       
        start = time.time()
        test(aDeque, size, collections.deque)
        d_delta = time.time() - start
    
        print('    Size %7d: list took %10fs, deque took %fs'
              % (size, l_delta, d_delta))
    print('    %s' % ('-' * 65))
    print('')
