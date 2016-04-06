#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module to test the implementation of the 'class' singly-linked list.
"""

import sll_class as sll
import unittest


class TestSLL(unittest.TestCase):

    def test_sll_create(self):
        """Check a simple SLL creation."""

        test = ['A', 20, 'q', 'M']
        my_sll = sll.SLL(test)
        expected = test[:]
        msg = "sll.SLL(%s) made SLL=%s" % (str(test), my_sll.str())
        self.assertEqual(my_sll.str(), str(expected), msg)

    def test_length(self):
        """Check that length() works."""

        test = ['A', 20, 'q', 'M']
        my_sll = sll.SLL(test)
        expected_len = len(test)
        length = my_sll.length()
        msg = "Length of SLL '%s' should be %d, got %d" % (my_sll.str(), expected_len, length)
        self.assertEqual(length, expected_len, msg)

    def test_length2(self):
        """Check that len() works on an empty list."""

        my_sll = None
        expected_len = 0

        self.assertEqual(sll.length(my_sll), expected_len)

    def test_length3(self):
        """Check that length() works."""

        my_sll = sll.SLL('M')
        expected_len = 1

        self.assertEqual(sll.length(my_sll), expected_len)

    def test_add_front(self):
        """Check that add_front() works for empty SLL."""

        old_sll = None
        new_sll = sll.add_front(old_sll, 'A')
        expected = ['A']

        self.assertEqual(new_sll.str(), str(expected))

    def test_add_front2(self):
        """Check that add_front() works on SLL with one element."""

        old_sll = sll.SLL(20)
        new_sll = sll.add_front(old_sll, 'M')
        expected = ['M', 20]

        self.assertEqual(new_sll.str(), str(expected))

    def test_add_front3(self):
        """Check that add_front() works on SLL with many elements."""

        old_sll = sll.SLL(20, sll.SLL('A', sll.SLL('omega')))
        new_sll = sll.add_front(old_sll, 'M')
        expected = ['M', 20, 'A', 'omega']

        self.assertEqual(new_sll.str(), str(expected))

    def test_add_front4(self):
        """Check that add_front() works repeatedly on SLL with no elements."""

        old_sll = None
        new_sll = sll.add_front(old_sll, 'first')
        expected = ['first']
        self.assertEqual(new_sll.str(), str(expected))

        new_sll = sll.add_front(new_sll, 'second')
        expected = ['second', 'first']
        self.assertEqual(new_sll.str(), str(expected))

        new_sll = sll.add_front(new_sll, 'third')
        expected = ['third', 'second', 'first']
        self.assertEqual(new_sll.str(), str(expected))

        new_sll = sll.add_front(new_sll, 'fourth')
        expected = ['fourth', 'third', 'second', 'first']
        self.assertEqual(new_sll.str(), str(expected))

    def test_add_end(self):
        """Check that add_end() works for empty SLL."""

        old_sll = None
        new_sll = sll.add_end(old_sll, 'A')
        expected = ['A']

        self.assertEqual(new_sll.str(), str(expected))

    def test_add_end2(self):
        """Check that add_end() works on SLL with one element."""

        old_sll = sll.SLL(20)
        new_sll = sll.add_end(old_sll, 'M')
        expected = [20, 'M']

        self.assertEqual(new_sll.str(), str(expected))

    def test_add_end3(self):
        """Check that add_end() works on SLL with many elements."""

        old_sll = sll.SLL(20, sll.SLL('A', sll.SLL('omega')))
        new_sll = sll.add_end(old_sll, 'M')
        expected = [20, 'A', 'omega', 'M']

        self.assertEqual(new_sll.str(), str(expected))

    def test_add_end4(self):
        """Check that add_end() works repeatedly on SLL with no elements."""

        old_sll = None
        new_sll = sll.add_end(old_sll, 'first')
        expected = ['first']
        self.assertEqual(new_sll.str(), str(expected))

        new_sll = sll.add_end(new_sll, 'second')
        expected = ['first', 'second']
        self.assertEqual(new_sll.str(), str(expected))

        new_sll = sll.add_end(new_sll, 'third')
        expected = ['first', 'second', 'third']
        self.assertEqual(new_sll.str(), str(expected))

        new_sll = sll.add_end(new_sll, 'fourth')
        expected = ['first', 'second', 'third', 'fourth']
        self.assertEqual(new_sll.str(), str(expected))

    def test_find(self):
        """Check that find() works on an empty SLL."""

        my_sll = None
        find = sll.find(my_sll, 20)
        msg = "Expected to not find 20 in SLL '%s', failed" % my_sll.str()
        self.assertFalse(find is not None, msg)

    def test_find2(self):
        """Check that find() works on an non-empty SLL."""

        my_sll = sll.SLL('A', sll.SLL(20, sll.SLL('q', sll.SLL('M'))))
        find = sll.find(my_sll, 20)
        msg = "Expected to find 20 in SLL '%s', failed" % my_sll.str()
        self.assertTrue(find is not None, msg)

        # check the sub-SLL returned is correct
        expected = sll.SLL(20, sll.SLL('q', sll.SLL('M')))
        msg = ("find('%s', 20) returned '%s', expected '%s'"
               % (my_sll.str(), find.str(), expected.str()))
        self.assertTrue(find.str() == expected.str(), msg)

    def test_find3(self):
        """Check that find() works on an non-empty SLL with multiple finds."""

        my_sll = sll.SLL('A', sll.SLL(20, sll.SLL('q', sll.SLL(20, sll.SLL('M')))))
        find = sll.find(my_sll, 20)
        msg = "Expected to find 20 in SLL '%s', failed" % my_sll.str()
        self.assertTrue(find is not None, msg)

        # check returned sub-SLL is as expected
        expected = sll.SLL(20, sll.SLL('q', sll.SLL(20, sll.SLL('M'))))
        msg = ("find('%s', 20) returned '%s', expected '%s'"
               % (my_sll.str(), find.str(), expected.str()))
        self.assertTrue(find.str() == expected.str(), msg)

    def test_find4(self):
        """Check that find() works on an non-empty SLL with NO FIND."""

        my_sll = sll.SLL('A', sll.SLL(20, sll.SLL('q', sll.SLL(20, sll.SLL('M')))))
        find = sll.find(my_sll, 'X')
        msg = "Expected to not find 'X' in SLL '%s', succeeded?" % my_sll.str()
        self.assertTrue(find is None, msg)

    def test_add_after(self):
        """Check that add_after() works on an empty SLL."""

        my_sll = None
        result = sll.add_after(my_sll, 20, 100)
        msg = "Expected add_after(None, 20, 100) to fail, didn't, got '%s'" % str(result)
        self.assertTrue(result is None, msg)

    def test_add_after2(self):
        """Check that add_after() works on an SLL with found value."""

        my_sll = sll.SLL('A', sll.SLL(20, sll.SLL('q', sll.SLL(20, sll.SLL('M')))))
        result = sll.add_after(my_sll, 20, 100)
        expected = sll.SLL(20, sll.SLL(100, sll.SLL('q', sll.SLL(20, sll.SLL('M')))))
        msg = ("Expected add_after('%s', 20, 100) to return '%s', got '%s'"
               % (my_sll.str(), expected.str(), result.str()))
        self.assertTrue(result.str() == expected.str(), msg)

    def test_add_after3(self):
        """Check that add_after() works on an SLL with NO found value."""

        my_sll = sll.SLL('A', sll.SLL(20, sll.SLL('q', sll.SLL(20, sll.SLL('M')))))
        result = sll.add_after(my_sll, 21, 100)
        expected = None
        msg = ("Expected add_after('%s', 21, 100) to return None, got '%s'"
               % (my_sll.str(), result.str()))
        self.assertTrue(result.str() == expected.str(), msg)

    def test_remove(self):
        """Check that remove() works on an empty SLL."""

        my_sll = None
        result = None
        expected = None
        result = sll.remove(my_sll, 21)
        msg = ("Expected remove('%s', 21) to return '%s', got '%s'"
               % (my_sll.str(), expected.str(), result.str()))
        self.assertTrue(result.str() == expected.str(), msg)

    def test_remove2(self):
        """Check that remove() works on an SLL with a found value."""

        my_sll = sll.SLL('A', sll.SLL(20, sll.SLL('q', sll.SLL(20, sll.SLL('M')))))
        result = sll.remove(my_sll, 'q')
        expected = sll.SLL('A', sll.SLL(20, sll.SLL(20, sll.SLL('M'))))
        msg = ("Expected remove('%s', 21, 100) to return '%s', got '%s'"
               % (my_sll.str(), expected.str(), result.str()))
        self.assertTrue(result.str() == expected.str(), msg)

    def test_remove3(self):
        """Check that remove() works on an SLL with NO found value."""

        my_sll = sll.SLL('A', sll.SLL(20, sll.SLL('q', sll.SLL(20, sll.SLL('M')))))
        result = sll.remove(my_sll, 22)
        expected = my_sll
        msg = ("Expected remove('%s', 21, 100) to return '%s', got '%s'"
               % (my_sll.str(), expected.str(), result.str()))
        self.assertTrue(result.str() == expected.str(), msg)

    def test_remove_first(self):
        """Check that remove_first() works on an empty SLL."""

        my_sll = sll.SLL()
        before = my_sll.str()
        my_sll.remove_first()
        after = my_sll.str()
        expected = sll.SLL()
        msg = ("Expected remove_first() on '%s' to leave '%s', got '%s'" % (before, expected.str(), after))
        self.assertTrue(after == expected.str(), msg)

    def test_remove_first2(self):
        """Check that remove_first() works on a non-empty SLL."""

        test = ['A', 20, 'q', 20, 'M']
        my_sll = sll.SLL(test)
        before = my_sll.str()
        my_sll.remove_first()
        after = my_sll.str()
        expected_list = test[1:]
        expected = sll.SLL(expected_list)
        msg = ("Expected remove_first() on '%s' to leave '%s', got '%s'" % (before, expected.str(), after))
        self.assertTrue(after == expected.str(), msg)

    def test_remove_last(self):
        """Check that remove_last() works on an empty SLL."""

        my_sll = sll.SLL()
        before = my_sll.str()
        my_sll.remove_last()
        after = my_sll.str()
        expected = sll.SLL()
        msg = ("Expected remove_last on '%s' to leave '%s', got '%s'" % (before, expected.str(), after))
        self.assertTrue(after == expected.str(), msg)

    def test_remove_last2(self):
        """Check that remove_last() works on a non-empty SLL."""

        test = ['A', 20, 'q', 20, 'M']
        my_sll = sll.SLL(test)
        before = my_sll.str()
        my_sll.remove_last()
        after = my_sll.str()
        expected_list= test[:-1]
        expected = sll.SLL(expected_list)
        msg = ("Expected remove_last() on '%s' to leave '%s', got '%s'" % (before, expected.str(), after))
        self.assertTrue(after == expected.str(), msg)

if __name__ == '__main__':
    suite = unittest.makeSuite(TestSLL,'test')
    runner = unittest.TextTestRunner()
    runner.run(suite)
