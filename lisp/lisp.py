#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Implement the basic lisp functionality.
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

def quote(x):       # not a real 'quote'
    return x

def atom(x):
    return not callable(x)

def eq(x, y):
    return x == y

######
# Some extensions and helpers
######

def islist(x):
    return callable(x)

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
