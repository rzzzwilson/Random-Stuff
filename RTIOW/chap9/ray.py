#!/bin/env python
# -*- coding: utf-8 -*-

"""
A Ray class.
From chapter 3 of "Ray Tracing in One Weekend".
"""

from utils import DefaultPlaces


class Ray(object):

    def __init__(self, a=None, b=None):
        """Construct 'ray' object from two vectors.

        a  a vector defining the ray origin
        b  a vector showing the ray direction from the origin
        """

        self.a = a
        self.b = b

    def update(self, a, b):
        """Update Ray a and b components."""

        self.a = a
        self.b = b

    @property
    def origin(self):
        """Return the origin of the ray."""

        return self.a

    @property
    def direction(self):
        """Return the direction of the ray"""

        return self.b

    def point_at_parameter(self, t):
        """Return the parameterised position from 'a' in the direction of 'b'."""

        return self.a + self.b * t

    def __str__(self, places=DefaultPlaces):
        """Return a string representation."""

        return ('origin=(%.*f %.*f %.*f) direction=(%.*f %.*f %.*f)'
                % (self.places, self.a.x, self.places, self.a.y, self.places, self.a.z,
                   self.places, self.b.x, self.places, self.b.y, self.places, self.b.z))

