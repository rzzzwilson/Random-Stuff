Test Results
============

This shows the time taken for each test and the memory used for both python2 and
python3, with the garbage collector running and disabled.

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

python running test.py (GC ON)
-------------------------------

| Using Python 2.7.12 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial
| For 50000000 concatenations, GC is ON:

+---------------+--------+
| Method        | Time   |
+===============+========+
| naive         | 11.12s |
+---------------+--------+
| join          | 11.83s |
+---------------+--------+
| stringio      | 20.07s |
+---------------+--------+
| comprehension | 10.38s |
+---------------+--------+

.. image:: test.py.python.log.png

python running test.py (GC OFF)
-------------------------------

| Using Python 2.7.12 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial
| For 50000000 concatenations, GC is OFF:

+---------------+--------+
| Method        | Time   |
+===============+========+
| naive         | 11.50s |
+---------------+--------+
| join          | 12.44s |
+---------------+--------+
| stringio      | 19.29s |
+---------------+--------+
| comprehension | 10.19s |
+---------------+--------+

.. image:: test.py.python-g.log.png

python running test2.py (GC ON)
-------------------------------

| Using Python 2.7.12 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial
| For 500000 concatenations, GC is ON:

+---------------+--------+
| Method        | Time   |
+===============+========+
| naive         | 30.18s |
+---------------+--------+
| join          |  0.15s |
+---------------+--------+
| stringio      |  0.17s |
+---------------+--------+
| comprehension |  0.09s |
+---------------+--------+

.. image:: test2.py.python.log.png

python running test2.py (GC OFF)
-------------------------------

| Using Python 2.7.12 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial
| For 500000 concatenations, GC is OFF:

+---------------+--------+
| Method        | Time   |
+===============+========+
| naive         | 47.83s |
+---------------+--------+
| join          |  0.15s |
+---------------+--------+
| stringio      |  0.21s |
+---------------+--------+
| comprehension |  0.09s |
+---------------+--------+

.. image:: test2.py.python-g.log.png

python3 running test.py (GC ON)
-------------------------------

| Using Python 3.5.2 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial
| For 50000000 concatenations, GC is ON:

+---------------+--------+
| Method        | Time   |
+===============+========+
| naive         | 14.26s |
+---------------+--------+
| join          | 19.23s |
+---------------+--------+
| stringio      | 16.78s |
+---------------+--------+
| comprehension | 13.93s |
+---------------+--------+

.. image:: test.py.python3.log.png

python3 running test.py (GC OFF)
-------------------------------

| Using Python 3.5.2 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial
| For 50000000 concatenations, GC is OFF:

+---------------+--------+
| Method        | Time   |
+===============+========+
| naive         | 14.34s |
+---------------+--------+
| join          | 19.53s |
+---------------+--------+
| stringio      | 16.77s |
+---------------+--------+
| comprehension | 13.48s |
+---------------+--------+

.. image:: test.py.python3-g.log.png

python3 running test2.py (GC ON)
-------------------------------

| Using Python 3.5.2 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial
| For 500000 concatenations, GC is ON:

+---------------+--------+
| Method        | Time   |
+===============+========+
| naive         | 44.88s |
+---------------+--------+
| join          |  0.17s |
+---------------+--------+
| stringio      |  0.17s |
+---------------+--------+
| comprehension |  0.14s |
+---------------+--------+

.. image:: test2.py.python3.log.png

python3 running test2.py (GC OFF)
-------------------------------

| Using Python 3.5.2 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial
| For 500000 concatenations, GC is OFF:

+---------------+--------+
| Method        | Time   |
+===============+========+
| naive         | 33.53s |
+---------------+--------+
| join          |  0.17s |
+---------------+--------+
| stringio      |  0.17s |
+---------------+--------+
| comprehension |  0.14s |
+---------------+--------+

.. image:: test2.py.python3-g.log.png

