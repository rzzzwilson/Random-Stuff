#!/bin/env python
# -*- coding: utf-8 -*-

"""
A metal material class.
"""

from material import Material
from utils import random_in_unit_sphere
from ray import Ray


def reflect(v, n):
    """Calculate a ray reflection.

    v  the initial Vec3 ray
    n  the Vec3 normal to the surface

    Returns a Vec3 reflected ray.
    """

    return v - n*v.dot(n)*2

class Metal(Material):

    def __init__(self, a):
        """Constructor.

        a  Vec3
        """

        self.a = a
        self.albedo = a

    def scatter(self, r_in, rec, attenuation, scattered):
        """Scatter from the material in a Lambertian way.

        r_in         input Ray
        rec          hit record(s)
        attenuation  attenuation Vec3
        scattered    Ray object to update

        Returns True if scattered.
        """

        reflected = reflect(r_in.direction.unit_vector(), rec.normal)

        #target = rec.p + rec.normal + random_in_unit_sphere()
        #scattered.update(rec.p, target - rec.p)
        scattered.update(rec.p, reflected)
        attenuation.update(self.albedo.x, self.albedo.y, self.albedo.z)

        return scattered.direction.dot(rec.normal) > 0.0
