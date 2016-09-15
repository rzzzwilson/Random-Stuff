#!/usr/bin/env python

"""
Some code in answer to:
https://www.reddit.com/r/learnpython/comments/52v5sz/sorted_list_iterating/

It appears that we have two lists of integers (sorted) A and B, and we need
to return two lists X and Y where:
    X is the list of integers in A but not in B
    Y is the list of integers in B but not in A
There is a restriction: we can't use the 'in' operator.
"""

def pop_list(l):
    """Pop a value from THE FRONT of list 'l', return None if nothing to pop."""

    try:
        return l.pop(0)
    except IndexError:
        return None

def check(AA, BB):
    """Return two lists X and Y where:
          X is a list of elements in A but not in B
          Y is a list of elements in B but not in A
    """

    # duplicate lists so we don't change originals
    A = AA[:]
    B = BB[:]

    # prepare result lists
    X = []
    Y = []

    # get leftmost elements of A and B
    last_a = pop_list(A)
    last_b = pop_list(B)

    while last_a or last_b:
        # loop while we still have at least one value

        if last_a and last_b:
            # both values not None
            if last_a == last_b:
                # same value in both lists, ignore value and read again from both input lists
                last_a = pop_list(A)
                last_b = pop_list(B)
            elif last_a < last_b:
                # last_a is in A but not B, append to X, get new A value
                X.append(last_a)
                last_a = pop_list(A)
            else:
                # last_b is in B but not A, append to Y, get new B value
                Y.append(last_b)
                last_b = pop_list(B)
        else:
            # either list A or B has ended
            if last_b is None:
                # B empty, add all remaining in A to X 
                X.append(last_a)
                X.extend(A)
            else:
                # A empty, add all remaining in B to Y 
                Y.append(last_b)
                Y.extend(B)
            break

    return (X, Y)


