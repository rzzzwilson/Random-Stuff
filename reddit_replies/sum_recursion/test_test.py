#!/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for code in 'test.py'.

An attempt to answer the reddit question:
    https://www.reddit.com/r/learnpython/comments/6rvs5c/recursive_exercise_help/
"""

import unittest
from test import pack

class TestPack(unittest.TestCase):
    """Tests for the pack() function."""

    def test_simple1(self):
        s = [4, 1, 3, 5]
        n = 7
        expect = {3, 4}
        msg = 'bug in test function: sum(%s)=%d > %d' % (str(expect), sum(expect), n)
        self.assertTrue(sum(expect) <= n, msg)
        found = pack(s, n)
        msg = 'pack(%s, %d) returned %s, expected %s' % (str(s), n, str(found), str(expect))
        self.assertTrue(found == expect, msg)

    def test_simple2(self):
        s = [4, 1, 3, 5]
        n = 6
        expect = {1, 5}
        msg = 'bug in test function: sum(%s)=%d > %d' % (str(expect), sum(expect), n)
        self.assertTrue(sum(expect) <= n, msg)
        found = pack(s, n)
        msg = 'pack(%s, %d) returned %s, expected %s' % (str(s), n, str(found), str(expect))
        self.assertTrue(found == expect, msg)

    def test_simple3(self):
        s = [4, 1, 3, 5]
        n = 11
        expect = {1, 4, 5}
        msg = 'bug in test function: sum(%s)=%d > %d' % (str(expect), sum(expect), n)
        self.assertTrue(sum(expect) <= n, msg)
        found = pack(s, n)
        msg = 'pack(%s, %d) returned %s, expected %s' % (str(s), n, str(found), str(expect))
        self.assertTrue(found == expect, msg)

    def test_empty_result(self):
        s = [4, 2, 3, 5]
        n = 1
        expect = set()
        msg = 'bug in test function: sum(%s)=%d > %d' % (str(expect), sum(expect), n)
        self.assertTrue(sum(expect) <= n, msg)
        found = pack(s, n)
        msg = 'pack(%s, %d) returned %s, expected %s' % (str(s), n, str(found), str(expect))
        self.assertTrue(found == expect, msg)

    def test_duplicates(self):
        s = [4, 1, 1, 3, 5]
        n = 11
        expect = {1, 4, 5}
        msg = 'bug in test function: sum(%s)=%d > %d' % (str(expect), sum(expect), n)
        self.assertTrue(sum(expect) <= n, msg)
        found = pack(s, n)
        msg = 'pack(%s, %d) returned %s, expected %s' % (str(s), n, str(found), str(expect))
        self.assertTrue(found == expect, msg)

    def test_complicated(self):
        s = [4, 1, 3, 5, 8, 11, 13, 2]
        n = 40
        expect = {1, 3, 4, 8, 11, 13}
        msg = 'bug in test function: sum(%s)=%d > %d' % (str(expect), sum(expect), n)
        self.assertTrue(sum(expect) <= n, msg)
        found = pack(s, n)
        msg = 'pack(%s, %d) returned %s, expected %s' % (str(s), n, str(found), str(expect))
        self.assertTrue(found == expect, msg)

    def test_complicated2(self):
        s = [4, 1, 3, 5, 8, 11, 13, 2]
        n = 41
        expect = {2, 3, 4, 8, 11, 13}
        msg = 'bug in test function: sum(%s)=%d > %d' % (str(expect), sum(expect), n)
        self.assertTrue(sum(expect) <= n, msg)
        found = pack(s, n)
        msg = 'pack(%s, %d) returned %s, expected %s' % (str(s), n, str(found), str(expect))
        self.assertTrue(found == expect, msg)

    def test_complicated3(self):
        s = [4, 1, 3, 5, 8, 11, 13, 2]
        n = 42
        expect = {1, 2, 3, 4, 8, 11, 13}
        msg = 'bug in test function: sum(%s)=%d > %d' % (str(expect), sum(expect), n)
        self.assertTrue(sum(expect) <= n, msg)
        found = pack(s, n)
        msg = 'pack(%s, %d) returned %s, expected %s' % (str(s), n, str(found), str(expect))
        self.assertTrue(found == expect, msg)

    def test_complicated4(self):
        s = [4, 1, 3, 5, 8, 11, 13, 2]
        n = 43
        expect = {2, 4, 5, 8, 11, 13}
        msg = 'bug in test function: sum(%s)=%d > %d' % (str(expect), sum(expect), n)
        self.assertTrue(sum(expect) <= n, msg)
        found = pack(s, n)
        msg = 'pack(%s, %d) returned %s, expected %s' % (str(s), n, str(found), str(expect))
        self.assertTrue(found == expect, msg)

if __name__ == '__main__':
    unittest.main()
