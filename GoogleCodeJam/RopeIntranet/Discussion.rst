Rope Intranet
=============

This problem is quite simply stated.  The first question we have is "how do we
solve this?".

At first glance, the obvious approach is to take one rope and figure out how 
many intersections it has with all the other ropes.  Now remove that rope from
further consideration and choose one rope from the remaining set.  Calculate
the number of intersections this rope has with the remaining ropes.  Repeat
until we are finished.

So, we choose one rope and consider how many intersecttions it has with the
other remaining ropes.  We will do that one-by one, so the question now is
how do we determine if two ropes intersect or not?

Suppose we have two ropes, **i** and **j**.  Following the naming convention
in the problem statement, the endpoints of the **i** rope are **Ai** and
**Bi**.  For the **j** rope, they are **Aj** and **Bj**.  After some fiddling
with simple pictures, we convince ourselves that the two ropes have an
intersection if any of the following conditions are true:

::

    (Ai < Bj) and (Bi > Aj)                     # relation 1
    (Ai > Aj) and (Bi < Bj)                     # relation 2
    (Ai < Aj) and (Bi > Bj)                     # relation 3

We think about this by drawing the two walls and then line **i** with some
slope to it.  We assume there is an intersection with **j** and we draw a dot
on **i** signifying that intersection.  Consider all the possible states
of **Ai**, **Bi**, **Aj** and **Bj**.

We notice that relations 2 and 3 are very similar, but we just go ahead and
implement the above as **rope_intranet.py**.  Testing shows the program is
wrong: case 2 has rope_set=[(5, 3), (6, 4)] which has an intersection but the
program says 0.  Edit: note that I'm wrong here, the case is correct.  No
matter, as the next idea is better.

We appear to be missing a case!?  Edit: also note that there is another bug in
count_one_intersections() (despite the bad grammar in the name) - we aren't
returning the **sum** of all intersections, we mistakenly return the first
1 value!

After more fiddling with little drawings we hit on the idea that it's really
**not about where the points are relative to each other**.  If we consider
all relations of two points in building A, two points in building B and the two
possile ways to connect those four dots with two lines, we realize that the 
important thing is the **sense of connection** of those four points.

If we define the relationship between Ai and Aj as either **up** (Ai < Aj) or
**down** (Ai > Aj) then we always have an intersection if the relationship
between Aj and Bj is the **opposite** to that between Ai and Bi.  We define
**up** as True and **down** as False and implement this idea in
rope_intranet2.py.

After stepping through the output including all the debug prints, we convince
ourselves that the small test case is correct.  Let's try to remove all the
debug prints and submit the small case output to Google.  We capture the output
in the file rope_intranet2.py.small.  And, it's rejected as the first case must
be numbered "1", not "0".  I didn't read the problem statement closely enough.

Edit rope_intranet2.py and try again.  Now it's correct!

Before we get a swelled head, try the large input file.  Save the output in
rope_intranet2.py.large.  That is also correct!  Plus it runs in about half
a second.

We finish at this point.

In an actual competition the test data may be much larger and the python
solution could be too slow.  How might we speed up the solution?

One possible way may be to prune the **other** list of ropes in the
count_one_intersection() function.  If we sort the list of ropes before we
start, we could possibly get to a point where we know the remining **other**
ropes could not intersect with the test rope, and we would return at that
point.

After that we get into fiddly stuff, like we don't need to create variables
**A_up** and **B_up** in count_one_intersection(), but just return the
expression:

::

    # ie, not this
    A_up = Ai < Aj
    B_up = Bi < Bj
    result += (A_up ^ B_up)

::

    # but this
    result += int((Ai < Aj) ^ (Bi < Bj))

We can't test this with the Google practice data.  Well, we can't test for
how much **speedup** we get as the practice sets are too small.  We could
generate our own large datasets and test them for speedup, forgetting for
the moment about correctness.  Exercise for the student!
