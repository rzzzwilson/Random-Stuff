#!/usr/bin/python3

"""
Code investigating:
    https://www.reddit.com/r/learnpython/comments/7sslph/create_a_list_between_two_instances_of_a_str_in/

This is the test suite for the above problem.
"""

import unittest
import test2 as test

class MyTest(unittest.TestCase):

    def test_simple(self):
        """Simple, no tricks"""

        given = ['A', 'B', 'C', 'A', 'D', 'A', 'E', 'F']
        expected = [['A', 'B', 'C'], ['A', 'D'], ['A', 'E', 'F']]
        got = test.substr_split(given)
        msg = f"Splitting '{given}',\nexpected '{expected}',\ngot '{got}'"
        self.assertEqual(expected, got, msg=msg)

    def test_only_one(self):
        """Simple, only one substring"""

        given = ['A', 'B', 'C', 'D', 'E', 'F']
        expected = [['A', 'B', 'C', 'D', 'E', 'F']]
        got = test.substr_split(given)
        msg = f"Splitting '{given}',\nexpected '{expected}',\ngot '{got}'"
        self.assertEqual(expected, got, msg=msg)

    def test_short_subs(self):
        """Try short substrings"""

        given = ['A', 'B', 'C', 'A', 'A', 'E', 'F']
        expected = [['A', 'B', 'C'], ['A'], ['A', 'E', 'F']]
        got = test.substr_split(given)
        msg = f"Splitting '{given}',\nexpected '{expected}',\ngot '{got}'"
        self.assertEqual(expected, got, msg=msg)

    def test_short_final(self):
        """Last substring is shortest possible"""

        given = ['A', 'B', 'C', 'A', 'A']
        expected = [['A', 'B', 'C'], ['A'], ['A']]
        got = test.substr_split(given)
        msg = f"Splitting '{given}',\nexpected '{expected}',\ngot '{got}'"
        self.assertEqual(expected, got, msg=msg)

    def test_short_first(self):
        """First substring is shortest possible"""

        given = ['A', 'A', 'B', 'C', 'A', 'A']
        expected = [['A'], ['A', 'B', 'C'], ['A'], ['A']]
        got = test.substr_split(given)
        msg = f"Splitting '{given}',\nexpected '{expected}',\ngot '{got}'"
        self.assertEqual(expected, got, msg=msg)

unittest.main()
