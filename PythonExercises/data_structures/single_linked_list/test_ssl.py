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

        my_ssl = None
        find = ssl.find(my_ssl, 20)
        msg = "Expected to not find 20 in SSL '%s', failed" % ssl.__str__(my_ssl)
        self.assertFalse(find is not None, msg)

    def test_find2(self):
        """Check that find() works on an non-empty SSL."""

        my_ssl = ssl.SSL('A', ssl.SSL(20, ssl.SSL('q', ssl.SSL('M'))))
        find = ssl.find(my_ssl, 20)
        msg = "Expected to find 20 in SSL '%s', failed" % ssl.__str__(my_ssl)
        self.assertTrue(find is not None, msg)

        # check the sub-SSL returned is correct
        expected = ssl.SSL(20, ssl.SSL('q', ssl.SSL('M')))
        msg = ("find('%s', 20) returned '%s', expected '%s'"
               % (ssl.__str__(my_ssl), ssl.__str__(find), ssl.__str__(expected)))
        self.assertTrue(ssl.__str__(find) == ssl.__str__(expected), msg)

    def test_find3(self):
        """Check that find() works on an non-empty SSL with multiple finds."""

        my_ssl = ssl.SSL('A', ssl.SSL(20, ssl.SSL('q', ssl.SSL(20, ssl.SSL('M')))))
        find = ssl.find(my_ssl, 20)
        msg = "Expected to find 20 in SSL '%s', failed" % ssl.__str__(my_ssl)
        self.assertTrue(find is not None, msg)

        # check returned sub-SSL is as expected
        expected = ssl.SSL(20, ssl.SSL('q', ssl.SSL(20, ssl.SSL('M'))))
        msg = ("find('%s', 20) returned '%s', expected '%s'"
               % (ssl.__str__(my_ssl), ssl.__str__(find), ssl.__str__(expected)))
        self.assertTrue(ssl.__str__(find) == ssl.__str__(expected), msg)

    def test_find4(self):
        """Check that find() works on an non-empty SSL with NO FIND."""

        my_ssl = ssl.SSL('A', ssl.SSL(20, ssl.SSL('q', ssl.SSL(20, ssl.SSL('M')))))
        find = ssl.find(my_ssl, 'X')
        msg = "Expected to not find 'X' in SSL '%s', succeeded?" % ssl.__str__(my_ssl)
        self.assertTrue(find is None, msg)

    def test_add_after(self):
        """Check that add_after() works on an empty SSL."""

        my_ssl = None
        result = ssl.add_after(my_ssl, 20, 100)
        msg = "Expected add_after(None, 20, 100) to fail, didn't, got '%s'" % str(result)
        self.assertTrue(result is None, msg)

    def test_add_after2(self):
        """Check that add_after() works on an SSL with found value."""

        my_ssl = ssl.SSL('A', ssl.SSL(20, ssl.SSL('q', ssl.SSL(20, ssl.SSL('M')))))
        result = ssl.add_after(my_ssl, 20, 100)
        expected = ssl.SSL(20, ssl.SSL(100, ssl.SSL('q', ssl.SSL(20, ssl.SSL('M')))))
        msg = ("Expected add_after('%s', 20, 100) to return '%s', got '%s'"
               % (ssl.__str__(my_ssl), ssl.__str__(expected), ssl.__str__(result)))
        self.assertTrue(ssl.__str__(result) == ssl.__str__(expected), msg)

    def test_add_after3(self):
        """Check that add_after() works on an SSL with NO found value."""

        my_ssl = ssl.SSL('A', ssl.SSL(20, ssl.SSL('q', ssl.SSL(20, ssl.SSL('M')))))
        result = ssl.add_after(my_ssl, 21, 100)
        expected = None
        msg = ("Expected add_after('%s', 21, 100) to return None, got '%s'"
               % (ssl.__str__(my_ssl), ssl.__str__(result)))
        self.assertTrue(ssl.__str__(result) == ssl.__str__(expected), msg)

if __name__ == '__main__':
    suite = unittest.makeSuite(TestSSL,'test')
    runner = unittest.TextTestRunner()
    runner.run(suite)
