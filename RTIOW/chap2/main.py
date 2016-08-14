#!/bin/env python
# -*- coding: utf-8 -*-

"""
A simple program to write a PPM file.
From chapter 2 of "Ray Tracing in One Weekend".
"""

from vec3 import Vec3

nx = 200
ny = 100

print('P3\n%d %d 255' % (nx, ny))

for j in range(ny)[::-1]:
    for i in range(nx):
        col = Vec3(float(i)/float(nx), float(j)/float(ny), 0.2)

        ir = int(col.r * 255.99)
        ig = int(col.g * 255.99)
        ib = int(col.b * 255.99)

        print('%d %d %d' % (ir, ig, ib))
