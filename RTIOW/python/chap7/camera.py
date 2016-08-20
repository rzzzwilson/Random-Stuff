#!/bin/env python
# -*- coding: utf-8 -*-

"""
A Camera class.
From Chapter 6 of "Ray Tracing in one Weekend".
"""

from vec3 import Vec3
from ray import Ray


class Camera(object):

    # number of decimal places used internally
    DefaultPlaces = 9

    def __init__(self):
        """A camera clas."""

        self.origin = Vec3(0.0, 0.0, 0.0)
        self.lower_left_corner = Vec3(-2.0, -1.0, -1.0)
        self.horizontal = Vec3(4.0, 0.0, 0.0)
        self.vertical = Vec3(0.0, 2.0, 0.0)

    def get_ray(self, u, v):
        return Ray(self.origin, self.lower_left_corner + self.horizontal*u
                   + self.vertical*v - self.origin)
