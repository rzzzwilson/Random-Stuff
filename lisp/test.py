#!/usr/bin/env python

"""
Little test code to see if we can implement cons/car/cdr
in a very functional and elemental way.
"""

def cons(x, y):
    return lambda m: m(x, y)

def car(z):
    return z(lambda p, q: p)

def cdr(z):
    return z(lambda p, q: q)

def islist(x):
    return callable(x)

def list_eq(x, y):
    if islist(x) and islist(y):
        return (car(x) == car(y)) and list_eq(cdr(x), cdr(y))
    return x == y

def list_print(str, x):
    print '%s: (' % str,
    x_list_print(x)
    print ')'
    
def x_list_print(x):
    if callable(x):
        print '(',
        x_list_print(car(x))
        x_list_print(cdr(x))
        print ')',
    else:
        print str(x),

a = cons(1, 2)
b = cons(a, 3)
list_print('b', b)
c = cons(10, 20)
d = cons(b, c)
list_print('d', d)

x = car(a)
assert x == 1
x = cdr(a)
assert x == 2
x = car(b)
print('x=%s' % str(x))
assert x == 1
x = cdr(b)
assert x == cons(2, 3)
