#!/bin/env python
# -*- coding: utf-8 -*-

"""
A 3-vector class.
From chapter 2 of "Ray Tracing in One Weekend".
"""

import math


class Vec3(object):

    # number of decimal places used internally
    DefaultPlaces = 9

    def __init__(self, e0=0.0, e1=0.0, e2=0.0):
        """Construct vec3 from individual values.

        e0, e1, e2  float values that make up a vector
        """

        self.x = float(e0)
        self.y = float(e1)
        self.z = float(e2)

    def update(self, v):
        """Update Vec3 components."""

        (self.x, self.y, self.z) = (v.x, v.y, v.z)

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

        return Vec3(-self.x, -self.y, -self.z)

    def __abs__(self):
        """Implement the absolute value."""

        return self.length

    def __add__(self, other):
        """Implement A + B."""

        if isinstance(other, (int, float)):
            # add a float constant
            return Vec3(self.x + other, self.y + other, self.z + other)

        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        """Implement A - B."""

        if isinstance(other, (int, float)):
            # subtract a float constant
            return Vec3(self.x - other, self.y - other, self.z - other)

        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        """Implement A * B."""

        if isinstance(other, (int, float)):
            # multiply by a float constant
            return Vec3(self.x * other, self.y * other, self.z * other)

        return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)

    def __div__(self, other):
        """Implement A / B."""

        if isinstance(other, (int, float)):
            # divide by a float constant
            return Vec3(self.x / other, self.y / other, self.z / other)

        return Vec3(self.x / other.x, self.y / other.y, self.z / other.z)

    @property
    def length(self):
        """Return the vector length."""

        return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

    @property
    def squared_length(self):
        """Return the squared vector length."""

        return (self.x*self.x + self.y*self.y + self.z*self.z)

    def dot(self, other):
        """Return the dot product of two vectors."""

        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        """Return the cross product of two vectors."""

        return Vec3(  self.y * other.z - self.z * other.y,
                    -(self.x * other.z - self.z * other.x),
                      self.x * other.y - self.y * other.x)

    def __str__(self, places=DefaultPlaces):
        """Return a string representation."""

        places = 2
        return 'vec: (x=%.*f, y=%.*f, z=%.*f)' % (places, self.x, places, self.y, places, self.z)

    def __repr__(self):
        """Return a 'formal' string representation."""

        return 'Vec3(%.*f, %.*f, %.*f)' % (places, self.x, places, self.y, places, self.z)

    def __nonzero__(self):
        """Return 'truthiness' value of the vector."""

        return math.abs(math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)) >= 0.000000001

    def __iadd__(self, other):
        """Implement the '+=' operator."""

        if isinstance(other, (int, float)):
            # add a float constant
            return Vec3(self.x + other, self.y + other, self.z + other)

        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __isub__(self, other):
        """Implement the '-=' operator."""

        if isinstance(other, (int, float)):
            # subtract a float constant
            return Vec3(self.x - other, self.y - other, self.z - other)

        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __imul__(self, other):
        """Implement the '*=' operator."""

        if isinstance(other, (int, float)):
            # multiply by a float constant
            return Vec3(self.x * other, self.y * other, self.z * other)

        return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)

    def __idiv__(self, other):
        """Implement the '/=' operator."""

        if isinstance(other, (int, float)):
            # divide by a float constant
            return Vec3(self.x / other, self.y / other, self.z / other)

        return Vec3(self.x / other.x, self.y / other.y, self.z / other.z)

    @property
    def unit_vector(self):
        """Make a unit vector from the vector we have."""

        scale = 1.0 / self.length
        return Vec3(self.x*scale, self.y*scale, self.z*scale)
