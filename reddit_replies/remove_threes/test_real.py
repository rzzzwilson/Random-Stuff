"""
Another way of doing it.
Keep note of index of each 3-sequence start and delete later.
"""


def remove_triplets(a_list):
    indices = []                    # start index of sequences to remove
    max_count = len(a_list) - 2     # because we check sequences of 3
    count = 0
    while count < max_count:
        if a_list[count] == a_list[count + 1] == a_list[count + 2]:
            indices.append(count)   # equal, remember index of start of 3 sequence
            count += 3              # skip to character after 3-sequence
        else:
            count += 1              # else just try next group of three

    result = a_list[:]              # must use copy else we change input list!
    for i in reversed(indices):     # must work right to left!
        del result[i:i+3]           # delete 3 in one go

    return result


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