if __name__ == '__main__':
    import os
    import unittest
    import tempfile

    class SLTTest(unittest.TestCase):
        def test_simple(self):
            """Test for both input lists empty."""

            A = []
            A.sort()
            B = []
            B.sort()
            (X, Y) = check(A, B)
            expected_X = []
            expected_Y = []
            msg = ('check(%s, %s) should return (%s, %s), but got (%s, %s)'
                   % (str(A), str(B), str(expected_X), str(expected_Y), str(X), str(Y)))
            self.assertTrue(X == expected_X and Y == expected_Y, msg)

        def test_only_A(self):
            """Test for only A containing values."""

            A = [2, 6, 1, 8]
            A.sort()
            B = []
            B.sort()
            (X, Y) = check(A, B)
            expected_X = [1, 2, 6, 8]
            expected_Y = []
            msg = ('check(%s, %s) should return (%s, %s), but got (%s, %s)'
                   % (str(A), str(B), str(expected_X), str(expected_Y), str(X), str(Y)))
            self.assertTrue(X == expected_X and Y == expected_Y, msg)

        def test_only_B(self):
            """Test for only B containing values."""

            A = []
            A.sort()
            B = [2, 8, 1, 7]
            B.sort()
            (X, Y) = check(A, B)
            expected_X = []
            expected_Y = [1, 2, 7, 8]
            msg = ('check(%s, %s) should return (%s, %s), but got (%s, %s)'
                   % (str(A), str(B), str(expected_X), str(expected_Y), str(X), str(Y)))
            self.assertTrue(X == expected_X and Y == expected_Y, msg)

        def test_only_A_extra(self):
            """Test for only A contains values not in B.
               Extra value at front.
            """

            A = [1, 2, 3, 4, 5]
            A.sort()
            B = [2, 3, 4, 5]
            B.sort()
            (X, Y) = check(A, B)
            expected_X = [1]
            expected_Y = []
            msg = ('check(%s, %s) should return (%s, %s), but got (%s, %s)'
                   % (str(A), str(B), str(expected_X), str(expected_Y), str(X), str(Y)))
            self.assertTrue(X == expected_X and Y == expected_Y, msg)

        def test_only_A_extra2(self):
            """Test for only A contains values not in B.
               Extra value at middle.
            """

            A = [1, 2, 3, 4, 5]
            A.sort()
            B = [1, 2, 4, 5]
            B.sort()
            (X, Y) = check(A, B)
            expected_X = [3]
            expected_Y = []
            msg = ('check(%s, %s) should return (%s, %s), but got (%s, %s)'
                   % (str(A), str(B), str(expected_X), str(expected_Y), str(X), str(Y)))
            self.assertTrue(X == expected_X and Y == expected_Y, msg)

        def test_only_A_extra3(self):
            """Test for only A contains values not in B.
               Extra value at end.
            """

            A = [1, 2, 3, 4, 5]
            A.sort()
            B = [1, 2, 3, 4]
            B.sort()
            (X, Y) = check(A, B)
            expected_X = [5]
            expected_Y = []
            msg = ('check(%s, %s) should return (%s, %s), but got (%s, %s)'
                   % (str(A), str(B), str(expected_X), str(expected_Y), str(X), str(Y)))
            self.assertTrue(X == expected_X and Y == expected_Y, msg)

        def test_only_B_extra(self):
            """Test for only B contains values not in A.
               Extra value at front.
            """

            A = [2, 3, 4, 5]
            A.sort()
            B = [1, 2, 3, 4, 5]
            B.sort()
            (X, Y) = check(A, B)
            expected_X = []
            expected_Y = [1]
            msg = ('check(%s, %s) should return (%s, %s), but got (%s, %s)'
                   % (str(A), str(B), str(expected_X), str(expected_Y), str(X), str(Y)))
            self.assertTrue(X == expected_X and Y == expected_Y, msg)

        def test_only_B_extra2(self):
            """Test for only A contains values not in B.
               Extra value at middle.
            """

            A = [1, 2, 4, 5]
            A.sort()
            B = [1, 2, 3, 4, 5]
            B.sort()
            (X, Y) = check(A, B)
            expected_X = []
            expected_Y = [3]
            msg = ('check(%s, %s) should return (%s, %s), but got (%s, %s)'
                   % (str(A), str(B), str(expected_X), str(expected_Y), str(X), str(Y)))
            self.assertTrue(X == expected_X and Y == expected_Y, msg)

        def test_only_B_extra3(self):
            """Test for only B contains values not in A.
               Extra value at end.
            """

            A = [1, 2, 3, 4]
            A.sort()
            B = [1, 2, 3, 4, 5]
            B.sort()
            (X, Y) = check(A, B)
            expected_X = []
            expected_Y = [5]
            msg = ('check(%s, %s) should return (%s, %s), but got (%s, %s)'
                   % (str(A), str(B), str(expected_X), str(expected_Y), str(X), str(Y)))
            self.assertTrue(X == expected_X and Y == expected_Y, msg)

        def test_only_AB_extra(self):
            """Test case where both A and B have values not in the other."""

            A = [2, 3, 4, 5, 6]
            A.sort()
            B = [1, 2, 3, 4, 5]
            B.sort()
            (X, Y) = check(A, B)
            expected_X = [6]
            expected_Y = [1]
            msg = ('check(%s, %s) should return (%s, %s), but got (%s, %s)'
                   % (str(A), str(B), str(expected_X), str(expected_Y), str(X), str(Y)))
            self.assertTrue(X == expected_X and Y == expected_Y, msg)

        def test_given(self):
            """Test for both input lists empty."""

            A = [1,2,9,3,4,5]
            A.sort()
            B = [1,2,3,4,5]
            B.sort()
            (X, Y) = check(A, B)
            expected_X = [9]
            expected_Y = []
            msg = ('check(%s, %s) should return (%s, %s), but got (%s, %s)'
                   % (str(A), str(B), str(expected_X), str(expected_Y), str(X), str(Y)))
            self.assertTrue(X == expected_X and Y == expected_Y, msg)


unittest.main()
