#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module to test the implementation of the singly-linked list implementations.
"""

import unittest


class TestSSL(unittest.TestCase):

    def create_ssl(self, ssl_list):
        """Create a test SSL in the appropriate manner for the SSL type.

        ssl_list  a python list of desired SSL values
        """

        if ModuleName == 'ssl_element':
            result = None
            if ssl_list:
                # we have a non-empty list
                for v in ssl_list[::-1]:
                    result = Module.SSL(v, result)
            return result
        elif ModuleName == 'ssl_tuple':
            result = None
            if ssl_list:
                # we have a non-empty list
                for v in ssl_list[::-1]:
                    result = [v, result]
            return result    
        else:
            self.assertFail('BAD MODULENAME: %s' % ModuleName)

    def test_length(self):
        """Check that length() works."""

        test_list = ['M', 'q', 20, 'A']
        my_ssl = self.create_ssl(test_list)
        expected_len = len(test_list)
        actual_len = Module.length(my_ssl)
        msg = "%s: Expected length('%s') to return %d, got %d" % (ModuleName, Module.__str__(my_ssl), expected_len, actual_len)
        self.assertEqual(actual_len, expected_len, msg)

    def test_length2(self):
        """Check that len() works on an empty list."""

        test_list = []
        my_ssl = self.create_ssl(test_list)
        expected_len = len(test_list)
        actual_len = Module.length(my_ssl)
        msg = "%s: Expected length('%s') to return %d, got %d" % (ModuleName, Module.__str__(my_ssl), expected_len, actual_len)
        self.assertEqual(actual_len, expected_len, msg)

    def test_length3(self):
        """Check that length() works."""

        test_list = ['M']
        my_ssl = self.create_ssl(test_list)
        expected_len = len(test_list)
        actual_len = Module.length(my_ssl)
        msg = "%s: Expected length('%s') to return %d, got %d" % (ModuleName, Module.__str__(my_ssl), expected_len, actual_len)
        self.assertEqual(actual_len, expected_len, msg)

    def test_add_front(self):
        """Check that add_front() works for empty SSL."""

        test_list = []
        old_ssl = self.create_ssl(test_list)
        new_ssl = Module.add_front(old_ssl, 'A')
        expected_list = ['A']
        expected = self.create_ssl(expected_list)
        msg = "%s: Expected add_front(%s, 'A') to return %s, got %s" % (ModuleName, Module.__str__(old_ssl),
                                                                        Module.__str__(expected),
                                                                        Module.__str__(new_ssl))
        self.assertEqual(Module.__str__(new_ssl), Module.__str__(expected), msg)

    def test_add_front2(self):
        """Check that add_front() works on SSL with one element."""

        test_list = [20]
        old_ssl = self.create_ssl(test_list)
        new_ssl = Module.add_front(old_ssl, 'M')
        expected_list = ['M', 20]
        expected = self.create_ssl(expected_list)
        msg = "%s: Expected add_front(%s, 'M') to return %s, got %s" % (ModuleName, Module.__str__(old_ssl),
                                                                        Module.__str__(expected),
                                                                        Module.__str__(new_ssl))
        self.assertEqual(Module.__str__(new_ssl), Module.__str__(expected), msg)

    def test_add_front3(self):
        """Check that add_front() works on SSL with many elements."""

        test_list = [20, 'A', 'omega']
        old_ssl = self.create_ssl(test_list)
        new_ssl = Module.add_front(old_ssl, 'M')
        expected_list = ['M', 20, 'A', 'omega']
        expected = self.create_ssl(expected_list)
        msg = "%s: Expected add_front(%s, 'M') to return %s, got %s" % (ModuleName, Module.__str__(old_ssl),
                                                                        Module.__str__(expected),
                                                                        Module.__str__(new_ssl))
        self.assertEqual(Module.__str__(new_ssl), Module.__str__(expected), msg)

    def test_add_front4(self):
        """Check that add_front() works repeatedly on SSL with no elements."""

        test_list = []
        old_ssl = self.create_ssl(test_list)
        new_ssl = Module.add_front(old_ssl, 'first')
        expected_list = ['first']
        expected = self.create_ssl(expected_list)
        msg = ("%s: add_front(%s, 'first') returned %s, expected %s"
                % (ModuleName, Module.__str__(old_ssl), Module.__str__(new_ssl), Module.__str__(expected)))
        self.assertEqual(Module.__str__(new_ssl), Module.__str__(expected), msg)

        new_ssl = Module.add_front(new_ssl, 'second')
        expected_list = ['second', 'first']
        expected = self.create_ssl(expected_list)
        msg = ("%s: add_front(%s, 'second') returned %s, expected %s"
                % (ModuleName, Module.__str__(old_ssl), Module.__str__(new_ssl), Module.__str__(expected)))
        self.assertEqual(Module.__str__(new_ssl), Module.__str__(expected), msg)

        new_ssl = Module.add_front(new_ssl, 'third')
        expected_list = ['third', 'second', 'first']
        expected = self.create_ssl(expected_list)
        msg = ("%s: add_front(%s, 'third') returned %s, expected %s"
                % (ModuleName, Module.__str__(old_ssl), Module.__str__(new_ssl), Module.__str__(expected)))
        self.assertEqual(Module.__str__(new_ssl), Module.__str__(expected), msg)

        new_ssl = Module.add_front(new_ssl, 'fourth')
        expected_list = ['fourth', 'third', 'second', 'first']
        expected = self.create_ssl(expected_list)
        msg = ("%s: add_front(%s, 'fourth') returned %s, expected %s"
                % (ModuleName, Module.__str__(old_ssl), Module.__str__(new_ssl), Module.__str__(expected)))
        self.assertEqual(Module.__str__(new_ssl), Module.__str__(expected), msg)

    def test_add_end(self):
        """Check that add_end() works for empty SSL."""

        test_list = []
        old_ssl = self.create_ssl(test_list)
        new_ssl = Module.add_end(old_ssl, 'A')
        expected_list = ['A']
        expected = self.create_ssl(expected_list)
        msg = ("%s: add_end(%s, 'A') returned %s, expected %s"
                % (ModuleName, Module.__str__(old_ssl), Module.__str__(new_ssl), Module.__str__(expected)))
        self.assertEqual(Module.__str__(new_ssl), Module.__str__(expected), msg)

    def test_add_end2(self):
        """Check that add_end() works on SSL with one element."""

        test_list = [20]
        old_ssl = self.create_ssl(test_list)
        new_ssl = Module.add_end(old_ssl, 'M')
        expected_list = [20, 'M']
        expected = self.create_ssl(expected_list)
        msg = ("%s: add_end(%s, 'M') returned %s, expected %s"
                % (ModuleName, Module.__str__(old_ssl), Module.__str__(new_ssl), Module.__str__(expected)))
        self.assertEqual(Module.__str__(new_ssl), Module.__str__(expected), msg)

    def test_add_end3(self):
        """Check that add_end() works on SSL with many elements."""

        test_list = [20, 'A', 'omega']
        old_ssl = self.create_ssl(test_list)
        new_ssl = Module.add_end(old_ssl, 'M')
        expected_list = [20, 'A', 'omega', 'M']
        expected = self.create_ssl(expected_list)
        msg = ("%s: add_end(%s, 'M') returned %s, expected %s"
                % (ModuleName, Module.__str__(old_ssl), Module.__str__(new_ssl), Module.__str__(expected)))
        self.assertEqual(Module.__str__(new_ssl), Module.__str__(expected), msg)

    def test_add_end4(self):
        """Check that add_end() works repeatedly on SSL with no elements."""

        test_list = []
        old_ssl = self.create_ssl(test_list)
        new_ssl = Module.add_end(old_ssl, 'first')
        expected_list = ['first']
        expected = self.create_ssl(expected_list)
        msg = ("%s: add_end(%s, 'first') returned %s, expected %s"
                % (ModuleName, Module.__str__(old_ssl), Module.__str__(new_ssl), Module.__str__(expected)))
        self.assertEqual(Module.__str__(new_ssl), Module.__str__(expected), msg)

        new_ssl = Module.add_end(new_ssl, 'second')
        expected_list = ['first', 'second']
        expected = self.create_ssl(expected_list)
        msg = ("%s: add_end(%s, 'second') returned %s, expected %s"
                % (ModuleName, Module.__str__(old_ssl), Module.__str__(new_ssl), Module.__str__(expected)))
        self.assertEqual(Module.__str__(new_ssl), Module.__str__(expected), msg)

        new_ssl = Module.add_end(new_ssl, 'third')
        expected_list = ['first', 'second', 'third']
        expected = self.create_ssl(expected_list)
        msg = ("%s: add_end(%s, 'third') returned %s, expected %s"
                % (ModuleName, Module.__str__(old_ssl), Module.__str__(new_ssl), Module.__str__(expected)))
        self.assertEqual(Module.__str__(new_ssl), Module.__str__(expected), msg)

        new_ssl = Module.add_end(new_ssl, 'fourth')
        expected_list = ['first', 'second', 'third', 'fourth']
        expected = self.create_ssl(expected_list)
        msg = ("%s: add_end(%s, 'fourth') returned %s, expected %s"
                % (ModuleName, Module.__str__(old_ssl), Module.__str__(new_ssl), Module.__str__(expected)))
        self.assertEqual(Module.__str__(new_ssl), Module.__str__(expected), msg)

    def test_find(self):
        """Check that find() works on an empty SSL."""

        test_list = []
        my_ssl = self.create_ssl(test_list)
        find = Module.find(my_ssl, 20)
        msg = "%s: Expected to not find 20 in SSL '%s', failed" % (ModuleName, Module.__str__(my_ssl))
        self.assertFalse(find is not None, msg)

    def test_find2(self):
        """Check that find() works on an non-empty SSL."""

        test_list = ['A', 20, 'q', 'M']
        my_ssl = self.create_ssl(test_list)
        find = Module.find(my_ssl, 20)
        msg = "%s: Expected to find 20 in SSL '%s', failed" % (ModuleName, Module.__str__(my_ssl))
        self.assertTrue(find is not None, msg)

        # check the sub-SSL returned is correct
        expected = self.create_ssl(test_list[1:])
        msg = ("%s: find('%s', 20) returned '%s', expected '%s'"
               % (ModuleName, Module.__str__(my_ssl), Module.__str__(find), Module.__str__(expected)))
        self.assertTrue(Module.__str__(find) == Module.__str__(expected), msg)

    def test_find3(self):
        """Check that find() works on an non-empty SSL with multiple finds."""

        test_list = ['A', 20, 'q', 20, 'M']
        my_ssl = self.create_ssl(test_list)
        find = Module.find(my_ssl, 20)
        msg = "%s: Expected to find 20 in SSL '%s', failed" % (ModuleName, Module.__str__(my_ssl))
        self.assertTrue(find is not None, msg)

        # check returned sub-SSL is as expected
        expected = self.create_ssl(test_list[1:])
        msg = ("%s: find('%s', 20) returned '%s', expected '%s'"
               % (ModuleName, Module.__str__(my_ssl), Module.__str__(find), Module.__str__(expected)))
        self.assertTrue(Module.__str__(find) == Module.__str__(expected), msg)

    def test_find4(self):
        """Check that find() works on an non-empty SSL with NO FIND."""

        test_list = ['A', 20, 'q', 20, 'M']
        my_ssl = self.create_ssl(test_list)
        find = Module.find(my_ssl, 'X')
        msg = "%s: Expected to not find 'X' in SSL '%s', succeeded?" % (ModuleName, Module.__str__(my_ssl))
        self.assertTrue(find is None, msg)

    def test_add_after(self):
        """Check that add_after() works on an empty SSL."""

        test_list = []
        my_ssl = self.create_ssl(test_list)
        result = Module.add_after(my_ssl, 20, 100)
        msg = "%s: Expected add_after(None, 20, 100) to fail, didn't, got '%s'" % (ModuleName, str(result))
        self.assertTrue(result is None, msg)

    def test_add_after2(self):
        """Check that add_after() works on an SSL with found value."""

        test_list = ['A', 20, 'q', 20, 'M']
        my_ssl = self.create_ssl(test_list)
        result = Module.add_after(my_ssl, 20, 100)
        expected_list = ['A', 20, 100, 'q', 20, 'M']
        expected = self.create_ssl(expected_list)
        msg = ("%s: Expected add_after('%s', 20, 100) to return '%s', got '%s'"
               % (ModuleName, Module.__str__(my_ssl), Module.__str__(expected), Module.__str__(result)))
        self.assertTrue(Module.__str__(result) == Module.__str__(expected), msg)

    def test_add_after3(self):
        """Check that add_after() works on an SSL with NO found value."""

        test_list = ['A', 20, 'q', 20, 'M']
        my_ssl = self.create_ssl(test_list)
        result = Module.add_after(my_ssl, 21, 100)
        expected_list = []
        expected = self.create_ssl(expected_list)
        msg = ("%s: Expected add_after('%s', 21, 100) to return None, got '%s'"
               % (ModuleName, Module.__str__(my_ssl), Module.__str__(result)))
        self.assertTrue(Module.__str__(result) == Module.__str__(expected), msg)

    def test_remove(self):
        """Check that remove() works on an empty SSL."""

        test_list = []
        my_ssl = self.create_ssl(test_list)
        result = None
        expected_list = []
        expected = self.create_ssl(expected_list)
        result = Module.remove(my_ssl, 21)
        msg = ("%s: Expected remove('%s', 21) to return '%s', got '%s'"
               % (ModuleName, Module.__str__(my_ssl), Module.__str__(expected), Module.__str__(result)))
        self.assertTrue(Module.__str__(result) == Module.__str__(expected), msg)

    def test_remove2(self):
        """Check that remove() works on an SSL with a found value."""

        test_list = ['A', 20, 'q', 20, 'M']
        my_ssl = self.create_ssl(test_list)
        result = Module.remove(my_ssl, 'q')
        expected_list = ['A', 20, 20, 'M']
        expected = self.create_ssl(expected_list)
        msg = ("%s: Expected remove('%s', 21, 100) to return '%s', got '%s'"
               % (ModuleName, Module.__str__(my_ssl), Module.__str__(expected), Module.__str__(result)))
        self.assertTrue(Module.__str__(result) == Module.__str__(expected), msg)

    def test_remove3(self):
        """Check that remove() works on an SSL with NO found value."""

        test_list = ['A', 20, 'q', 20, 'M']
        my_ssl = self.create_ssl(test_list)
        result = Module.remove(my_ssl, 22)
        expected = my_ssl
        msg = ("%s: Expected remove('%s', 21, 100) to return '%s', got '%s'"
               % (ModuleName, Module.__str__(my_ssl), Module.__str__(expected), Module.__str__(result)))
        self.assertTrue(Module.__str__(result) == Module.__str__(expected), msg)

    def test_remove_first(self):
        """Check that remove_first() works on an empty SSL."""

        test_list = []
        my_ssl = self.create_ssl(test_list)
        result = Module.remove_first(my_ssl)
        expected_list = []
        expected = self.create_ssl(expected_list)
        msg = ("%s: Expected remove_first('%s') to return '%s', got '%s'"
               % (ModuleName, Module.__str__(my_ssl), Module.__str__(expected), Module.__str__(result)))
        self.assertTrue(Module.__str__(result) == Module.__str__(expected), msg)

    def test_remove_first2(self):
        """Check that remove_first() works on a non-empty SSL."""

        test_list = ['A', 20, 'q', 20, 'M']
        my_ssl = self.create_ssl(test_list)
        result = Module.remove_first(my_ssl)
        expected_list = test_list[1:]
        expected = self.create_ssl(expected_list)
        msg = ("%s: Expected remove_first('%s') to return '%s', got '%s'"
               % (ModuleName, Module.__str__(my_ssl), Module.__str__(expected), Module.__str__(result)))
        self.assertTrue(Module.__str__(result) == Module.__str__(expected), msg)

    def test_remove_last(self):
        """Check that remove_last() works on an empty SSL."""

        test_list = []
        my_ssl = self.create_ssl(test_list)
        result = Module.remove_last(my_ssl)
        expected_list = []
        expected = self.create_ssl(expected_list)
        msg = ("%s: Expected remove_last('%s') to return '%s', got '%s'"
               % (ModuleName, Module.__str__(my_ssl), Module.__str__(expected), Module.__str__(result)))
        self.assertTrue(Module.__str__(result) == Module.__str__(expected), msg)

    def test_remove_last2(self):
        """Check that remove_last() works on a non-empty SSL."""

        test_list = ['A', 20, 'q', 20, 'M']
        my_ssl = self.create_ssl(test_list)
        result = Module.remove_last(my_ssl)
        expected_list = test_list[:-1]
        expected = self.create_ssl(expected_list)
        msg = ("%s: Expected remove_last('%s') to return '%s', got '%s'"
               % (ModuleName, Module.__str__(my_ssl), Module.__str__(expected), Module.__str__(result)))
        self.assertTrue(Module.__str__(result) == Module.__str__(expected), msg)

if __name__ == '__main__':
    global Module, ModuleName

    suite = unittest.makeSuite(TestSSL,'test')
    runner = unittest.TextTestRunner()

    import ssl_element
    Module = ssl_element
    ModuleName = 'ssl_element'
    print('\n%s %s' % (ModuleName, '.oOo. '*14))
    runner.run(suite)

    import ssl_tuple
    Module = ssl_tuple
    ModuleName = 'ssl_tuple'
    print('\n%s %s' % (ModuleName, '.oOo. '*14))
    runner.run(suite)

