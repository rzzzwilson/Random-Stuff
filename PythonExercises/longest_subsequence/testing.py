#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test the code samples.

Usage: testing.py <filename>

For example:
    testing.py test2.py
would test the code in test2.py.
"""

import os
import sys
import importlib
import unittest


class TestLongest(unittest.TestCase):

    def test_empty(self):
        """An empty string should return the empty string."""

        given = ''
        expected = ''
        result = longest(given)
        msg = "longest('%s') should return '%s' but got '%s'" % (given, expected, str(result))

        self.assertEqual(result, expected, msg)

    def test_simple(self):
        """A single character string should return the character."""

        given = 'a'
        expected = 'a'
        result = longest(given)
        msg = "longest('%s') should return '%s' but got '%s'" % (given, expected, str(result))

        self.assertEqual(result, expected, msg)

    def test_simple2(self):
        """An all increasing string should return the input string."""

        given = 'abc'
        expected = 'abc'
        result = longest(given)
        msg = "longest('%s') should return '%s' but got '%s'" % (given, expected, str(result))

        self.assertEqual(result, expected, msg)

    def test_simple3(self):
        """A decreasing sequence should return the FIRST single character."""

        given = 'cba'
        expected = 'c'
        result = longest(given)
        msg = "longest('%s') should return '%s' but got '%s'" % (given, expected, str(result))

        self.assertEqual(result, expected, msg)

    def test_simple4(self):
        """A repeated sequence should return the input string."""

        given = 'bbbbbb'
        expected = 'bbbbbb'
        result = longest(given)
        msg = "longest('%s') should return '%s' but got '%s'" % (given, expected, str(result))

        self.assertEqual(result, expected, msg)

    def test_longer(self):
        given = 'abcaqaaabbbqqqabd'
        expected = 'aaabbbqqq'
        result = longest(given)
        msg = "longest('%s') should return '%s' but got '%s'" % (given, expected, str(result))

        self.assertEqual(result, expected, msg)

    def test_longest(self):

        given = 'khdieuryfpbieuypbdfjlruuuuufvoidufvnodubeoriuybvspuybrpuyvbor'
        expected = 'bdfjlruuuuu'
        result = longest(given)
        msg = "longest('%s') should return '%s' but got '%s'" % (given, expected, str(result))

        self.assertEqual(result, expected, msg)


# get the name of the file to test
if len(sys.argv) != 2:
    print(__doc__)
    sys.exit(10)
filename = sys.argv[1]

# ensure name is of the form *.py and then dynamically import the code
# and set the global 'longest' to the function to test
(root, ext) = os.path.splitext(filename)
if ext != '.py':
    print("Sorry, the file must end in '.py'")
    sys.exit(10)
(head, tail) = os.path.split(root)
if head:
    print("Sorry, the file must be in this directory")
    sys.exit(10)

my_module = importlib.import_module(tail)
longest = my_module.longest

suite = unittest.makeSuite(TestLongest, 'test')
runner = unittest.TextTestRunner()
runner.run(suite)
