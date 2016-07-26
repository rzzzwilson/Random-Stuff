#!/bin/env python
# -*- coding: utf-8 -*-

"""
A simple program to write a PPM file.

From chapter 5 of "Ray Tracing in One Weekend".
Surface normals ans multiple objects.
"""

from math import sqrt
from vec3 import Vec3
import ray

def hit_sphere(center, radius, r):
    """Decide if ray 'r' intersects a sphere."""

    oc = r.origin - center
    a = r.direction.dot(r.direction)
    b = oc.dot(r.direction)*2.0
    c = oc.dot(oc) - radius*radius
    discriminant = b*b - a*c*4
    if discriminant < 0.0:
        return -1.0

    return (-b - sqrt(discriminant)) / (a*2.0)

def color(r):
    """Get colour from vector.

    We decide if we hit the sphere.
    """

    t = hit_sphere(Vec3((0, 0, -1)), 0.5, r)
    if t > 0.0:
        N = (r.point_at_parameter(t) - Vec3((0, 0, -1))).unit_vector()
        return Vec3((N.x+1, N.y+1, N.z+1)) * 0.5

    unit_direction = r.direction.unit_vector()
    t = (unit_direction.y + 1.0) * 0.5
    return Vec3((1.0, 1.0, 1.0)) * (1.0 - t) + Vec3((0.5, 0.7, 1.0)) * t

nx = 200
ny = 100

print('P3\n%d %d 255' % (nx, ny))

lower_left_corner = Vec3((-2.0, -1.0, -1.0))
horizontal = Vec3((4.0, 0.0, 0.0))
vertical = Vec3((0.0, 2.0, 0.0))
origin = Vec3((0.0, 0.0, 0.))

for j in range(ny)[::-1]:
    for i in range(nx):
        u = float(i) / float(nx)
        v = float(j) / float(ny)
        r = ray.Ray(origin, lower_left_corner + horizontal * u + vertical * v)
        col = color(r)
        ir = int(255.99 * col.r)
        ig = int(255.99 * col.g)
        ib = int(255.99 * col.b)

        print('%d %d %d' % (ir, ig, ib))
