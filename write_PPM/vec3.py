#!/bin/env python
# -*- coding: utf-8 -*-

"""
A 3-vector class.
"""

class vec3(object):

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

    def __getitem__(self, i):
        """return vec3[i]."""

        return self.e[i]
