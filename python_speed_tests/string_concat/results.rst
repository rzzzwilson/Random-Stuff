Test Results
============

This shows the tie taken for each test and the memory used.  Both python2 and
python3 were used.

Each test shows the timings in a table, followed by a graph showing memory
usage during the test.  The graph shows all the tests in the order as shown
in the timing table.  For instance, in the python2/test.py results immediately
below, we see four major peaks representing the usage for the naive, join,
stringio and comprehension methods respectively.

The *test2.py* code is designed to disable the optimizations python performs on
string contenation.  The timing figures show expected results, but the memory
usage graphs show odd behaviour.  Still working on that!

python2 running test.py
-----------------------

| Using Python 2.7.12 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial
| For 50000000 concatenations:

Using Python 2.7.12 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial

For 50000000 concatenations:


+---------------+--------+
| Method        | Time   |
+===============+========+
| naive         | 10.78s |
+---------------+--------+
| join          | 11.56s |
+---------------+--------+
| stringio      | 20.93s |
+---------------+--------+
| comprehension | 9.75s |
+---------------+--------+

.. image:: test.2.log.png

python3 running test.py
-----------------------

| Using Python 3.5.2 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial
| For 50000000 concatenations:

Using Python 3.5.2 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial

For 50000000 concatenations:


+---------------+--------+
| Method        | Time   |
+===============+========+
| naive         | 13.80s |
+---------------+--------+
| join          | 16.16s |
+---------------+--------+
| stringio      | 16.74s |
+---------------+--------+
| comprehension | 12.69s |
+---------------+--------+

.. image:: test.3.log.png

python2 running test2.py
------------------------

| Using Python 2.7.12 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial
| For 500000 concatenations:

Using Python 2.7.12 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial

For 500000 concatenations:


+---------------+--------+
| Method        | Time   |
+===============+========+
| naive         | 131.75s |
+---------------+--------+
| join          | 0.17s |
+---------------+--------+
| stringio      | 0.23s |
+---------------+--------+

.. image:: test2.2.log.png

python3 running test2.py
------------------------

| Using Python 3.5.2 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial
| For 500000 concatenations:

Using Python 3.5.2 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial

For 500000 concatenations:


+---------------+--------+
| Method        | Time   |
+===============+========+
| naive         | 139.68s |
+---------------+--------+
| join          | 0.26s |
+---------------+--------+
| stringio      | 0.27s |
+---------------+--------+

.. image:: test2.3.log.png

