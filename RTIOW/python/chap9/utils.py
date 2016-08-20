#!/bin/env python
# -*- coding: utf-8 -*-

"""
Various utility functions.
"""

from random import random

from vec3 import Vec3

# number of decimal places used internally
DefaultPlaces = 9


def random_in_unit_sphere():
    """Return a random vector in the unit sphere."""

    while True:
        p = Vec3(random(), random(), random()) * 2.0 - Vec3(1.0, 1.0, 1.0)
        if p.squared_length <= 1.0:
            return p
