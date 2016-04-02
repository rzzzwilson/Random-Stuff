#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module to test the implementation of the singly-linked list.
"""

import ssl
import unittest


class TestSSL(unittest.TestCase):

    def test_ssl2list(self):
        """Check that ssl2list() works."""

        my_list = ssl.SSL('M')
        my_list = ssl.SSL('q', my_list)
        my_list = ssl.SSL(20, my_list)
        my_list = ssl.SSL('A', my_list)
        expected = ['M', 'q', 20, 'A']

        self.assertEqual(ssl.ssl2list(my_list), expected)

    def test_ssl_create(self):
        """Check a simple SSL creation."""

        my_list = ssl.SSL('M')
        my_list = ssl.SSL('q', my_list)
        my_list = ssl.SSL(20, my_list)
        my_list = ssl.SSL('A', my_list)

        my_list2 = ssl.SSL('A',
                           ssl.SSL(20,
                               ssl.SSL('q',
                                   ssl.SSL('M'))))

        self.assertEqual(ssl.ssl2list(my_list), ssl.ssl2list(my_list2))


if __name__ == '__main__':
    suite = unittest.makeSuite(TestSSL,'test')
    runner = unittest.TextTestRunner()
    runner.run(suite)
