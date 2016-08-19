#!/bin/env python
# -*- coding: utf-8 -*-

"""
A material abstract class.
From chapter 8 of "Ray Tracing in One Weekend".
"""

class Material(object):

    def scatter(self, r_in, rec, attenuation, scattered):
        """Scatter from the material.

        r_in         input Ray
        rec          hit record(s)
        attenuation  attenuation Vec3
        scattered    Ray object to update
        """

        raise Exception('Material.scatter() method not overridden!?')
