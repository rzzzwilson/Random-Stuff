#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Implement the cons/car/cdr functionality.
"""

######
# The "lisp" primitives
######

def cons(x, y):
    return lambda m: m(x, y)

def car(z):
    return z(lambda p, q: p)

def cdr(z):
    return z(lambda p, q: q)

def islist(x):
    return callable(x)

######
# Some extensions and helpers
######

def list_eq(x, y):
    if islist(x) and islist(y):
        return (car(x) == car(y)) and list_eq(cdr(x), cdr(y))
    return x == y

def list_print(str, x):
    print('%s: (' % str, end='')
    x_list_print(x)
    print(')')
    
def x_list_print(x):
    if callable(x):
        print('(', end='')
        x_list_print(car(x))
        x_list_print(cdr(x))
        print(')', end='')
    else:
        print(str(x), end='')
