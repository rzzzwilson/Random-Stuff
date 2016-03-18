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

It seems to me that a simple 'hill-climbing' approach might work.  We need a stack:

0. Set current position to (0, 0), the top-left cell (must be the lowest value cell)
1. If the current position is on the matrix, goto 4
2. If the stack is empty, return False
3. Pop the stack to current, goto 1
4. If M(current) == required, return T
5. Push current (x+=1), current <- (X,Y=1), goto 1

How does it perform?
--------------------

From a test suite of ONE, matrix_find.py works!

My solution is about the same size as Keith's, but because it uses an explicit stack
it takes longer: for a million executions, mf.py takes 6.2s versus 149.7s for matrix_find.py.

I'm sure I could make this faster, possibly by using the python stack rather than the
explicit stack, but I don't care.  It works and it's a bit shorter than I thought it
would be.  Intellectual itch scratched!

More
----

Of course I couldn't leave it at that, as I thought of a better approach.  The python
stack approach is in matrix_find2.py.  Unfortunately, the algorithm is broken as some
test cases show.  Do 'make test' to run the test cases.

Also note that the solutions before the brute-force solution matrix_find4.py are
**broken**!.  The brute-force solution must work, of course, but it's twice as slow
as the original solution.
