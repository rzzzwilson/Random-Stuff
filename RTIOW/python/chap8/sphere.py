#!/bin/env python
# -*- coding: utf-8 -*-

"""
A Sphere class.
"""

from math import sqrt
from hitable import Hitable

class Sphere(Hitable):

    # number of decimal places used internally
    DefaultPlaces = 9

    def __init__(self, cen=None, r=None, material=None):
        """Define a sphere:

        cen  center Vec3
        r    radius
        """

        self.center = cen
        self.radius = r
        self.material = material

    def hit(self, r, t_min, t_max, rec):
        """Determine if the sphere has been hit.

        r      ray of interest
        t_min  minimum time of interest
        t_max  maximum time of interest
        rec    a hit record to update
        """

        oc = r.origin - self.center
        r_direction = r.direction
        a = r_direction.dot(r_direction)
        b = oc.dot(r_direction)
        c = oc.dot(oc) - self.radius*self.radius
        discriminant = b*b - a*c
        if discriminant > 0.0:
            temp = (-b - sqrt(b*b - a*c)) / a
            if temp < t_max and temp > t_min:
                rec.t = temp
                rec.p = r.point_at_parameter(temp)
                rec.normal = (rec.p - self.center) / self.radius
                rec.material = self.material
                return True
            temp = (-b + sqrt(b*b - a*c)) / a
            if temp < t_max and temp > t_min:
                rec.t = temp
                rec.p = r.point_at_parameter(temp)
                rec.normal = (rec.p - self.center) / self.radius
                rec.material = self.material
                return True
        return False
