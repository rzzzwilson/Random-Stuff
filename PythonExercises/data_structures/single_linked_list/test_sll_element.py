#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module to test the implementation of the singly-linked list.
"""

import sll_element as sll
import unittest


class TestSLL(unittest.TestCase):

    def test___str__(self):
        """Check that __str__() works."""

        my_sll = sll.SLL('M')
        my_sll = sll.SLL('q', my_sll)
        my_sll = sll.SLL(20, my_sll)
        my_sll = sll.SLL('A', my_sll)
        expected = ['A', 20, 'q', 'M']

        self.assertEqual(sll.__str__(my_sll), str(expected))

    def test_sll_create(self):
        """Check a simple SLL creation."""

        my_sll = sll.SLL('M')
        my_sll = sll.SLL('q', my_sll)
        my_sll = sll.SLL(20, my_sll)
        my_sll = sll.SLL('A', my_sll)

        my_sll2 = sll.SLL('A',
                           sll.SLL(20,
                               sll.SLL('q',
                                   sll.SLL('M'))))

        self.assertEqual(sll.__str__(my_sll), sll.__str__(my_sll2))

    def test_length(self):
        """Check that length() works."""

        my_sll = sll.SLL('M')
        my_sll = sll.SLL('q', my_sll)
        my_sll = sll.SLL(20, my_sll)
        my_sll = sll.SLL('A', my_sll)
        expected_len = 4

        self.assertEqual(sll.length(my_sll), expected_len)

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

        self.assertEqual(sll.__str__(new_sll), str(expected))

    def test_add_front2(self):
        """Check that add_front() works on SLL with one element."""

        old_sll = sll.SLL(20)
        new_sll = sll.add_front(old_sll, 'M')
        expected = ['M', 20]

        self.assertEqual(sll.__str__(new_sll), str(expected))

    def test_add_front3(self):
        """Check that add_front() works on SLL with many elements."""

        old_sll = sll.SLL(20, sll.SLL('A', sll.SLL('omega')))
        new_sll = sll.add_front(old_sll, 'M')
        expected = ['M', 20, 'A', 'omega']

        self.assertEqual(sll.__str__(new_sll), str(expected))

    def test_add_front4(self):
        """Check that add_front() works repeatedly on SLL with no elements."""

        old_sll = None
        new_sll = sll.add_front(old_sll, 'first')
        expected = ['first']
        self.assertEqual(sll.__str__(new_sll), str(expected))

        new_sll = sll.add_front(new_sll, 'second')
        expected = ['second', 'first']
        self.assertEqual(sll.__str__(new_sll), str(expected))

        new_sll = sll.add_front(new_sll, 'third')
        expected = ['third', 'second', 'first']
        self.assertEqual(sll.__str__(new_sll), str(expected))

        new_sll = sll.add_front(new_sll, 'fourth')
        expected = ['fourth', 'third', 'second', 'first']
        self.assertEqual(sll.__str__(new_sll), str(expected))

    def test_add_end(self):
        """Check that add_end() works for empty SLL."""

        old_sll = None
        new_sll = sll.add_end(old_sll, 'A')
        expected = ['A']

        self.assertEqual(sll.__str__(new_sll), str(expected))

    def test_add_end2(self):
        """Check that add_end() works on SLL with one element."""

        old_sll = sll.SLL(20)
        new_sll = sll.add_end(old_sll, 'M')
        expected = [20, 'M']

        self.assertEqual(sll.__str__(new_sll), str(expected))

    def test_add_end3(self):
        """Check that add_end() works on SLL with many elements."""

        old_sll = sll.SLL(20, sll.SLL('A', sll.SLL('omega')))
        new_sll = sll.add_end(old_sll, 'M')
        expected = [20, 'A', 'omega', 'M']

        self.assertEqual(sll.__str__(new_sll), str(expected))

    def test_add_end4(self):
        """Check that add_end() works repeatedly on SLL with no elements."""

        old_sll = None
        new_sll = sll.add_end(old_sll, 'first')
        expected = ['first']
        self.assertEqual(sll.__str__(new_sll), str(expected))

        new_sll = sll.add_end(new_sll, 'second')
        expected = ['first', 'second']
        self.assertEqual(sll.__str__(new_sll), str(expected))

        new_sll = sll.add_end(new_sll, 'third')
        expected = ['first', 'second', 'third']
        self.assertEqual(sll.__str__(new_sll), str(expected))

        new_sll = sll.add_end(new_sll, 'fourth')
        expected = ['first', 'second', 'third', 'fourth']
        self.assertEqual(sll.__str__(new_sll), str(expected))

    def test_find(self):
        """Check that find() works on an empty SLL."""

        my_sll = None
        find = sll.find(my_sll, 20)
        msg = "Expected to not find 20 in SLL '%s', failed" % sll.__str__(my_sll)
        self.assertFalse(find is not None, msg)

    def test_find2(self):
        """Check that find() works on an non-empty SLL."""

        my_sll = sll.SLL('A', sll.SLL(20, sll.SLL('q', sll.SLL('M'))))
        find = sll.find(my_sll, 20)
        msg = "Expected to find 20 in SLL '%s', failed" % sll.__str__(my_sll)
        self.assertTrue(find is not None, msg)

        # check the sub-SLL returned is correct
        expected = sll.SLL(20, sll.SLL('q', sll.SLL('M')))
        msg = ("find('%s', 20) returned '%s', expected '%s'"
               % (sll.__str__(my_sll), sll.__str__(find), sll.__str__(expected)))
        self.assertTrue(sll.__str__(find) == sll.__str__(expected), msg)

    def test_find3(self):
        """Check that find() works on an non-empty SLL with multiple finds."""

        my_sll = sll.SLL('A', sll.SLL(20, sll.SLL('q', sll.SLL(20, sll.SLL('M')))))
        find = sll.find(my_sll, 20)
        msg = "Expected to find 20 in SLL '%s', failed" % sll.__str__(my_sll)
        self.assertTrue(find is not None, msg)

        # check returned sub-SLL is as expected
        expected = sll.SLL(20, sll.SLL('q', sll.SLL(20, sll.SLL('M'))))
        msg = ("find('%s', 20) returned '%s', expected '%s'"
               % (sll.__str__(my_sll), sll.__str__(find), sll.__str__(expected)))
        self.assertTrue(sll.__str__(find) == sll.__str__(expected), msg)

    def test_find4(self):
        """Check that find() works on an non-empty SLL with NO FIND."""

        my_sll = sll.SLL('A', sll.SLL(20, sll.SLL('q', sll.SLL(20, sll.SLL('M')))))
        find = sll.find(my_sll, 'X')
        msg = "Expected to not find 'X' in SLL '%s', succeeded?" % sll.__str__(my_sll)
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
               % (sll.__str__(my_sll), sll.__str__(expected), sll.__str__(result)))
        self.assertTrue(sll.__str__(result) == sll.__str__(expected), msg)

    def test_add_after3(self):
        """Check that add_after() works on an SLL with NO found value."""

        my_sll = sll.SLL('A', sll.SLL(20, sll.SLL('q', sll.SLL(20, sll.SLL('M')))))
        result = sll.add_after(my_sll, 21, 100)
        expected = None
        msg = ("Expected add_after('%s', 21, 100) to return None, got '%s'"
               % (sll.__str__(my_sll), sll.__str__(result)))
        self.assertTrue(sll.__str__(result) == sll.__str__(expected), msg)

    def test_remove(self):
        """Check that remove() works on an empty SLL."""

        my_sll = None
        result = None
        expected = None
        result = sll.remove(my_sll, 21)
        msg = ("Expected remove('%s', 21) to return '%s', got '%s'"
               % (sll.__str__(my_sll), sll.__str__(expected), sll.__str__(result)))
        self.assertTrue(sll.__str__(result) == sll.__str__(expected), msg)

    def test_remove2(self):
        """Check that remove() works on an SLL with a found value."""

        my_sll = sll.SLL('A', sll.SLL(20, sll.SLL('q', sll.SLL(20, sll.SLL('M')))))
        result = sll.remove(my_sll, 'q')
        expected = sll.SLL('A', sll.SLL(20, sll.SLL(20, sll.SLL('M'))))
        msg = ("Expected remove('%s', 21, 100) to return '%s', got '%s'"
               % (sll.__str__(my_sll), sll.__str__(expected), sll.__str__(result)))
        self.assertTrue(sll.__str__(result) == sll.__str__(expected), msg)

    def test_remove3(self):
        """Check that remove() works on an SLL with NO found value."""

        my_sll = sll.SLL('A', sll.SLL(20, sll.SLL('q', sll.SLL(20, sll.SLL('M')))))
        result = sll.remove(my_sll, 22)
        expected = my_sll
        msg = ("Expected remove('%s', 21, 100) to return '%s', got '%s'"
               % (sll.__str__(my_sll), sll.__str__(expected), sll.__str__(result)))
        self.assertTrue(sll.__str__(result) == sll.__str__(expected), msg)

    def test_remove_first(self):
        """Check that remove_first() works on an empty SLL."""

        my_sll = None
        result = sll.remove_first(my_sll)
        expected = None
        msg = ("Expected remove_first('%s') to return '%s', got '%s'"
               % (sll.__str__(my_sll), sll.__str__(expected), sll.__str__(result)))
        self.assertTrue(sll.__str__(result) == sll.__str__(expected), msg)

    def test_remove_first2(self):
        """Check that remove_first() works on a non-empty SLL."""

        my_sll = sll.SLL('A', sll.SLL(20, sll.SLL('q', sll.SLL(20, sll.SLL('M')))))
        result = sll.remove_first(my_sll)
        expected = sll.SLL(20, sll.SLL('q', sll.SLL(20, sll.SLL('M'))))
        msg = ("Expected remove_first('%s') to return '%s', got '%s'"
               % (sll.__str__(my_sll), sll.__str__(expected), sll.__str__(result)))
        self.assertTrue(sll.__str__(result) == sll.__str__(expected), msg)

    def test_remove_last(self):
        """Check that remove_last() works on an empty SLL."""

        my_sll = None
        result = sll.remove_last(my_sll)
        expected = None
        msg = ("Expected remove_last('%s') to return '%s', got '%s'"
               % (sll.__str__(my_sll), sll.__str__(expected), sll.__str__(result)))
        self.assertTrue(sll.__str__(result) == sll.__str__(expected), msg)

    def test_remove_last2(self):
        """Check that remove_last() works on a non-empty SLL."""

        my_sll = sll.SLL('A', sll.SLL(20, sll.SLL('q', sll.SLL(20, sll.SLL('M')))))
        result = sll.remove_last(my_sll)
        expected = sll.SLL('A', sll.SLL(20, sll.SLL('q', sll.SLL(20))))
        msg = ("Expected remove_last('%s') to return '%s', got '%s'"
               % (sll.__str__(my_sll), sll.__str__(expected), sll.__str__(result)))
        self.assertTrue(sll.__str__(result) == sll.__str__(expected), msg)

if __name__ == '__main__':
    suite = unittest.makeSuite(TestSLL,'test')
    runner = unittest.TextTestRunner()
    runner.run(suite)
