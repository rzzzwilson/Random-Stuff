#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test the UID() class.
"""

import os
import sys
from uid import UID
import unittest

class TestUID(unittest.TestCase):
    def test_smoke(self):
        """A smoke test for the UID class."""

        uid = UID()

    def test_simple(self):
        """Just create one UID and free it."""

        my_uid = UID()

        actual = my_uid.pop()
        expected = '0'
        msg = ("Expected first UID to be '0', got '%s'" % str(actual))
        self.assertEqual(actual, expected, msg)

        my_uid.push(actual)

    def test_simple2(self):
        """Create two UIDs and free the first."""

        my_uid = UID()

        first = my_uid.pop()
        expected = '0'
        msg = ("Expected first UID to be '0', got '%s'" % str(first))
        self.assertEqual(first, expected, msg)

        second = my_uid.pop()
        expected = '1'
        msg = ("Expected second UID to be '1', got '%s'" % str(second))
        self.assertEqual(second, expected, msg)

        my_uid.push(first)


unittest.main()
