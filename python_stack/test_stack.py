#!/usr/bin/env python3

"""
Test the "stack" code.
"""

import os
import unittest

from stack import stack


class TestStack(unittest.TestCase):

    def test_size(self):
        s = stack()
        s.extend(range(100))    # have not allowed stack(range(100))

        expected = 100
        size = s.size()
        msg = f'Stack size should be {expected}, got {size}'
        self.assertEqual(size, expected, msg)

    def test_isempty(self):
        s = stack()

        got = s.isEmpty()
        expected = True
        msg = f"Got '{got}' from stack, expected '{expected}'"
        self.assertEqual(got, expected, msg)

        s.push(1)
        got = s.isEmpty()
        expected = False
        msg = f"Got '{got}' from stack, expected '{expected}'"
        self.assertEqual(got, expected, msg)

    def test_push(self):
        s = stack()

        s.push(1)
        expected = 1
        size = s.size()
        msg = f'After push(1) stack size should be {expected}, got {size}'
        self.assertEqual(size, expected, msg)

        s.push(2)
        expected = 2
        size = s.size()
        msg = f'After push(2) stack size should be {expected}, got {size}'
        self.assertEqual(size, expected, msg)

        got = s.pop()
        expected = 2
        msg = f'Got {got} from stack, expected {expected}'
        self.assertEqual(got, expected, msg)

        got = s.pop()
        expected = 1
        msg = f'Got {got} from stack, expected {expected}'
        self.assertEqual(got, expected, msg)

        got = s.isEmpty()
        expected = True
        msg = f"Got '{got}' from stack, expected '{expected}'"
        self.assertEqual(got, expected, msg)

    def test_pop(self):
        s = stack()
        s.extend([1, 2, 3])

        got = s.pop()
        expected = 3
        msg = f'Got {got} from stack, expected {expected}'
        self.assertEqual(got, expected, msg)

        got = s.pop()
        expected = 2
        msg = f'Got {got} from stack, expected {expected}'
        self.assertEqual(got, expected, msg)

        got = s.pop()
        expected = 1
        msg = f'Got {got} from stack, expected {expected}'
        self.assertEqual(got, expected, msg)

        msg = 'Expected IndexError from pop() of empty list'
        with self.assertRaises(IndexError, msg=msg):
            s.pop()

unittest.main()
