#!/bin/env python
# -*- coding: utf-8 -*-

"""
A simple program to write a PPM file.

From chapter 3 of "Ray Tracing in One Weekend".
Uses the Ray and Vec3 classes.
"""

import vec3
import ray

def color(r):
    unit_direction = r.direction.unit_vector()
    t = 0.5 * (unit_direction.y + 1.0)
    return (1.0 - t) * vec3.Vec3((1.0, 1.0, 1.0)) * t * vec3.Vec3((0.5, 0.7, 1.0))

nx = 200
ny = 100

print('P3\n%d %d 255' % (nx, ny))

lower_left_corner = vec3.Vec3((-2.0, -1.0, -1.0))
horizontal = vec3.Vec3((4.0, 0.0, 0.0))
vertical = vec3.Vec3((0.0, 2.0, 0.0))
origin = vec3.Vec3((0.0, 0.0, 0.))

for j in range(ny)[::-1]:
    for i in range(nx):
        u = float(i) / float(nx)
        v = float(j) / float(ny)
        r = ray.Ray(origin, lower_left_corner + u * horizontal + v * vertical)
        col = color(r)
        ir = int(255.99 * col[0])
        ig = int(255.99 * col[1])
        ib = int(255.99 * col[2])

        print('%d %d %d' % (ir, ig, ib))
