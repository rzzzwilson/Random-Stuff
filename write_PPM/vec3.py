#!/bin/env python
# -*- coding: utf-8 -*-

"""
A 3-vector class.
"""

import math


class Vec3(object):

    def __init__(self, e=None):
        """Construct vec3.

        e  is a 3-tuple of components, if supplied
        """

        self.e = e
        (x, y, z) = e

    @property
    def x(self):
        """Return the X component of the vector."""

        return self.x

    @property
    def y(self):
        """Return the Y component of the vector."""

        return self.y

    @property
    def z(self):
        """Return the Z component of the vector."""

        return self.z
    
    @property
    def r(self):
        """Return the R component of the vector."""

        return self.x

    @property
    def g(self):
        """Return the G component of the vector."""

        return self.y

    @property
    def b(self):
        """Return the B component of the vector."""

        return self.z

    def __pos__(self):
        """Implement the unary +."""

        return self

    def __neg__(self):
        """Implement the unary -."""
                
        return Vec3((-self.x, -self.y, -self.z))

    def __getitem__(self, i):
        """return vec3[i]."""

        return self.e[i]

    def __add__(self, other):
        """Implement A + B."""

        return Vec3((self.x + other.x, self.y + other.y, self.z + other.z))

    def __len__(self):
        """Return the vector length."""

        return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

    def squere_len(self):
        """Return the squared vector length."""

        return (self.x*self.x + self.y*self.y + self.z*self.z)

    def __str__(self):
        """Return a string representation."""

        return '%.2f, %.2f, %.2f' % (self.x, self.y, self.z)

    def make_unit_vector(self):

