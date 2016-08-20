#!/bin/env python
# -*- coding: utf-8 -*-

"""
A simple program to write a PPM file.
From chapter 6 of "Ray Tracing in One Weekend".
Antialiasing.
"""

import sys
from math import sqrt
from random import random

from vec3 import Vec3
from hitable import Hitable, HitRecord
from hitable_list import HitableList
from sphere import Sphere
from camera import Camera

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
ns = 100

print('P3\n%d %d 255' % (nx, ny))

#lower_left_corner = Vec3(-2.0, -1.0, -1.0)
#horizontal = Vec3(4.0, 0.0, 0.0)
#vertical = Vec3(0.0, 2.0, 0.0)
#origin = Vec3(0.0, 0.0, 0.0)

hlist = [Sphere(Vec3(0.0, 0.0, -1.0), 0.5), Sphere(Vec3(0.0, -100.5, -1.0), 100.0)]
world = HitableList(hlist)

cam = Camera()

for j in range(ny)[::-1]:
    for i in range(nx):
        col = Vec3(0.0, 0.0, 0.0)
        for s in range(ns):
            u = (float(i) + random()) / float(nx)
            v = (float(j) + random()) / float(ny)
            r = cam.get_ray(u, v)
            p = r.point_at_parameter(2.0)
            col += color(r, world)

        col /= float(ns)

        ir = int(255.99 * col.r)
        ig = int(255.99 * col.g)
        ib = int(255.99 * col.b)

        print('%d %d %d' % (ir, ig, ib))
