#!/bin/env python
# -*- coding: utf-8 -*-

"""
A Lambertian material class.
"""

from material import Material
from utils import random_in_unit_sphere
from ray import Ray


class Lambertian(Material):

    def __init__(self, a):
        """Constructor.

        a  Vec3

        Albedo?
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

        target = rec.p + rec.normal + random_in_unit_sphere()
        scattered.update(rec.p, target-rec.p)
        attenuation.update(self.albedo.x, self.albedo.y, self.albedo.z)

        return True
