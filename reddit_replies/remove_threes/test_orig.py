"""
Original code from the OP, fixed to work.
"""


def remove_triplets(a_list):
    passed_list = a_list[:]     # must copy, else you change the input list
    count = 0
    while count < (len(passed_list) - 2):   # '<', not '<='
        # this is a simpler test for 3 equal in sequence
        if passed_list[count] == passed_list[count + 1] == passed_list[count + 2]:
#            passed_list.pop(count)          # no need for 'count + 1', etc
#            passed_list.pop(count)
#            passed_list.pop(count)
            del passed_list[count:count+3]  # even better
        else:
            count += 1

    return passed_list

##########
# some test code.
# get into the habit of writing test code for stuff like this.
# even better, write test cases BEFORE you write "remove_triplets()".
# look at <https://pymotw.com/3/unittest/index.html#module-unittest>.
##########

import unittest

class MyTest(unittest.TestCase):

    def test_easy(self):
        """Test with OP's data."""

        a_list = [6, 6, 6, 7, 6, 6, 6, 3, 3, 3, 8, 8, 8, 3]
        expected = [7, 3]
        got = remove_triplets(a_list)
        msg = f'Expected result {expected} but got {got}'
        self.assertEqual(expected, got, msg=msg)

    def test_hard1(self):
        """Test with 4 in a row at beginning."""

        a_list = [6, 6, 6, 6, 7, 6, 6, 6, 3, 3, 3, 8, 8, 8, 3]
        expected = [6, 7, 3]
        got = remove_triplets(a_list)
        msg = f'Expected result {expected} but got {got}'
        self.assertEqual(expected, got, msg=msg)

    def test_hard2(self):
        """Test with 4 in a row in the middle."""

        a_list = [6, 6, 6, 7, 6, 6, 6, 3, 3, 3, 3, 8, 8, 8, 3]
        expected = [7, 3, 3]
        got = remove_triplets(a_list)
        msg = f'Expected result {expected} but got {got}'
        self.assertEqual(expected, got, msg=msg)

    def test_hard3(self):
        """Test with 4 in a row at the end."""

        a_list = [6, 6, 6, 7, 6, 6, 6, 3, 3, 3, 8, 8, 8, 3, 3, 3, 3]
        expected = [7, 3]
        got = remove_triplets(a_list)
        msg = f'Expected result {expected} but got {got}'
        self.assertEqual(expected, got, msg=msg)

    def test_hard4(self):
        """Test with 2 long sequence at start."""

        a_list = [6, 6, 7, 6, 6, 6, 3, 3, 3, 8, 8, 8, 3, 3, 3, 3]
        expected = [6, 6, 7, 3]
        got = remove_triplets(a_list)
        msg = f'Expected result {expected} but got {got}'
        self.assertEqual(expected, got, msg=msg)

    def test_hard5(self):
        """Test with 2 long sequence in middle."""

        a_list = [6, 6, 6, 7, 6, 6, 6, 8, 8, 3, 3, 3, 8, 8, 8, 3]
        expected = [7, 8, 8, 3]
        got = remove_triplets(a_list)
        msg = f'Expected result {expected} but got {got}'
        self.assertEqual(expected, got, msg=msg)

    def test_hard6(self):
        """Test with 2 long sequence at end."""

        a_list = [6, 6, 6, 7, 6, 6, 6, 3, 3, 3, 8, 8, 8, 3, 3]
        expected = [7, 3, 3]
        got = remove_triplets(a_list)
        msg = f'Expected result {expected} but got {got}'
        self.assertEqual(expected, got, msg=msg)

unittest.main()

