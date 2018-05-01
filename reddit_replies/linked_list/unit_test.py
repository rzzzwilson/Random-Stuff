#!/usr/bin/env python

"""
Test the linked list code.
"""

import os
import unittest

from test import *


class MyTest(unittest.TestCase):

    def test_simple(self):
        """Instantiate a linked list without an error?"""

        l = LinkedList()

    def test_append(self):
        """Can append to a linked list?"""

        l = LinkedList()
        l.add(12)
        l.add(12)
        for node in l:
            print(node.data)
            msg = f"Found node.data '{node.data}', expected 12"
            self.assertEqual(node.data, 12, msg=msg)

unittest.main()
