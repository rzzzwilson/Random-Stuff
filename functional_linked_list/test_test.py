#!/usr/bin/env python

"""
Test the functional linked list code.
"""

import os
import unittest

from test import *


class MyTest(unittest.TestCase):

    def test_smoke(self):
        z = create(1, None)
        y = create(2, z)
        x = create(3, y)

    def test_iterate(self):
        z = create(1, None)
        y = create(2, z)
        x = create(3, y)
        while x:
            x = get_next(x)

unittest.main()
