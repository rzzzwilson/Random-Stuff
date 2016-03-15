What is this?
=============

This directory contains code on solving the "Matrix Find" problem which I first
ran across at `Keith Schwarz's page<http://www.keithschwarz.com/interesting/code/?dir=matrix-find>`_.

Matrix Find
-----------

As stated on Keith's page, the Matrix Find problem is to find:

::

    An algorithm for finding a specific value in a specially-formatted matrix of
    values.
    
    The algorithm takes as input a matrix of values where each row and each
    column are in sorted order, along with a value to locate in that array, then
    returns whether that element exists in the matrix.  For example, given the
    matrix
    
        1 2 2 2 3 4
        1 2 3 3 4 5
        3 4 4 4 4 6
        4 5 6 7 8 9
   
    along with the number 7, the algorithm would output YES, but if given the
    number 0 the algorithm would output NO.

The challenge for me is to create my own algorithm and compare the time/space/complexity
attributes of my solution against Keith's solution, which I haven't looked at yet.

Basic idea
----------

It seems to me that a simple 'hill-climbing' approach might work.  We need a stack.

0. Set the current position to the top-left cell (must be the lowest value cell)
1. Note the value of the current cell
2. If current value is required, return True
3. Compare the current value with the values to the right, lower-right and lower cells.
4. If any of those values equals the required value, return True
5. If right-lower cell has a value less than the required, push current location to the stack and use the new cell as current
6. Move current cell to the right
7. If still within the row, goto step 1
8. If the stack is not empty, pop stack, increment X coord and goto step 1
9. Return False
