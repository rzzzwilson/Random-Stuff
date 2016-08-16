#!/bin/env python
# -*- coding: utf-8 -*-

"""
A Hitable class.
"""


class HitRecord(object):

    def __init__(self, t=None, p=None, normal=None, material=None):
        self.t = t
        self.p = p
        self.normal = normal
        self.material = material


class Hitable(object):

    # number of decimal places used internally
    DefaultPlaces = 9

    def hit(self, r, t_min, t_max, rec):
        """See if this object has been hit.

        r    ray of interest
        t_min  minimum time of interest
        t_max  maximum time of interest
        rec    hit record(s)
        """

        raise Exception('Virtual method Hitable.hit() has not been overridden!?')
