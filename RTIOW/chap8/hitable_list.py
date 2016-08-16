#!/bin/env python
# -*- coding: utf-8 -*-

"""
A Hitable collection class.
"""

from hitable import Hitable, HitRecord
#from vec3 import *

class HitableList(Hitable):

    def __init__(self, l=None):
        """Define a Hitable list:

        l  a list of hitable objects
        """

        self.hlist = l

    def hit(self, r, t_min, t_max, rec):
        """Determine if the object has been hit.

        r      ray of interest
        t_min  minimum time of interest
        t_max  maximum time of interest
        rec    a hit record to update
        """

        temp_rec = HitRecord()
        hit_anything = False
        closest_so_far = t_max

        for i in self.hlist:
            if i.hit(r, t_min, closest_so_far, temp_rec):
                hit_anything = True
                closest_so_far = temp_rec.t
                (rec.t, rec.p, rec.normal, rec.material) = (temp_rec.t, temp_rec.p, temp_rec.normal, i.material)

        return hit_anything
