#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module to test the implementation of the singly-linked list implementations.
"""

import unittest


class TestSLL(unittest.TestCase):

    def create_sll(self, sll_list):
        """Create a test SLL in the appropriate manner for the SLL type.

        sll_list  a python list of desired SLL values
        """

        if ModuleName == 'sll_element':
            result = None
            if sll_list:
                # we have a non-empty list
                for v in sll_list[::-1]:
                    result = Module.SLL(v, result)
            return result
        elif ModuleName == 'sll_tuple':
            result = None
            if sll_list:
                # we have a non-empty list
                for v in sll_list[::-1]:
                    result = [v, result]
            return result    
        else:
            self.fail('BAD MODULENAME: %s' % ModuleName)

    def test_length(self):
        """Check that length() works."""

        test_list = ['M', 'q', 20, 'A']
        my_sll = self.create_sll(test_list)
        expected_len = len(test_list)
        actual_len = Module.length(my_sll)
        msg = "%s: Expected length('%s') to return %d, got %d" % (ModuleName, Module.__str__(my_sll), expected_len, actual_len)
        self.assertEqual(actual_len, expected_len, msg)

    def test_length2(self):
        """Check that len() works on an empty list."""

        test_list = []
        my_sll = self.create_sll(test_list)
        expected_len = len(test_list)
        actual_len = Module.length(my_sll)
        msg = "%s: Expected length('%s') to return %d, got %d" % (ModuleName, Module.__str__(my_sll), expected_len, actual_len)
        self.assertEqual(actual_len, expected_len, msg)

    def test_length3(self):
        """Check that length() works."""

        test_list = ['M']
        my_sll = self.create_sll(test_list)
        expected_len = len(test_list)
        actual_len = Module.length(my_sll)
        msg = "%s: Expected length('%s') to return %d, got %d" % (ModuleName, Module.__str__(my_sll), expected_len, actual_len)
        self.assertEqual(actual_len, expected_len, msg)

    def test_add_front(self):
        """Check that add_front() works for empty SLL."""

        test_list = []
        old_sll = self.create_sll(test_list)
        new_sll = Module.add_front(old_sll, 'A')
        expected_list = ['A']
        expected = self.create_sll(expected_list)
        msg = "%s: Expected add_front(%s, 'A') to return %s, got %s" % (ModuleName, Module.__str__(old_sll),
                                                                        Module.__str__(expected),
                                                                        Module.__str__(new_sll))
        self.assertEqual(Module.__str__(new_sll), Module.__str__(expected), msg)

    def test_add_front2(self):
        """Check that add_front() works on SLL with one element."""

        test_list = [20]
        old_sll = self.create_sll(test_list)
        new_sll = Module.add_front(old_sll, 'M')
        expected_list = ['M', 20]
        expected = self.create_sll(expected_list)
        msg = "%s: Expected add_front(%s, 'M') to return %s, got %s" % (ModuleName, Module.__str__(old_sll),
                                                                        Module.__str__(expected),
                                                                        Module.__str__(new_sll))
        self.assertEqual(Module.__str__(new_sll), Module.__str__(expected), msg)

    def test_add_front3(self):
        """Check that add_front() works on SLL with many elements."""

        test_list = [20, 'A', 'omega']
        old_sll = self.create_sll(test_list)
        new_sll = Module.add_front(old_sll, 'M')
        expected_list = ['M', 20, 'A', 'omega']
        expected = self.create_sll(expected_list)
        msg = "%s: Expected add_front(%s, 'M') to return %s, got %s" % (ModuleName, Module.__str__(old_sll),
                                                                        Module.__str__(expected),
                                                                        Module.__str__(new_sll))
        self.assertEqual(Module.__str__(new_sll), Module.__str__(expected), msg)

    def test_add_front4(self):
        """Check that add_front() works repeatedly on SLL with no elements."""

        test_list = []
        old_sll = self.create_sll(test_list)
        new_sll = Module.add_front(old_sll, 'first')
        expected_list = ['first']
        expected = self.create_sll(expected_list)
        msg = ("%s: add_front(%s, 'first') returned %s, expected %s"
                % (ModuleName, Module.__str__(old_sll), Module.__str__(new_sll), Module.__str__(expected)))
        self.assertEqual(Module.__str__(new_sll), Module.__str__(expected), msg)

        new_sll = Module.add_front(new_sll, 'second')
        expected_list = ['second', 'first']
        expected = self.create_sll(expected_list)
        msg = ("%s: add_front(%s, 'second') returned %s, expected %s"
                % (ModuleName, Module.__str__(old_sll), Module.__str__(new_sll), Module.__str__(expected)))
        self.assertEqual(Module.__str__(new_sll), Module.__str__(expected), msg)

        new_sll = Module.add_front(new_sll, 'third')
        expected_list = ['third', 'second', 'first']
        expected = self.create_sll(expected_list)
        msg = ("%s: add_front(%s, 'third') returned %s, expected %s"
                % (ModuleName, Module.__str__(old_sll), Module.__str__(new_sll), Module.__str__(expected)))
        self.assertEqual(Module.__str__(new_sll), Module.__str__(expected), msg)

        new_sll = Module.add_front(new_sll, 'fourth')
        expected_list = ['fourth', 'third', 'second', 'first']
        expected = self.create_sll(expected_list)
        msg = ("%s: add_front(%s, 'fourth') returned %s, expected %s"
                % (ModuleName, Module.__str__(old_sll), Module.__str__(new_sll), Module.__str__(expected)))
        self.assertEqual(Module.__str__(new_sll), Module.__str__(expected), msg)

    def test_add_back(self):
        """Check that add_back() works for empty SLL."""

        test_list = []
        old_sll = self.create_sll(test_list)
        new_sll = Module.add_back(old_sll, 'A')
        expected_list = ['A']
        expected = self.create_sll(expected_list)
        msg = ("%s: add_back(%s, 'A') returned %s, expected %s"
                % (ModuleName, Module.__str__(old_sll), Module.__str__(new_sll), Module.__str__(expected)))
        self.assertEqual(Module.__str__(new_sll), Module.__str__(expected), msg)

    def test_add_back2(self):
        """Check that add_back() works on SLL with one element."""

        test_list = [20]
        old_sll = self.create_sll(test_list)
        new_sll = Module.add_back(old_sll, 'M')
        expected_list = [20, 'M']
        expected = self.create_sll(expected_list)
        msg = ("%s: add_back(%s, 'M') returned %s, expected %s"
                % (ModuleName, Module.__str__(old_sll), Module.__str__(new_sll), Module.__str__(expected)))
        self.assertEqual(Module.__str__(new_sll), Module.__str__(expected), msg)

    def test_add_back3(self):
        """Check that add_back() works on SLL with many elements."""

        test_list = [20, 'A', 'omega']
        old_sll = self.create_sll(test_list)
        new_sll = Module.add_back(old_sll, 'M')
        expected_list = [20, 'A', 'omega', 'M']
        expected = self.create_sll(expected_list)
        msg = ("%s: add_back(%s, 'M') returned %s, expected %s"
                % (ModuleName, Module.__str__(old_sll), Module.__str__(new_sll), Module.__str__(expected)))
        self.assertEqual(Module.__str__(new_sll), Module.__str__(expected), msg)

    def test_add_back4(self):
        """Check that add_back() works repeatedly on SLL with no elements."""

        test_list = []
        old_sll = self.create_sll(test_list)
        new_sll = Module.add_back(old_sll, 'first')
        expected_list = ['first']
        expected = self.create_sll(expected_list)
        msg = ("%s: add_back(%s, 'first') returned %s, expected %s"
                % (ModuleName, Module.__str__(old_sll), Module.__str__(new_sll), Module.__str__(expected)))
        self.assertEqual(Module.__str__(new_sll), Module.__str__(expected), msg)

        new_sll = Module.add_back(new_sll, 'second')
        expected_list = ['first', 'second']
        expected = self.create_sll(expected_list)
        msg = ("%s: add_back(%s, 'second') returned %s, expected %s"
                % (ModuleName, Module.__str__(old_sll), Module.__str__(new_sll), Module.__str__(expected)))
        self.assertEqual(Module.__str__(new_sll), Module.__str__(expected), msg)

        new_sll = Module.add_back(new_sll, 'third')
        expected_list = ['first', 'second', 'third']
        expected = self.create_sll(expected_list)
        msg = ("%s: add_back(%s, 'third') returned %s, expected %s"
                % (ModuleName, Module.__str__(old_sll), Module.__str__(new_sll), Module.__str__(expected)))
        self.assertEqual(Module.__str__(new_sll), Module.__str__(expected), msg)

        new_sll = Module.add_back(new_sll, 'fourth')
        expected_list = ['first', 'second', 'third', 'fourth']
        expected = self.create_sll(expected_list)
        msg = ("%s: add_back(%s, 'fourth') returned %s, expected %s"
                % (ModuleName, Module.__str__(old_sll), Module.__str__(new_sll), Module.__str__(expected)))
        self.assertEqual(Module.__str__(new_sll), Module.__str__(expected), msg)

    def test_find(self):
        """Check that find() works on an empty SLL."""

        test_list = []
        my_sll = self.create_sll(test_list)
        find = Module.find(my_sll, 20)
        msg = "%s: Expected to not find 20 in SLL '%s', failed" % (ModuleName, Module.__str__(my_sll))
        self.assertFalse(find is not None, msg)

    def test_find2(self):
        """Check that find() works on an non-empty SLL."""

        test_list = ['A', 20, 'q', 'M']
        my_sll = self.create_sll(test_list)
        find = Module.find(my_sll, 20)
        msg = "%s: Expected to find 20 in SLL '%s', failed" % (ModuleName, Module.__str__(my_sll))
        self.assertTrue(find is not None, msg)

        # check the sub-SLL returned is correct
        expected = self.create_sll(test_list[1:])
        msg = ("%s: find('%s', 20) returned '%s', expected '%s'"
               % (ModuleName, Module.__str__(my_sll), Module.__str__(find), Module.__str__(expected)))
        self.assertTrue(Module.__str__(find) == Module.__str__(expected), msg)

    def test_find3(self):
        """Check that find() works on an non-empty SLL with multiple finds."""

        test_list = ['A', 20, 'q', 20, 'M']
        my_sll = self.create_sll(test_list)
        find = Module.find(my_sll, 20)
        msg = "%s: Expected to find 20 in SLL '%s', failed" % (ModuleName, Module.__str__(my_sll))
        self.assertTrue(find is not None, msg)

        # check returned sub-SLL is as expected
        expected = self.create_sll(test_list[1:])
        msg = ("%s: find('%s', 20) returned '%s', expected '%s'"
               % (ModuleName, Module.__str__(my_sll), Module.__str__(find), Module.__str__(expected)))
        self.assertTrue(Module.__str__(find) == Module.__str__(expected), msg)

    def test_find4(self):
        """Check that find() works on an non-empty SLL with NO FIND."""

        test_list = ['A', 20, 'q', 20, 'M']
        my_sll = self.create_sll(test_list)
        find = Module.find(my_sll, 'X')
        msg = "%s: Expected to not find 'X' in SLL '%s', succeeded?" % (ModuleName, Module.__str__(my_sll))
        self.assertTrue(find is None, msg)

    def test_add_after(self):
        """Check that add_after() works on an empty SLL."""

        test_list = []
        my_sll = self.create_sll(test_list)
        result = Module.add_after(my_sll, 20, 100)
        msg = "%s: Expected add_after(None, 20, 100) to fail, didn't, got '%s'" % (ModuleName, str(result))
        self.assertTrue(result is None, msg)

    def test_add_after2(self):
        """Check that add_after() works on an SLL with found value."""

        test_list = ['A', 20, 'q', 20, 'M']
        my_sll = self.create_sll(test_list)
        result = Module.add_after(my_sll, 20, 100)
        expected_list = ['A', 20, 100, 'q', 20, 'M']
        expected = self.create_sll(expected_list)
        msg = ("%s: Expected add_after('%s', 20, 100) to return '%s', got '%s'"
               % (ModuleName, Module.__str__(my_sll), Module.__str__(expected), Module.__str__(result)))
        self.assertTrue(Module.__str__(result) == Module.__str__(expected), msg)

    def test_add_after3(self):
        """Check that add_after() works on an SLL with NO found value."""

        test_list = ['A', 20, 'q', 20, 'M']
        my_sll = self.create_sll(test_list)
        result = Module.add_after(my_sll, 21, 100)
        expected_list = []
        expected = self.create_sll(expected_list)
        msg = ("%s: Expected add_after('%s', 21, 100) to return None, got '%s'"
               % (ModuleName, Module.__str__(my_sll), Module.__str__(result)))
        self.assertTrue(Module.__str__(result) == Module.__str__(expected), msg)

    def test_remove(self):
        """Check that remove() works on an empty SLL."""

        test_list = []
        my_sll = self.create_sll(test_list)
        result = None
        expected_list = []
        expected = self.create_sll(expected_list)
        result = Module.remove(my_sll, 21)
        msg = ("%s: Expected remove('%s', 21) to return '%s', got '%s'"
               % (ModuleName, Module.__str__(my_sll), Module.__str__(expected), Module.__str__(result)))
        self.assertTrue(Module.__str__(result) == Module.__str__(expected), msg)

    def test_remove2(self):
        """Check that remove() works on an SLL with a found value."""

        test_list = ['A', 20, 'q', 20, 'M']
        my_sll = self.create_sll(test_list)
        result = Module.remove(my_sll, 'q')
        expected_list = ['A', 20, 20, 'M']
        expected = self.create_sll(expected_list)
        msg = ("%s: Expected remove('%s', 21, 100) to return '%s', got '%s'"
               % (ModuleName, Module.__str__(my_sll), Module.__str__(expected), Module.__str__(result)))
        self.assertTrue(Module.__str__(result) == Module.__str__(expected), msg)

    def test_remove3(self):
        """Check that remove() works on an SLL with NO found value."""

        test_list = ['A', 20, 'q', 20, 'M']
        my_sll = self.create_sll(test_list)
        result = Module.remove(my_sll, 22)
        expected = my_sll
        msg = ("%s: Expected remove('%s', 21, 100) to return '%s', got '%s'"
               % (ModuleName, Module.__str__(my_sll), Module.__str__(expected), Module.__str__(result)))
        self.assertTrue(Module.__str__(result) == Module.__str__(expected), msg)

    def test_remove_first(self):
        """Check that remove_first() works on an empty SLL."""

        test_list = []
        my_sll = self.create_sll(test_list)
        result = Module.remove_first(my_sll)
        expected_list = []
        expected = self.create_sll(expected_list)
        msg = ("%s: Expected remove_first('%s') to return '%s', got '%s'"
               % (ModuleName, Module.__str__(my_sll), Module.__str__(expected), Module.__str__(result)))
        self.assertTrue(Module.__str__(result) == Module.__str__(expected), msg)

    def test_remove_first2(self):
        """Check that remove_first() works on a non-empty SLL."""

        test_list = ['A', 20, 'q', 20, 'M']
        my_sll = self.create_sll(test_list)
        result = Module.remove_first(my_sll)
        expected_list = test_list[1:]
        expected = self.create_sll(expected_list)
        msg = ("%s: Expected remove_first('%s') to return '%s', got '%s'"
               % (ModuleName, Module.__str__(my_sll), Module.__str__(expected), Module.__str__(result)))
        self.assertTrue(Module.__str__(result) == Module.__str__(expected), msg)

    def test_remove_last(self):
        """Check that remove_last() works on an empty SLL."""

        test_list = []
        my_sll = self.create_sll(test_list)
        result = Module.remove_last(my_sll)
        expected_list = []
        expected = self.create_sll(expected_list)
        msg = ("%s: Expected remove_last('%s') to return '%s', got '%s'"
               % (ModuleName, Module.__str__(my_sll), Module.__str__(expected), Module.__str__(result)))
        self.assertTrue(Module.__str__(result) == Module.__str__(expected), msg)

    def test_remove_last2(self):
        """Check that remove_last() works on a non-empty SLL."""

        test_list = ['A', 20, 'q', 20, 'M']
        my_sll = self.create_sll(test_list)
        result = Module.remove_last(my_sll)
        expected_list = test_list[:-1]
        expected = self.create_sll(expected_list)
        msg = ("%s: Expected remove_last('%s') to return '%s', got '%s'"
               % (ModuleName, Module.__str__(my_sll), Module.__str__(expected), Module.__str__(result)))
        self.assertTrue(Module.__str__(result) == Module.__str__(expected), msg)

    def test_map_fun(self):
        """Check the map_fun() function."""

        test_list = [1, 2, -3, 5, 100]
        my_sll = self.create_sll(test_list)
        func = lambda x, y: x + y
        result = Module.map_fun(my_sll, func, 1)
        expected_list = [x + 1 for x in test_list]
        expected = self.create_sll(expected_list)
        msg = ("%s: Expected map_fun('%s', func, 1) to return '%s', got '%s'"
               % (ModuleName, Module.__str__(my_sll), Module.__str__(expected), Module.__str__(result)))
        self.assertTrue(Module.__str__(result) == Module.__str__(expected), msg)


if __name__ == '__main__':
    global Module, ModuleName

    suite = unittest.makeSuite(TestSLL,'test')
    runner = unittest.TextTestRunner()

    delim = '*' * 100

    import sll_element
    Module = sll_element
    ModuleName = 'sll_element'
    delim2 = '* %s' % ModuleName
    print('\n%s' % delim)
    print('%s' % delim2)
    print('%s' % delim)
    runner.run(suite)

    import sll_tuple
    Module = sll_tuple
    ModuleName = 'sll_tuple'
    delim2 = '* %s' % ModuleName
    print('\n%s' % delim)
    print('%s' % delim2)
    print('%s' % delim)
    runner.run(suite)
