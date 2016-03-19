#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test the solution(s) to the MatrixFind problem.
"""

import unittest


class TestMatrixFind(unittest.TestCase):

    def test_simple_find(self):
        #          ---> Y
        matrix = [[1, 1, 3, 4],	# .
                  [2, 2, 4, 5],	# .
                  [2, 3, 4, 6],	# V
                  [2, 3, 4, 7],	# 
                  [3, 4, 4, 8],	# X
                  [4, 5, 6, 9]]

        msg = '%s: Expected to find 7 in the matrix, did not?' % ModuleName
        result = Module.matrix_find(matrix, 7)
        self.assertTrue(result, msg)

    def test_simple_nofind(self):
        #          ---> Y
        matrix = [[1, 1, 3, 4],	# .
                  [2, 2, 4, 5],	# .
                  [2, 3, 4, 6],	# V
                  [2, 3, 4, 7],	# 
                  [3, 4, 4, 8],	# X
                  [4, 5, 6, 9]]

        msg = '%s: Value 10 is not in the matrix, but found it?' % ModuleName
        result = Module.matrix_find(matrix, 10)
        self.assertFalse(result, msg)

    def test_simple_nofind2(self):
        #          ---> Y
        matrix = [[1, 1, 3, 4],	# .
                  [2, 2, 4, 5],	# .
                  [2, 3, 4, 6],	# V
                  [2, 3, 4, 7],	# 
                  [3, 4, 4, 8],	# X
                  [4, 5, 6, 9]]

        msg = '%s: Value 0 is not in the matrix, but found it?' % ModuleName
        result = Module.matrix_find(matrix, 0)
        self.assertFalse(result, msg)

    def test_simple_nofind3(self):
        #          ---> Y
        matrix = [[0, 0, 3, 4],	# .
                  [2, 2, 4, 5],	# .
                  [2, 3, 4, 6],	# V
                  [2, 3, 4, 7],	# 
                  [3, 4, 4, 8],	# X
                  [4, 5, 6, 9]]

        msg = '%s: Value 1 is not in the matrix, but found it?' % ModuleName
        result = Module.matrix_find(matrix, 1)
        self.assertFalse(result, msg)

    def test_notsimple_find(self):
        #          ---> Y
        matrix = [[0, 0, 0, 0, 1, 1, 1, 2],	# .
                  [0, 0, 1, 1, 2, 3, 7, 8],	# .
                  [1, 1, 2, 3, 4, 6, 8, 8],	# .
                  [2, 3, 3, 6, 6, 6, 8, 9],	# v
                  [2, 3, 3, 8, 8, 8, 8, 9],	# 
                  [2, 3, 4, 8, 8, 8, 8, 9],	# 
                  [2, 3, 5, 8, 8, 8, 9, 10],	# X
                  [2, 3, 6, 8, 9, 9, 9, 10]]

        m_str = str(matrix)
        msg = '%s: Value 7 is in the matrix, but not found?' % ModuleName
        result = Module.matrix_find(matrix, 7)
        self.assertTrue(result, msg)

    def test_notsimple_find2(self):
        #          ---> Y
        matrix = [[0, 0, 0, 0, 1, 1, 1, 2],	# .
                  [0, 0, 1, 1, 2, 3, 7, 8],	# .
                  [1, 1, 2, 3, 4, 6, 8, 8],	# .
                  [2, 3, 3, 6, 6, 6, 8, 9],	# v
                  [2, 3, 3, 8, 8, 8, 8, 9],	# 
                  [2, 3, 4, 8, 8, 8, 8, 9],	# 
                  [2, 3, 5, 8, 8, 8, 9, 10],	# X
                  [2, 3, 6, 8, 9, 9, 9, 10]]

        msg = '%s: Value 5 is in the matrix, but not found?' % ModuleName
        result = Module.matrix_find(matrix, 5)
        self.assertTrue(result, msg)

################################################################################

if __name__ == '__main__':
    global Module, ModuleName

    suite = unittest.makeSuite(TestMatrixFind, 'test')
    runner = unittest.TextTestRunner()

    import matrix_find
    Module = matrix_find
    ModuleName = 'matrix_find'
    print('\n%s %s' % (ModuleName, '.oOo. '*14))
    runner.run(suite)

    import matrix_find2
    Module = matrix_find2
    ModuleName = 'matrix_find2'
    print('\n%s %s' % (ModuleName, '.oOo. '*14))
    runner.run(suite)

    import matrix_find3
    Module = matrix_find3
    ModuleName = 'matrix_find3'
    print('\n%s %s' % (ModuleName, '.oOo. '*14))
    runner.run(suite)

    import matrix_find4
    Module = matrix_find4
    ModuleName = 'matrix_find4'
    print('\n%s %s' % (ModuleName, '.oOo. '*14))
    runner.run(suite)

    import matrix_find5
    Module = matrix_find5
    ModuleName = 'matrix_find5'
    print('\n%s %s' % (ModuleName, '.oOo. '*14))
    runner.run(suite)
