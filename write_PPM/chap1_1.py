#!/bin/env python
# -*- coding: utf-8 -*-

"""
A simple program to write a PPM file.
"""

nx = 200
ny = 100

print('P3\n%d %d 255' % (nx, ny))

for j in range(ny)[::-1]:
    for i in range(nx):
        r = float(i) / float(nx)
        g = float(j) / float(ny)
        b = 0.2

        ir = int(255.99 * r)
        ig = int(255.99 * g)
        ib = int(255.99 * b)

        print('%d %d %d' % (ir, ig, ib))
