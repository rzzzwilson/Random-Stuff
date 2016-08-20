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

    def __init__(self, a, f):
        """Constructor.

        a  Vec3
        f  the fuzz
        """

        self.a = a
        self.albedo = a
        self.fuzz = f if f < 1.0 else 1

    def scatter(self, r_in, rec, attenuation, scattered):
        """Scatter from the material in a Lambertian way.

        r_in         input Ray
        rec          hit record(s)
        attenuation  attenuation Vec3
        scattered    Ray object to update

        Returns True if scattered.
        """

        reflected = reflect(r_in.direction.unit_vector, rec.normal)

        scattered.update(rec.p, reflected+random_in_unit_sphere()*self.fuzz)
        attenuation.update(self.albedo)

        return scattered.direction.dot(rec.normal) > 0.0
