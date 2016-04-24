#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module to test the implementation of the 'class' singly-linked list.
"""

import sll_class as sll
import unittest
import copy


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

        test = []
        my_sll = sll.SLL(test)
        length = my_sll.length()
        expected_len = len(test)
        msg = "Length of SLL '%s' should be %d, got %d" % (my_sll.str(), expected_len, length)
        self.assertEqual(length, expected_len, msg)

    def test_length3(self):
        """Check that length() works."""

        test = ['M']
        my_sll = sll.SLL(test)
        expected_len = len(test)
        msg = "Expected SLL %s to have length %d, got %d" % (my_sll.str(), expected_len, my_sll.length())
        self.assertEqual(my_sll.length(), expected_len)

    def test_add_front(self):
        """Check that add_front() works for empty SLL."""

        old_sll = sll.SLL()
        before = old_sll.str()
        old_sll.add_front('A')
        after = old_sll.str()
        expected_list = ['A']
        expected = sll.SLL(expected_list)
        msg = "add_front() on %s should leave %s, got %s" % (before, expected.str(), after)
        self.assertEqual(after, expected.str())

    def test_add_front2(self):
        """Check that add_front() works on SLL with one element."""

        test = [20]
        my_sll = sll.SLL(test)
        before = my_sll.str()
        my_sll.add_front('M')
        after = my_sll.str()
        expected_list = ['M', 20]
        expected = sll.SLL(expected_list)
        msg = "add_front() on %s should leave %s, got %s" % (before, expected.str(), after)
        self.assertEqual(after, expected.str())

    def test_add_front3(self):
        """Check that add_front() works on SLL with many elements."""

        test = [20, 'A', 'omega']
        my_sll = sll.SLL(test)
        before = my_sll.str()
        my_sll.add_front('M')
        after = my_sll.str()
        expected_list = ['M', 20, 'A', 'omega']
        expected = sll.SLL(expected_list)
        msg = "add_front('M') on %s should give %s, got %s" % (before, expected.str(), after)
        self.assertEqual(my_sll.str(), expected.str())

    def test_add_front4(self):
        """Check that add_front() works repeatedly on SLL with no elements."""

        my_sll = sll.SLL()
        my_sll.add_front('first')
        expected = sll.SLL(['first'])
        self.assertEqual(my_sll.str(), expected.str())

        my_sll.add_front('second')
        expected = sll.SLL(['second', 'first'])
        self.assertEqual(my_sll.str(), expected.str())

        my_sll.add_front('third')
        expected = sll.SLL(['third', 'second', 'first'])
        self.assertEqual(my_sll.str(), expected.str())

        my_sll.add_front('fourth')
        expected = sll.SLL(['fourth', 'third', 'second', 'first'])
        self.assertEqual(my_sll.str(), expected.str())

    def test_add_back(self):
        """Check that add_back() works for empty SLL."""

        my_sll = sll.SLL()
        before = my_sll.str()
        my_sll.add_back('A')
        after = my_sll.str()
        expected_list = ['A']
        expected = sll.SLL(expected_list)
        msg = "add_back('M') on %s should give %s, git %s" % (before, expected.str(), after)
        self.assertEqual(after, expected.str())

    def test_add_back2(self):
        """Check that add_back() works on SLL with one element."""

        test = [20]
        my_sll = sll.SLL(20)
        before = my_sll.str()
        my_sll.add_back('M')
        after = my_sll.str()
        expected_list = [20, 'M']
        expected = sll.SLL(expected_list)
        msg = "add_back('M') on %s should give %s, git %s" % (before, expected.str(), after)
        self.assertEqual(after, expected.str())

    def test_add_back3(self):
        """Check that add_back() works on SLL with many elements."""

        test = ['A', 'omega']
        my_sll = sll.SLL(test)
        before = my_sll.str()
        my_sll.add_back('M')
        after = my_sll.str()
        expected_list = ['A', 'omega', 'M']
        expected = sll.SLL(expected_list)
        msg = "add_back('M') on %s should give %s, git %s" % (before, expected.str(), after)
        self.assertEqual(after, expected.str(), msg)

    def test_add_back4(self):
        """Check that add_back() works repeatedly on SLL with no elements."""

        my_sll = sll.SLL()
        before = my_sll.str()
        my_sll.add_back('first')
        after = my_sll.str()
        expected = sll.SLL(['first'])
        msg = "add_back('first') on %s should give %s, got %s" % (before, expected.str(), after)
        self.assertEqual(after, expected.str())

        before = my_sll.str()
        my_sll.add_back('second')
        after = my_sll.str()
        expected = sll.SLL(['first', 'second'])
        msg = "add_back('second') on %s should give %s, got %s" % (before, expected.str(), after)
        self.assertEqual(after, expected.str())

        before = my_sll.str()
        my_sll.add_back('third')
        after = my_sll.str()
        expected = sll.SLL(['first', 'second', 'third'])
        msg = "add_back('second') on %s should give %s, got %s" % (before, expected.str(), after)
        self.assertEqual(after, expected.str())

    def test_find(self):
        """Check that find() works on an empty SLL."""

        my_sll = sll.SLL()
        find = my_sll.find(20)
        msg = "Expected to not find 20 in SLL '%s', failed" % my_sll.str()
        self.assertFalse(find is not None, msg)

    def test_find2(self):
        """Check that find() works on an non-empty SLL."""

        test = ['A', 20, 'q', 'M']
        my_sll = sll.SLL(test)
        find = my_sll.find(20)
        expected = test.index(20)
        msg = ("find(20) on %s returned %s, expected %d" % (my_sll.str(), str(find), expected))
        self.assertTrue(find is not None, msg)

        # check the index returned is correct
        expected = test.index(20)
        msg = "find(20) on %s' returned '%s', expected '%s'" % (my_sll.str(), str(find), expected)
        self.assertTrue(find == expected, msg)

    def test_find3(self):
        """Check that find() works on an non-empty SLL with multiple finds."""

        test = ['A', 20, 'q', 20, 'M']
        my_sll = sll.SLL(test)
        find = my_sll.find(20)
        msg = "Expected to find 20 in SLL '%s', failed" % my_sll.str()
        self.assertTrue(find is not None, msg)

        # check returned index is as expected
        expected = test.index(20)
        msg = ("find(20) on %s' returned %s, expected %d" % (my_sll.str(), str(find), expected))
        self.assertTrue(find == expected, msg)

    def test_find4(self):
        """Check that find() works on an non-empty SLL with NO FIND."""

        test = ['A', 20, 'q', 20, 'M']
        my_sll = sll.SLL(test)
        find = my_sll.find('X')
        msg = "Expected to not find 'X' in SLL '%s', succeeded, find=%s?" % (my_sll.str(), str(find))
        self.assertTrue(find is None, msg)

    def test_add_after(self):
        """Check that add_after() works on an empty SLL."""

        my_sll = sll.SLL()
        before = my_sll.str()
        my_sll.add_after(20, 100)
        after = my_sll.str()
        expected = sll.SLL()
        msg = "add_after(20, 100) on %s should return %s, got '%s'" % (before, expected.str(), after)
        self.assertTrue(after == expected.str(), msg)

    def test_add_after2(self):
        """Check that add_after() works on an SLL with found value."""

        test = ['A', 20, 'q', 20, 'M']
        my_sll = sll.SLL(test)
        before = my_sll.str()
        my_sll.add_after(20, 100)
        after = my_sll.str()
        expected_list = ['A', 20, 100, 'q', 20, 'M']
        expected = sll.SLL(expected_list)
        msg = ("add_after(20, 100) on %s should return '%s', got '%s'" % (before, expected.str(), after))
        self.assertTrue(after == expected.str(), msg)

    def test_add_after3(self):
        """Check that add_after() works on an SLL with NO found value."""

        test = ['A', 20, 'q', 20, 'M']
        my_sll = sll.SLL(test)
        before = my_sll.str()
        my_sll.add_after(21, 100)
        after = my_sll.str()
        expected = sll.SLL(test)
        msg = ("add_after(21, 100) on %s should return %s, got '%s'" % (before, expected.str(), after))
        self.assertTrue(after == expected.str(), msg)

    def test_remove(self):
        """Check that remove() works on an empty SLL."""

        my_sll = sll.SLL()
        before = my_sll.str()
        my_sll.remove(21)
        after = my_sll.str()
        expected = sll.SLL()
        msg = ("Expected remove(21) on %s to return '%s', got '%s'" % (before, expected.str(), after))
        self.assertTrue(after == expected.str(), msg)

    def test_remove2(self):
        """Check that remove() works on an SLL with a found value."""
        test = ['A', 20, 'q', 20, 'M']
        my_sll = sll.SLL(test)
        before = my_sll.str()
        my_sll.remove('q')
        after = my_sll.str()
        expected_list = test[:]
        expected_list.remove('q')
        expected = sll.SLL(expected_list)
        msg = ("Expected remove('q') on %s to leave '%s', got '%s'" % (before, expected.str(), after))
        self.assertTrue(after == expected.str(), msg)

    def test_remove3(self):
        """Check that remove() works on an SLL with NO found value."""

        test = ['A', 20, 'q', 20, 'M']
        my_sll = sll.SLL(test)
        before = my_sll.str()
        my_sll.remove(22)
        after = my_sll.str()
        expected = sll.SLL(test)
        msg = ("Expected remove(21) on '%s' to leave '%s', got '%s'" % (before, expected.str(), after))
        self.assertTrue(after == expected.str(), msg)

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

    def test_map_fun(self):
        """Check the map_fun() function."""

        test = [1, 2, -3, 5, 100]
        my_sll = sll.SLL(test)
        before = copy.deepcopy(my_sll)
        func = lambda x, y: x + y
        my_sll.map_fun(func, 1)
        expected_list = [x + 1 for x in test]
        expected = sll.SLL(expected_list)
        msg = ("Expected map_fun('%s', func, 1) to return '%s', got '%s'"
               % (before.str(), expected.str(), my_sll.str()))
        self.assertTrue(my_sll.str() == expected.str(), msg)


if __name__ == '__main__':
    suite = unittest.makeSuite(TestSLL,'test')
    runner = unittest.TextTestRunner()
    runner.run(suite)
