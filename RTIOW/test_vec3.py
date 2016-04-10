#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module to test the Vec3 class.
"""

import vec3
import math
import unittest


# number of significant places for comparisons
Places = 7


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

    def test_vec3_unary_minus(self):
        """Check unary minus of Vec3."""

        given = (1, 2, 3)
        v1 = vec3.Vec3(given)

        expect = (-given[0], -given[1], -given[2])
        ve = vec3.Vec3(expect)

        v2 = -v1

        msg = "v2 = -v1 should equal %s, got %s" % (str(expect), str(v2))
        self.assertEqual(str(v2), str(ve), msg)

    def test_vec3_binary_minus(self):
        """Check binary minus of Vec3."""

        given = (1, 2, 3)
        v1 = vec3.Vec3(given)

        given2 = (1, 2, 3)
        v2 = vec3.Vec3(given2)

        expect = (given[0]-given2[0], given[1]-given2[1], given[2]-given2[2])
        ve = vec3.Vec3(expect)

        vsum = v1 - v2

        msg = "v1 + v2 should equal %s + %s = %s, got %s" % (str(v1), str(v2), str(ve), str(vsum))
        self.assertEqual(str(vsum), str(ve), msg)

    def test_vec3_binary_minus2(self):
        """Check binary minus of Vec3."""

        given = (1, 2, 3)
        v1 = vec3.Vec3(given)

        given2 = (-1.1, 2.2, -3.9)
        v2 = vec3.Vec3(given2)

        expect = (given[0]-given2[0], given[1]-given2[1], given[2]-given2[2])
        ve = vec3.Vec3(expect)

        vsum = v1 - v2

        msg = "v1 + v2 should equal %s + %s = %s, got %s" % (str(v1), str(v2), str(ve), str(vsum))
        self.assertEqual(str(vsum), str(ve), msg)

    def test_vec3_length(self):
        """Check length() function on Vec3."""

        given = (1, 1, 1)
        v = vec3.Vec3(given)

        expect = math.sqrt(given[0]**2 + given[1]**2 + given[2]**2)
        len_v = v.length

        msg = "len(v) should be %.*f, got %.*f" % (Places, expect, Places, len_v)
        self.assertAlmostEqual(expect, len_v, msg=msg, places=Places)

    def test_vec3_length2(self):
        """Check length() function on Vec3."""

        given = (0, 0, 0)
        v = vec3.Vec3(given)

        expect = math.sqrt(given[0]**2 + given[1]**2 + given[2]**2)
        len_v = v.length

        msg = "len(v) should be %.*f, got %.*f" % (Places, expect, Places, len_v)
        self.assertAlmostEqual(expect, len_v, msg=msg, places=Places)

    def test_vec3_square_length(self):
        """Check square_length() function on Vec3."""

        given = (1, 1, 1)
        v = vec3.Vec3(given)

        expect = given[0]**2 + given[1]**2 + given[2]**2
        len_v = v.square_length

        msg = "len(v) should be %.*f, got %.*f" % (Places, expect, Places, len_v)
        self.assertAlmostEqual(expect, len_v, msg=msg, places=Places)

    def test_vec3_square_length2(self):
        """Check square_length() function on Vec3."""

        given = (0, 0, 0)
        v = vec3.Vec3(given)

        expect = given[0]**2 + given[1]**2 + given[2]**2
        len_v = v.square_length

        msg = "len(v) should be %.*f, got %.*f" % (Places, expect, Places, len_v)
        self.assertAlmostEqual(expect, len_v, msg=msg, places=Places)

    def test_vec3_binary_add(self):
        """Check binary add operation on Vec3."""

        v1_given = (0, 0, 0)
        v1 = vec3.Vec3(v1_given)

        v2_given = (0, 0, 0)
        v2 = vec3.Vec3(v2_given)

        v1plus2 = v1 + v2

        expect_given = (v1_given[0] + v2_given[0], v1_given[1] + v2_given[1], v1_given[2] + v2_given[2])
        expect = vec3.Vec3(expect_given)

        msg = "Vec3(%s) + Vec3(%s) should be %s, got %s" % (str(v1_given), str(v2_given), str(expect_given), str(v1plus2))
        expect_tuple = (expect.x, expect.y, expect.z)
        v1plus2_tuple = (v1plus2.x, v1plus2.y, v1plus2.z)
        self.assertAlmostEqual(expect_tuple, v1plus2_tuple, msg=msg, places=Places)

    def test_vec3_binary_add2(self):
        """Check binary add operation on Vec3."""

        v1_given = (1, 2, 3)
        v1 = vec3.Vec3(v1_given)

        v2_given = (1, 2, 3)
        v2 = vec3.Vec3(v2_given)

        v1plus2 = v1 + v2

        expect_given = (v1_given[0] + v2_given[0], v1_given[1] + v2_given[1], v1_given[2] + v2_given[2])
        expect = vec3.Vec3(expect_given)

        msg = "Vec3(%s) + Vec3(%s) should be %s, got %s" % (str(v1_given), str(v2_given), str(expect_given), str(v1plus2))
        expect_tuple = (expect.x, expect.y, expect.z)
        v1plus2_tuple = (v1plus2.x, v1plus2.y, v1plus2.z)
        self.assertAlmostEqual(expect_tuple, v1plus2_tuple, msg=msg, places=Places)

    def test_vec3_binary_add3(self):
        """Check binary add operation on Vec3."""

        v1_given = (1, 2, 3)
        v1 = vec3.Vec3(v1_given)

        v2_given = (-1, -2, -3)
        v2 = vec3.Vec3(v2_given)

        v1plus2 = v1 + v2

        expect_given = (v1_given[0] + v2_given[0], v1_given[1] + v2_given[1], v1_given[2] + v2_given[2])
        expect = vec3.Vec3(expect_given)

        msg = "Vec3(%s) + Vec3(%s) should be %s, got %s" % (str(v1_given), str(v2_given), str(expect_given), str(v1plus2))
        expect_tuple = (expect.x, expect.y, expect.z)
        v1plus2_tuple = (v1plus2.x, v1plus2.y, v1plus2.z)
        self.assertAlmostEqual(expect_tuple, v1plus2_tuple, msg=msg, places=Places)

    def test_vec3_binary_subtract(self):
        """Check binary subtract operation on Vec3."""

        v1_given = (0, 0, 0)
        v1 = vec3.Vec3(v1_given)

        v2_given = (0, 0, 0)
        v2 = vec3.Vec3(v2_given)

        v1plus2 = v1 - v2

        expect_given = (v1_given[0] - v2_given[0], v1_given[1] - v2_given[1], v1_given[2] - v2_given[2])
        expect = vec3.Vec3(expect_given)

        msg = "Vec3(%s) - Vec3(%s) should be %s, got %s" % (str(v1_given), str(v2_given), str(expect_given), str(v1plus2))
        expect_tuple = (expect.x, expect.y, expect.z)
        v1plus2_tuple = (v1plus2.x, v1plus2.y, v1plus2.z)
        self.assertAlmostEqual(expect_tuple, v1plus2_tuple, msg=msg, places=Places)

    def test_vec3_binary_subtract2(self):
        """Check binary subtract operation on Vec3."""

        v1_given = (0, 0, 0)
        v1 = vec3.Vec3(v1_given)

        v2_given = (1.1, 2.2, 3.3)
        v2 = vec3.Vec3(v2_given)

        v1plus2 = v1 - v2

        expect_given = (v1_given[0] - v2_given[0], v1_given[1] - v2_given[1], v1_given[2] - v2_given[2])
        expect = vec3.Vec3(expect_given)

        msg = "Vec3(%s) - Vec3(%s) should be %s, got %s" % (str(v1_given), str(v2_given), str(expect_given), str(v1plus2))
        expect_tuple = (expect.x, expect.y, expect.z)
        v1plus2_tuple = (v1plus2.x, v1plus2.y, v1plus2.z)
        self.assertAlmostEqual(expect_tuple, v1plus2_tuple, msg=msg, places=Places)

    def test_vec3_binary_subtract3(self):
        """Check binary subtract operation on Vec3."""

        v1_given = (1.1, 2.2, 3.3)
        v1 = vec3.Vec3(v1_given)

        v2_given = (0.1, 0.2, 0.3)
        v2 = vec3.Vec3(v2_given)

        v1plus2 = v1 - v2

        expect_given = (v1_given[0] - v2_given[0], v1_given[1] - v2_given[1], v1_given[2] - v2_given[2])
        expect = vec3.Vec3(expect_given)

        msg = "Vec3(%s) - Vec3(%s) should be %s, got %s" % (str(v1_given), str(v2_given), str(expect_given), str(v1plus2))
        expect_tuple = (expect.x, expect.y, expect.z)
        v1plus2_tuple = (v1plus2.x, v1plus2.y, v1plus2.z)
        self.assertAlmostEqual(expect_tuple, v1plus2_tuple, msg=msg, places=Places)

    def test_vec3_binary_multiply(self):
        """Check binary multiply operation on Vec3."""

        given = (1, 2, 3)
        v1 = vec3.Vec3(given)

        given2 = (-1.1, 2.2, -3.9)
        v2 = vec3.Vec3(given2)

        expect = (given[0]*given2[0], given[1]*given2[1], given[2]*given2[2])
        ve = vec3.Vec3(expect)

        vmul = v1 * v2

        msg = "Vec3(%s) * Vec3(%s) should be %s, got %s" % (str(v1), str(v2), str(ve), str(vmul))
        self.assertEqual(str(vmul), str(ve), msg)

    def test_vec3_binary_multiply2(self):
        """Check binary multiply operation on Vec3."""

        given = (1, 2, 3)
        v1 = vec3.Vec3(given)

        given2 = (1, 0, -1)
        v2 = vec3.Vec3(given2)

        expect = (given[0]*given2[0], given[1]*given2[1], given[2]*given2[2])
        ve = vec3.Vec3(expect)

        vmul = v1 * v2

        msg = "Vec3(%s) * Vec3(%s) should be %s, got %s" % (str(v1), str(v2), str(ve), str(vmul))
        self.assertEqual(str(vmul), str(ve), msg)

    def test_vec3_binary_divide(self):
        """Check binary divide operation on Vec3."""

        v1_given = (1.1, 2.2, 3.3)
        v1 = vec3.Vec3(v1_given)

        v2_given = (1, 2, 3)
        v2 = vec3.Vec3(v2_given)

        v1plus2 = v1 / v2

        expect_given = (v1_given[0] / v2_given[0], v1_given[1] / v2_given[1], v1_given[2] / v2_given[2])
        expect = vec3.Vec3(expect_given)

        msg = "Vec3(%s) / Vec3(%s) should be %s, got %s" % (str(v1_given), str(v2_given), str(expect_given), str(v1plus2))
        expect_tuple = (expect.x, expect.y, expect.z)
        v1plus2_tuple = (v1plus2.x, v1plus2.y, v1plus2.z)
        self.assertAlmostEqual(expect_tuple, v1plus2_tuple, msg=msg, places=Places)

    def test_vec3_binary_divide2(self):
        """Check binary divide operation on Vec3."""

        v1_given = (1.1, 2.2, 3.3)
        v1 = vec3.Vec3(v1_given)

        v2_given = (0.1, 0.1, 0.1)
        v2 = vec3.Vec3(v2_given)

        v1plus2 = v1 / v2

        expect_given = (v1_given[0] / v2_given[0], v1_given[1] / v2_given[1], v1_given[2] / v2_given[2])
        expect = vec3.Vec3(expect_given)

        msg = "Vec3(%s) / Vec3(%s) should be %s, got %s" % (str(v1_given), str(v2_given), str(expect_given), str(v1plus2))
        expect_tuple = (expect.x, expect.y, expect.z)
        v1plus2_tuple = (v1plus2.x, v1plus2.y, v1plus2.z)
        self.assertAlmostEqual(expect_tuple, v1plus2_tuple, msg=msg, places=Places)

    def test_vec3_binary_divide3(self):
        """Check binary divide operation on Vec3.  Divide-by-zero!"""

        v1_given = (1.1, 2.2, 3.3)
        v1 = vec3.Vec3(v1_given)

        v2_given = (0.1, 0.0, 0.1)
        v2 = vec3.Vec3(v2_given)

        with self.assertRaises(ZeroDivisionError):
            v1plus2 = v1 / v2

    def test_vec3_dot(self):
        """Check dot product operation on Vec3."""

        v1_given = (1.1, 2.2, 3.3)
        v1 = vec3.Vec3(v1_given)

        v2_given = (0.1, 0.1, 0.1)
        v2 = vec3.Vec3(v2_given)

        v1dotv2 = v1.dot(v2)

        expect = v1_given[0] * v2_given[0] + v1_given[1] * v2_given[1] + v1_given[2] * v2_given[2]

        msg = "Vec3(%s).dot(Vec3(%s)) should be %s, got %s" % (str(v1_given), str(v2_given), str(expect), str(v1dotv2))
        self.assertAlmostEqual(expect, v1dotv2, msg=msg, places=Places)

    def test_vec3_dot2(self):
        """Check dot product operation on Vec3."""

        v1_given = (1, 2, 3)
        v1 = vec3.Vec3(v1_given)

        v2_given = (0, 1, 1)
        v2 = vec3.Vec3(v2_given)

        v1dotv2 = v1.dot(v2)

        expect = v1_given[0] * v2_given[0] + v1_given[1] * v2_given[1] + v1_given[2] * v2_given[2]

        msg = "Vec3(%s).dot(Vec3(%s)) should be %s, got %s" % (str(v1_given), str(v2_given), str(expect), str(v1dotv2))
        self.assertAlmostEqual(expect, v1dotv2, msg=msg, places=Places)

    def test_vec3_dot3(self):
        """Check dot product operation on Vec3."""

        v1_given = (1, 2, 3)
        v1 = vec3.Vec3(v1_given)

        v2_given = (1, 0, 1)
        v2 = vec3.Vec3(v2_given)

        v1dotv2 = v1.dot(v2)

        expect = v1_given[0] * v2_given[0] + v1_given[1] * v2_given[1] + v1_given[2] * v2_given[2]

        msg = "Vec3(%s).dot(Vec3(%s)) should be %s, got %s" % (str(v1_given), str(v2_given), str(expect), str(v1dotv2))
        self.assertAlmostEqual(expect, v1dotv2, msg=msg, places=Places)

    def test_vec3_dot4(self):
        """Check dot product operation on Vec3."""

        v1_given = (1, 2, 3)
        v1 = vec3.Vec3(v1_given)

        v2_given = (1, 1, 0)
        v2 = vec3.Vec3(v2_given)

        v1dotv2 = v1.dot(v2)

        expect = v1_given[0] * v2_given[0] + v1_given[1] * v2_given[1] + v1_given[2] * v2_given[2]

        msg = "Vec3(%s).dot(Vec3(%s)) should be %s, got %s" % (str(v1_given), str(v2_given), str(expect), str(v1dotv2))
        self.assertAlmostEqual(expect, v1dotv2, msg=msg, places=Places)

    def test_vec3_cross(self):
        """Check cross product operation on Vec3."""

        v1_given = (1, 2, 3)
        v1 = vec3.Vec3(v1_given)

        v2_given = (1, 1, 1)
        v2 = vec3.Vec3(v2_given)

        v1crossv2 = v1.cross(v2)

        expect_tuple = (v1.y * v2.z - v1.z * v2.y, -(v1.x * v2.z - v1.z * v2.x), v1.x * v2.y - v1.y * v2.x)
        expect = vec3.Vec3(expect_tuple)

        msg = "Vec3(%s).cross(Vec3(%s)) should be %s, got %s" % (str(v1_given), str(v2_given), str(expect), str(v1crossv2))
        self.assertAlmostEqual(expect, v1crossv2, msg=msg, places=Places)

    def test_vec3_cross2(self):
        """Check cross product operation on Vec3."""

        v1_given = (1, 1, 1)
        v1 = vec3.Vec3(v1_given)

        v2_given = (-1, 1, 1)
        v2 = vec3.Vec3(v2_given)

        v1crossv2 = v1.cross(v2)

        expect_tuple = (v1.y * v2.z - v1.z * v2.y, -(v1.x * v2.z - v1.z * v2.x), v1.x * v2.y - v1.y * v2.x)
        expect = vec3.Vec3(expect_tuple)

        msg = "Vec3(%s).cross(Vec3(%s)) should be %s, got %s" % (str(v1_given), str(v2_given), str(expect), str(v1crossv2))
        self.assertNotEqual(expect, v1crossv2, msg=msg)

    def test_vec3_unitvector(self):
        """Check unit vector operation on Vec3."""

        v1_given = (1, 1, 1)
        v1 = vec3.Vec3(v1_given)

        u_vec = v1.unit_vector()

        expect_tuple = (v1.x/v1.length, v1.y/v1.length, v1.z/v1.length)
        expect = vec3.Vec3(expect_tuple)

        msg = "Vec3(%s).unit_vector() should be %s, got %s" % (str(v1_given), str(expect), str(u_vec))
        self.assertAlmostEqual(expect, u_vec, msg=msg)

if __name__ == '__main__':
    suite = unittest.makeSuite(TestVec3, 'test')
    runner = unittest.TextTestRunner()
    runner.run(suite)
