Test Results
============

This shows the time taken for each test and the memory used for both python2 and
python3.

Each test shows the timings in a table, followed by a graph showing memory
usage during the test.  The graph shows all the tests in the order as shown
in the timing table.  For instance, in the python2/test.py results immediately
below, we see four major peaks representing the usage for the naive, join,
stringio and comprehension methods respectively.

The *test.py* code tests each concatenation method in a direct manner.  Python
does have some optimizations it applies if it can recognize that string
concatenation is occurring.

The *test2.py* code is designed to disable the optimizations python performs on
string contenation.  The timing figures show expected results, but the memory
usage graphs show odd behaviour.  Still working on that!

python2 running test.py
-----------------------

| Using Python 2.7.12 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial
| For 50000000 concatenations:

+---------------+--------+
| Method        | Time   |
+===============+========+
| naive         | 11.09s |
+---------------+--------+
| join          | 12.98s |
+---------------+--------+
| stringio      | 22.65s |
+---------------+--------+
| comprehension | 10.78s |
+---------------+--------+

.. image:: test.2.log.png

python3 running test.py
-----------------------

| Using Python 3.5.2 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial
| For 50000000 concatenations:

+---------------+--------+
| Method        | Time   |
+===============+========+
| naive         | 14.78s |
+---------------+--------+
| join          | 15.81s |
+---------------+--------+
| stringio      | 16.21s |
+---------------+--------+
| comprehension | 12.38s |
+---------------+--------+

.. image:: test.3.log.png

python2 running test2.py
------------------------

| Using Python 2.7.12 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial
| For 500000 concatenations:

+---------------+--------+
| Method        | Time   |
+===============+========+
| naive         | 35.76s |
+---------------+--------+
| join          |  0.17s |
+---------------+--------+
| stringio      |  0.24s |
+---------------+--------+

.. image:: test2.2.log.png

python3 running test2.py
------------------------

| Using Python 3.5.2 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial
| For 500000 concatenations:

+---------------+--------+
| Method        | Time   |
+===============+========+
| naive         | 25.67s |
+---------------+--------+
| join          |  0.20s |
+---------------+--------+
| stringio      |  0.20s |
+---------------+--------+

.. image:: test2.3.log.png

