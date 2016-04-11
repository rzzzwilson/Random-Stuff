# File: MatrixFind.py
# Author: Keith Schwarz (htiek@cs.stanford.edu)
#
# An algorithm for finding a specific value in a specially-formatted matrix of
# values.
#
# The algorithm takes as input a matrix of values where each row and each
# column are in sorted order, along with a value to locate in that array, then
# returns whether that element exists in the matrix.  For example, given the
# matrix
#
#       1 2 2 2 3 4
#       1 2 3 3 4 5
#       3 4 4 4 4 6
#       4 5 6 7 8 9
#
# along with the number 7, the algorithm would output YES, but if given the
# number 0 the algorithm would output NO.
#
# One approach for solving this problem would be a simple exhaustive search of
# the matrix to find the value.  If the matrix dimensions are m x n, this
# algorithm will take time O(mn) in the worst-case, which is indeed linear in
# the size of the matrix but takes no advantage of the sorted structure we are
# guaranteed to have in the matrix.  Our goal will be to find a much faster
# algorithm for solving the same problem.
#
# One approach that might be useful for solving the problem is to try to keep
# deleting rows or columns out of the array in a way that reduces the problem
# size without ever deleting the value (should it exist).  For example, suppose
# that we iteratively start deleting rows and columns from the matrix that we
# know do not contain the value.  We can repeat this until either we've reduced
# the matrix down to nothingness, in which case we know that the element is not
# present, or until we find the value.  If the matrix is m x n, then this would
# require only O(m + n) steps, which is much faster than the O(mn) approach
# outlined above.
# 
# In order to realize this as a concrete algorithm, we'll need to find a way to
# determine which rows or columns to drop.  One particularly elegant way to do
# this is to look at the very last element of the first row of the matrix.
# Consider how it might relate to the value we're looking for.  If it's equal
# to the value in question, we're done and can just hand back that we've found
# the entry we want.  If it's greater than the value in question, since each
# column is in sorted order, we know that no element of the last column could
# possibly be equal to the number we want to search for, and so we can discard
# the last column of the matrix.  Finally, if it's less than the value in
# question, then we know that since each row is in sorted order, none of the
# values in the first row can equal the element in question, since they're no
# bigger than the last element of that row, which is in turn smaller than the
# element in question.  This gives a very straightforward algorithm for finding
# the element - we keep looking at the last element of the first row, then
# decide whether to discard the last row or the last column.  As mentioned
# above, this will run in O(m + n) time.  (Thanks to Prof. David Gries of
# Cornell University for this solution).

# Function: matrixFind(matrix, value)
# Usage: result = matrixFind(myMatrix, 137)
# -----------------------------------------------------------------------------
# Searches the given matrix, which must have its rows and columns in sorted
# order, for the given value, returning whether or not that value was found.

def matrixFind(matrix, value):
    # Get the matrix dimensions.  If the matrix is empty, return that we could
    # not find the value in question.
    m = len(matrix)
    if m == 0:
        return False

    n = len(matrix[0])
    if n == 0:
        return False

    # Maintain the index (i, j) of the last element of the first row.  We will
    # be using this index to keep track of the next location to look.
    i = 0
    j = n - 1

    # Keep comparing the last element of the first row of the matrix to the
    # element in question, paring down a row or column as appropriate.  If we
    # ever walk off the matrix, we know that the element must not exist.
    while i < m and j >= 0:

        # If we found the value, great!  We're done.
        if matrix[i][j] == value:
            return True
        # Otherwise, if the value here is smaller than the value we're looking
        # for, we can exclude this row from consideration.
        elif matrix[i][j] < value:
            i = i + 1
        # Otherwise, the value here is greater, so we can exclude this column
        # from consideration.
        else:
            j = j - 1

    return False
