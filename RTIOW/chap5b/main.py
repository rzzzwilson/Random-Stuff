#!/bin/env python
# -*- coding: utf-8 -*-

"""
A simple program to write a PPM file.

From chapter 5 of "Ray Tracing in One Weekend".
Surface normals ans multiple objects.
"""

import sys
from math import sqrt

from vec3 import Vec3
from ray import Ray
from hitable import Hitable, HitRecord
from hitable_list import HitableList
from sphere import Sphere


def color(r, world):
    """Get colour from vector.

    r      the ray of interest
    world  hitable list
    """

    rec = HitRecord()
    if world.hit(r, 0.0, sys.float_info.max, rec):
        return Vec3(rec.normal.x + 1.0, rec.normal.y + 1.0, rec.normal.z + 1.0) * 0.5
    else:
        unit_direction = r.direction.unit_vector()
        t = 0.5 * (unit_direction.y + 1.0)
        return Vec3(1.0, 1.0, 1.0) * (1.0 - t) + Vec3(0.5, 0.7, 1.0) * t

nx = 200
ny = 100

print('P3\n%d %d 255' % (nx, ny))

lower_left_corner = Vec3(-2.0, -1.0, -1.0)
horizontal = Vec3(4.0, 0.0, 0.0)
vertical = Vec3(0.0, 2.0, 0.0)
origin = Vec3(0.0, 0.0, 0.0)

hlist = [Sphere(Vec3(0.0, 0.0, -1.0), 0.5), Sphere(Vec3(0.0, -100.5, -1.0), 100.0)]
world = HitableList(hlist)

for j in range(ny)[::-1]:
    for i in range(nx):
        u = float(i) / float(nx)
        v = float(j) / float(ny)
        r = Ray(origin, lower_left_corner + horizontal * u + vertical * v)

        p = r.point_at_parameter(2.0)
        col = color(r, world)
        ir = int(255.99 * col.r)
        ig = int(255.99 * col.g)
        ib = int(255.99 * col.b)

        print('%d %d %d' % (ir, ig, ib))
