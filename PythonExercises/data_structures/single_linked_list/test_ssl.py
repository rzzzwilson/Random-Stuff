#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module to test the implementation of the singly-linked list.
"""

import ssl_element as ssl
import unittest


class TestSSL(unittest.TestCase):

    def test___str__(self):
        """Check that __str__() works."""

        my_ssl = ssl.SSL('M')
        my_ssl = ssl.SSL('q', my_ssl)
        my_ssl = ssl.SSL(20, my_ssl)
        my_ssl = ssl.SSL('A', my_ssl)
        expected = ['A', 20, 'q', 'M']

        self.assertEqual(ssl.__str__(my_ssl), str(expected))

    def test_ssl_create(self):
        """Check a simple SSL creation."""

        my_ssl = ssl.SSL('M')
        my_ssl = ssl.SSL('q', my_ssl)
        my_ssl = ssl.SSL(20, my_ssl)
        my_ssl = ssl.SSL('A', my_ssl)

        my_ssl2 = ssl.SSL('A',
                           ssl.SSL(20,
                               ssl.SSL('q',
                                   ssl.SSL('M'))))

        self.assertEqual(ssl.__str__(my_ssl), ssl.__str__(my_ssl2))

    def test_length(self):
        """Check that length() works."""

        my_ssl = ssl.SSL('M')
        my_ssl = ssl.SSL('q', my_ssl)
        my_ssl = ssl.SSL(20, my_ssl)
        my_ssl = ssl.SSL('A', my_ssl)
        expected_len = 4

        self.assertEqual(ssl.length(my_ssl), expected_len)

    def test_length2(self):
        """Check that len() works on an empty list."""

        my_ssl = None
        expected_len = 0

        self.assertEqual(ssl.length(my_ssl), expected_len)

    def test_length3(self):
        """Check that length() works."""

        my_ssl = ssl.SSL('M')
        expected_len = 1

        self.assertEqual(ssl.length(my_ssl), expected_len)

    def test_add_front(self):
        """Check that add_front() works for empty SSL."""

        old_ssl = None
        new_ssl = ssl.add_front(old_ssl, 'A')
        expected = ['A']

        self.assertEqual(ssl.__str__(new_ssl), str(expected))

    def test_add_front2(self):
        """Check that add_front() works on SSL with one element."""

        old_ssl = ssl.SSL(20)
        new_ssl = ssl.add_front(old_ssl, 'M')
        expected = ['M', 20]

        self.assertEqual(ssl.__str__(new_ssl), str(expected))

    def test_add_front3(self):
        """Check that add_front() works on SSL with many elements."""

        old_ssl = ssl.SSL(20, ssl.SSL('A', ssl.SSL('omega')))
        new_ssl = ssl.add_front(old_ssl, 'M')
        expected = ['M', 20, 'A', 'omega']

        self.assertEqual(ssl.__str__(new_ssl), str(expected))

    def test_add_front4(self):
        """Check that add_front() works repeatedly on SSL with no elements."""

        old_ssl = None
        new_ssl = ssl.add_front(old_ssl, 'first')
        expected = ['first']
        self.assertEqual(ssl.__str__(new_ssl), str(expected))

        new_ssl = ssl.add_front(new_ssl, 'second')
        expected = ['second', 'first']
        self.assertEqual(ssl.__str__(new_ssl), str(expected))

        new_ssl = ssl.add_front(new_ssl, 'third')
        expected = ['third', 'second', 'first']
        self.assertEqual(ssl.__str__(new_ssl), str(expected))

        new_ssl = ssl.add_front(new_ssl, 'fourth')
        expected = ['fourth', 'third', 'second', 'first']
        self.assertEqual(ssl.__str__(new_ssl), str(expected))

    def test_add_end(self):
        """Check that add_end() works for empty SSL."""

        old_ssl = None
        new_ssl = ssl.add_end(old_ssl, 'A')
        expected = ['A']

        self.assertEqual(ssl.__str__(new_ssl), str(expected))

    def test_add_end2(self):
        """Check that add_end() works on SSL with one element."""

        old_ssl = ssl.SSL(20)
        new_ssl = ssl.add_end(old_ssl, 'M')
        expected = [20, 'M']

        self.assertEqual(ssl.__str__(new_ssl), str(expected))

    def test_add_end3(self):
        """Check that add_end() works on SSL with many elements."""

        old_ssl = ssl.SSL(20, ssl.SSL('A', ssl.SSL('omega')))
        new_ssl = ssl.add_end(old_ssl, 'M')
        expected = [20, 'A', 'omega', 'M']

        self.assertEqual(ssl.__str__(new_ssl), str(expected))

    def test_add_end4(self):
        """Check that add_end() works repeatedly on SSL with no elements."""

        old_ssl = None
        new_ssl = ssl.add_end(old_ssl, 'first')
        expected = ['first']
        self.assertEqual(ssl.__str__(new_ssl), str(expected))

        new_ssl = ssl.add_end(new_ssl, 'second')
        expected = ['first', 'second']
        self.assertEqual(ssl.__str__(new_ssl), str(expected))

        new_ssl = ssl.add_end(new_ssl, 'third')
        expected = ['first', 'second', 'third']
        self.assertEqual(ssl.__str__(new_ssl), str(expected))

        new_ssl = ssl.add_end(new_ssl, 'fourth')
        expected = ['first', 'second', 'third', 'fourth']
        self.assertEqual(ssl.__str__(new_ssl), str(expected))

    def test_find(self):
        """Check that find() works on an empty SSL."""

        pass

if __name__ == '__main__':
    suite = unittest.makeSuite(TestSSL,'test')
    runner = unittest.TextTestRunner()
    runner.run(suite)
