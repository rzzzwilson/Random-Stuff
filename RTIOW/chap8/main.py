#!/bin/env python
# -*- coding: utf-8 -*-

"""
A simple program to write a PPM file.
From chapter 8 of "Ray Tracing in One Weekend".
Metal.
"""

import sys
from math import sqrt
from random import random

from vec3 import Vec3
from ray import Ray
from hitable import Hitable, HitRecord
from hitable_list import HitableList
from sphere import Sphere
from camera import Camera
from lambertian import Lambertian
from metal import Metal


def color(r, world, depth):
    """Get colour from vector.

    r      the ray of interest
    world  hitable list
    depth  ??
    """

    rec = HitRecord()
    if world.hit(r, 0.001, sys.float_info.max, rec):
        scattered = Ray(None, None)
        attenuation = Vec3(0.5, 0.5, 0.5)
        if depth < 50 and rec.material.scatter(r, rec, attenuation, scattered):
            return attenuation * color(scattered, world, depth+1)
        else:
            return Vec3(0.0, 0.0, 0.0)
    else:
        unit_direction = r.direction.unit_vector()
        t = (unit_direction.y + 1.0) * 0.5
        return Vec3(1.0, 1.0, 1.0) * (1.0 - t) + Vec3(0.5, 0.7, 1.0) * t

nx = 200
ny = 100
ns = 100

print('P3\n%d %d 255' % (nx, ny))

sphere1 = Sphere(Vec3(0.0, 0.0, -1.0), 0.5, Lambertian(Vec3(0.8, 0.3, 0.3)))
sphere2 = Sphere(Vec3(0.0, -100.5, -1.0), 100.0, Lambertian(Vec3(0.8, 0.8, 0.0)))
sphere3 = Sphere(Vec3(1.0, 0.0, -1.0), 0.5, Metal(Vec3(0.8, 0.6, 0.2)))
sphere4 = Sphere(Vec3(-1.0, 0.0, -1.0), 0.5, Metal(Vec3(0.8, 0.8, 0.8)))

hlist = [sphere1, sphere2, sphere3, sphere4]
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
            col += color(r, world, 0.0)

        col /= float(ns)
        col = Vec3(sqrt(col.r), sqrt(col.g), sqrt(col.b))

        ir = int(255.99 * col.r)
        ig = int(255.99 * col.g)
        ib = int(255.99 * col.b)

        print('%d %d %d' % (ir, ig, ib))
