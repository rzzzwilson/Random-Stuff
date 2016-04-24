What is this?
=============

This directory contains code on solving the "Matrix Find" problem which I first
ran across at `Keith Schwarz's page <http://www.keithschwarz.com/interesting/code/?dir=matrix-find>`_.

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
**broken**!.  Yay for testing!!  The brute-force solution must work, of course, but
it's twice as slow as Keith's solution.

A solution?
===========

Another approach (with more thought!) is:

As before, start at the top-left element and proceed down the diagonal until we either:

1. Find the value we want, the result is FOUND,
2. We run off the bottom or right of the matrix, see below, or
3. We find a value greater than the required value.

If we find a greater value than required, we step back to the previous diagonal element.
If we *can't* do that without stepping off the matrix, the result is NOT FOUND.
The element that is current defines four sub-matrices:

1. The sub-matrix defined by the (0,0) and current element corners.  This sub-matrix cannot
   contain the required value because the maximum values must occur in the right or bottom
   edges, and they are all less than the required value.
2. All elements to the right and below the element containing the value greater than the
   required value.  Since the top-left element of that sub-matrix is greater than required,
   *all* elements must be greater than required.
3. The sub-matrix above and to the right of the current element may contain the required value.
4. The sub-matrix below and to the left of the current element may contain the required value.

The sub-matrices defined in 3 and 4 above are searched in the same way as the original matrix.

If we run off the bottom of the original matrix, the last element scanned on the diagonal
defines a sub-matrix above and to the right of the last element.  Scan this sub-matrix the
same way as the original.

Similarly, if the diagonal scan runs off the right side of the original matrix, the last
element scanned defines a sub-matrix to the left and below the last scanned element.  Scan
this sub-matrix the same way as the original matrix.

To implement this we define a function that searches a sub-matrix of an original matrix.  We
must define this function in such a way that we can start with the search of the original
matrix.  Something like:

::

    matrix_find(matrix, start_x, start_y, max_x, max_y, value)

where the **start_x** and **start_y** coordinates define the top-left element in the matrix
that we start searching from, and the **max_x** and **max_y** values define the coordinates
of the bottom-right corner of the sub-matrix (inclusive).

The special case when we find a value greater than the required value at the extreme right-
and/or bottom-most cell in the sub-matrix is still handled by the above algorithm, but this
just results in an inefficient linear search.  Optionally, this could be handled as a special
case and just search linearly.  Note that this won't change the "big O" time.

We implement this in **matrix_find5.py**.

Testing
-------

The file **test_matrix_find.py** tests each implementation one after the other.  The file
**time_matrix_find.py** times execution of a simple test case for a large number of times
for each implementation.

Keith's solution is tested and timed in **test_mf.py** abd **time_mf.py** respectively.

After reading Keith's solution
==============================

I have now (20 Mar 2016) read the source of Keith's **mf.py**.  The idea there is very simple
and I kick myself for not thinking of it.  But even that still doesn't use all the information
from the matrix.

First, the **mf.py** explanation (note I still haven't read the *code* of mf.py) talks about
"deleting" rows and columns.  I think that's a little misleading.  What you should do is
have a "view" onto the original matrix and the algorithm incrementally constricts the view by
removing areas where the required value cannot be.

A more general algorithm might be:

::

    Given a view:
    1. scan the top row from the left and remove columns starting with a value > required
    2. scan the bottom row from the right and remove columns ending with a value < required
    3. scan the left column from the top and remove rows starting with a value > required
    4. scan the right column from the bottom and remove rows ending with a value < required

Of course, if we find the required value during a scan we immediately terminate.

It is not clear if there is anything to be gained by scanning in one direction or the other.

Between each step modify the view limits.  That is, don't do all 4 steps on the *original* view
and then update the view limits.

This algorithm is implemented in *matrix_find6.py* (recursive) and *matrix_find7.py*
(iterative).

Testing shows that the iterative version is slightly faster than the recursive version,
of course.  But this is still half the speed of *mf.py*.  I'll have to read the code to
see what is happening in *mf.py*.


Summary
=======

TBD
