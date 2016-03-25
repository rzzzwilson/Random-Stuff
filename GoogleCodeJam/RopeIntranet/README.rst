This is the puzzle **Rope Intranet** from the Google Code Jam
`practice page <https://code.google.com/codejam/contest/619102/dashboard#s=p0>`_.

The files:

::

    A-small-practice.in

The small practice input file from the Code Jam page.

::

    A-large-practice.in

The large practice input file from the Code Jam page.

::

    rope_intranet.py

Hopefully a solution to the problem.

The problem, from the web page
==============================

A company is located in two very tall buildings. The company intranet connecting
the buildings consists of many wires, each connecting a window on the first
building to a window on the second building.

You are looking at those buildings from the side, so that one of the buildings
is to the left and one is to the right. The windows on the left building are
seen as points on its right wall, and the windows on the right building are seen
as points on its left wall. Wires are straight segments connecting a window on
the left building to a window on the right building.

.. image:: rope_intranet.png

You've noticed that no two wires share an endpoint (in other words, there's at
most one wire going out of each window). However, from your viewpoint, some of
the wires intersect midway. You've also noticed that exactly two wires meet at
each intersection point.

On the above picture, the intersection points are the black circles, while the
windows are the white circles.

How many intersection points do you see?

Input
-----

The first line of the input gives the number of test cases, T. T test cases
follow. Each case begins with a line containing an integer N, denoting the
number of wires you see.

The next N lines each describe one wire with two integers Ai and Bi. These describe the windows that this wire connects: Ai is the height of the window on the left building, and Bi is the height of the window on the right building.

Output
------

For each test case, output one line containing "Case #x: y", where x is the
case number (starting from 1) and y is the number of intersection points you
see.

Limits
------

1 <= T <= 15.
1 <= Ai <= 104.
1 <= Bi <= 104.

Within each test case, all Ai are different.

Within each test case, all Bi are different.

No three wires intersect at the same point.
