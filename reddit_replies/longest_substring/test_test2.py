#!/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for code in 'test2.py'.
"""

import unittest
from test2 import longest_sequence

class TestLS(unittest.TestCase):
    """Tests for the longest_sequence() function."""

    def test_simple1(self):
        input_string = 'azcbobobegghakl'
        got = longest_sequence(input_string)
        expect = 'beggh'
        msg = "longest_sequence(%s) returned '%s', expected '%s'" % (input_string, got, expect)
        self.assertTrue(got == expect, msg)

    def test_simple2(self):
        input_string = 'abcdefghzcbobobegghakl'
        got = longest_sequence(input_string)
        expect = 'abcdefghz'
        msg = "longest_sequence(%s) returned '%s', expected '%s'" % (input_string, got, expect)
        self.assertTrue(got == expect, msg)

    def test_simple3(self):
        input_string = 'azcabobobegghakl'
        got = longest_sequence(input_string)
        expect = 'beggh'
        msg = "longest_sequence(%s) returned '%s', expected '%s'" % (input_string, got, expect)
        self.assertTrue(got == expect, msg)

    def test_end_problem(self):
        input_string = 'azcabobobegghabcdefgkabcdefg'
        got = longest_sequence(input_string)
        expect = 'abcdefgk'
        msg = "longest_sequence(%s) returned '%s', expected '%s'" % (input_string, got, expect)
        self.assertTrue(got == expect, msg)

    def test_start_problem(self):
        input_string = 'abcdefghijkzcabobobegghabcdefgkabcdefg'
        got = longest_sequence(input_string)
        expect = 'abcdefghijkz'
        msg = "longest_sequence(%s) returned '%s', expected '%s'" % (input_string, got, expect)
        self.assertTrue(got == expect, msg)

    def test_debug_problem(self):
        input_string = 'abcdaxaxabc'
        got = longest_sequence(input_string)
        expect = 'abcd'
        msg = "longest_sequence(%s) returned '%s', expected '%s'" % (input_string, got, expect)
        self.assertTrue(got == expect, msg)

if __name__ == '__main__':
    unittest.main()
