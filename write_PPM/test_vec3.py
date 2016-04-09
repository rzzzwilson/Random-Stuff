#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module to test the Vec3 class.
"""

import vec3
import math
import unittest


class TestVec3(unittest.TestCase):

    def test_vec3_simple_create(self):
        """Check a simple Vec3 creation."""

        v = vec3.Vec3()

        msg = 'X component should be None, got %s' % str(v.x)
        self.assertEqual(v.x, None, msg)
        msg = 'X component should equal R component, got x=%s, r=%s' % (str(v.x), str(v.r))
        self.assertEqual(v.x, v.r, msg)

        msg = 'Y component should be None, got %s' % str(v.y)
        self.assertEqual(v.y, None, msg)
        msg = 'Y component should equal G component, got x=%s, r=%s' % (str(v.y), str(v.g))
        self.assertEqual(v.y, v.g, msg)

        msg = 'Z component should be None, got %s' % str(v.z)
        self.assertEqual(v.z, None, msg)
        msg = 'Z component should equal B component, got x=%s, r=%s' % (str(v.z), str(v.b))
        self.assertEqual(v.z, v.b, msg)

    def test_vec3_simple_create2(self):
        """Check a simple Vec3 creation."""

        given = (1, 2, 3)
        v = vec3.Vec3(given)

        expect = given[0]
        msg = 'X component should be %s, got %s' % (str(expect), str(v.x))
        self.assertEqual(v.x, expect, msg)
        msg = 'X component should equal R component, got x=%s, r=%s' % (str(v.x), str(v.r))
        self.assertEqual(v.x, v.r, msg)

        expect = given[1]
        msg = 'Y component should be %s, got %s' % (str(expect), str(v.y))
        self.assertEqual(v.y, expect, msg)
        msg = 'Y component should equal G component, got x=%s, r=%s' % (str(v.y), str(v.g))
        self.assertEqual(v.y, v.g, msg)

        expect = given[2]
        msg = 'Z component should be %s, got %s' % (str(expect), str(v.z))
        self.assertEqual(v.z, expect, msg)
        msg = 'Z component should equal B component, got x=%s, r=%s' % (str(v.z), str(v.b))
        self.assertEqual(v.z, v.b, msg)

    def test_vec3_unary_plus(self):
        """Check unary plus of Vec3."""

        given = (1, 2, 3)
        v = vec3.Vec3(given)

        v2 = +v

        msg = "v should equal +v, got v=%s, +v=%s" % (str(v), str(v2))
        self.assertEqual(str(v), str(v2), msg)

    def test_vec3_binary_plus(self):
        """Check binary plus of Vec3."""

        given = (1, 2, 3)
        v1 = vec3.Vec3(given)

        given2 = (1, 2, 3)
        v2 = vec3.Vec3(given2)

        expect = (given[0]+given2[0], given[1]+given2[1], given[2]+given2[2])
        ve = vec3.Vec3(expect)

        vsum = v1 + v2

        msg = "v1 + v2 should equal %s + %s =%s, got %s" % (str(v1), str(v2), str(ve), str(vsum))
        self.assertEqual(str(vsum), str(ve), msg)

    def test_vec3_binary_plus2(self):
        """Check binary plus of Vec3."""

        given = (1.1, 2.2, 3.3)
        v1 = vec3.Vec3(given)

        given2 = (-1.2, -2.3, -3.4)
        v2 = vec3.Vec3(given2)

        expect = (given[0]+given2[0], given[1]+given2[1], given[2]+given2[2])
        ve = vec3.Vec3(expect)

        vsum = v1 + v2

        msg = "v1 + v2 should equal %s + %s =%s, got %s" % (str(v1), str(v2), str(ve), str(vsum))
        self.assertEqual(str(vsum), str(ve), msg)

    def test_vec3_unary_minus(self):
        """Check unary minus of Vec3."""

        given = (1, 2, 3)
        v1 = vec3.Vec3(given)

        expect = (-given[0], -given[1], -given[2])
        ve = vec3.Vec3(expect)

        v2 = -v1

        msg = "v2 = -v1 should equal %s, got %s" % (str(expect), str(v2))
        self.assertEqual(str(v2), str(ve), msg)

    def test_vec3_len(self):
        """Check len() function on Vec3."""

        #given = (3, 4, 5)
        given = (1, 1, 1)
        v = vec3.Vec3(given)

        expect = math.sqrt(given[0]**2 + given[1]**2 + given[2]**2)

        print('len(v)=%s' % str(len(v)))

        msg = "len(v1) should be %.2f, got %.2f" % (expect, len(v))
        self.assertEqual(expect, len(v), msg)

if __name__ == '__main__':
    suite = unittest.makeSuite(TestVec3, 'test')
    runner = unittest.TextTestRunner()
    runner.run(suite)
