#!/bin/env python
# -*- coding: utf-8 -*-

"""
A 3-vector class.
"""

import math


class Vec3(object):

    def __init__(self, v=None):
        """Construct vec3 from a vector tuple.

        v  is a 3-tuple of components, if not None
        """

        self.v = v

        if v:
            (self.x, self.y, self.z) = v
            self.x = float(self.x)
            self.y = float(self.y)
            self.z = float(self.z)
        else:
            self.x = None
            self.y = None
            self.z = None

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

    def __abs__(self):
        """Implement the absolute value."""
                
        return self.length

    def __getitem__(self, i):
        """return vec3[i]."""

        return self.e[i]

    def __add__(self, other):
        """Implement A + B."""

        return Vec3((self.x + other.x, self.y + other.y, self.z + other.z))

    def __sub__(self, other):
        """Implement A - B."""

        return Vec3((self.x - other.x, self.y - other.y, self.z - other.z))

    def __mul__(self, other):
        """Implement A * B."""

        return Vec3((self.x * other.x, self.y * other.y, self.z * other.z))

    def __div__(self, other):
        """Implement A / B."""

        return Vec3((self.x / other.x, self.y / other.y, self.z / other.z))

    @property
    def length(self):
        """Return the vector length."""

        return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

    @property
    def square_length(self):
        """Return the squared vector length."""

        return (self.x*self.x + self.y*self.y + self.z*self.z)

    def dot(self, other):
        """Return the dot product of two vectors."""

        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        """Return the cross product of two vectors."""

        return Vec3((  self.y * other.z - self.z * other.y,
                     -(self.x * other.z - self.z * other.x),
                       self.x * other.y - self.y * other.x))

    def __str__(self):
        """Return a string representation."""

        return '%.2f %.2f %.2f' % (self.x, self.y, self.z)

    def __repr__(self):
        """Return a 'formal' string representation."""

        return 'Vec3((%.2f, %.2f, %.2f))' % (self.x, self.y, self.z)

    def __nonzero__(self):
        """Return 'truthiness' value of the vector."""

        if math.abs(math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)) >= 0.000000001:
            return True
        return False

    def unit_vector(self):
        """Make a unit vector from the vector we have."""

        scale = 1.0 / self.length
        return Vec3((self.x*scale, self.y*scale, self.z*scale))
