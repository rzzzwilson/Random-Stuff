#!/bin/env python
# -*- coding: utf-8 -*-

"""
A Ray class.
"""


class Ray(object):

    # number of decimal places used internally
    DefaultPlaces = 9

    def __init__(self, a=None, b=None):
        """Construct 'ray' object from two vectors.

        a  a vector defining the ray origin
        b  a vector showing the ray direction through the origin
        """

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

        return self.a + t * self.b

