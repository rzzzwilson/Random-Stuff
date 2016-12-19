#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test the "lisp" code.
"""

import os
import unittest

from lisp import *


class MyTest(unittest.TestCase):

    def test_cons_ok(self):
        """Does "cons" not fail?"""

        z = cons(1, 2)
        z = cons('1', 2)
        z = cons(1, '2')
        z = cons(1.0, 'qwe')

    def test_cons_fail(self):
        """Does "cons" not fail?"""

        msg = "'cons(1)' should raise TypeError!?"
        with self.assertRaises(TypeError, msg=msg):
            z = cons(1)

        msg = "'cons(1, 2, 3)' should raise TypeError!?"
        with self.assertRaises(TypeError, msg=msg):
            z = cons(1, 2, 3)

    def test_car_ok(self):
        """Can "car" a "cons" and get right result?"""

        z = cons(1, 2)
        x = car(z)
        msg = "'z=cons(1, 2); car(z)' should return 1, got '%s'!?" % str(x)
        self.assertEqual(x, 1, msg=msg)

        x = car(cons(3, 4))
        msg = "'car(cons(3, 4))' should return 3, got '%s'!?" % str(x)
        self.assertEqual(x, 3, msg=msg)

        x = car(cons('3', 4))
        msg = '''"car(cons('3', 4))" should return '3', got '%s'!?''' % str(x)
        self.assertEqual(x, '3', msg=msg)

    def test_cdr_ok(self):
        """Can "cdr" a "cons" and get right result?"""

        z = cons(1, '123')
        y = cdr(z)
        msg = "'z=cons(1, '123'); cdr(z)' should return '123', got '%s'!?" % str(y)
        self.assertEqual(y, '123', msg=msg)

        y = cdr(cons(3, None))
        msg = "'cdr(cons(3, None))' should return None, got '%s'!?" % str(y)
        self.assertEqual(y, None, msg=msg)

unittest.main()
