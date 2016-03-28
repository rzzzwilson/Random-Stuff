#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test the solution(s) to the BigCitySkyline problem.
"""

import unittest
import big_city_skyline


class TestBigCitySkyline(unittest.TestCase):

    def test_small_in(self):
        filename = 'small.in'
        expected = 51
        result = big_city_skyline.main(filename)
        msg = ("Expected file '%s' to give result %d, got %d instead"
               % (filename, expected, result))
        self.assertTrue(result == expected, msg)

    def test_test1_in(self):
        filename = 'test1.in'
        expected = 36
        result = big_city_skyline.main(filename)
        msg = ("Expected file '%s' to give result %d, got %d instead"
               % (filename, expected, result))
        self.assertTrue(result == expected, msg)

    def test_test2_in(self):
        filename = 'test2.in'
        expected = 54
        result = big_city_skyline.main(filename)
        msg = ("Expected file '%s' to give result %d, got %d instead"
               % (filename, expected, result))
        self.assertTrue(result == expected, msg)

    def test_test3_in(self):
        filename = 'test3.in'
        expected = 30
        result = big_city_skyline.main(filename)
        msg = ("Expected file '%s' to give result %d, got %d instead"
               % (filename, expected, result))
        self.assertTrue(result == expected, msg)

################################################################################

if __name__ == '__main__':
    suite = unittest.makeSuite(TestBigCitySkyline, 'test')
    runner = unittest.TextTestRunner()
    runner.run(suite)


