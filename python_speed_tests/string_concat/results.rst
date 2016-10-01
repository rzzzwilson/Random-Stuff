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
| naive         |  9.96s |
+---------------+--------+
| join          | 12.52s |
+---------------+--------+
| stringio      | 23.21s |
+---------------+--------+
| comprehension | 10.73s |
+---------------+--------+

.. image:: test.py.python.log.png

python running test.py (GC OFF)
-------------------------------

| Using Python 2.7.12 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial
| For 50000000 concatenations, GC is OFF:

+---------------+--------+
| Method        | Time   |
+===============+========+
| naive         | 10.70s |
+---------------+--------+
| join          | 12.56s |
+---------------+--------+
| stringio      | 20.89s |
+---------------+--------+
| comprehension | 10.42s |
+---------------+--------+

.. image:: test.py.python-g.log.png

python running test2.py (GC ON)
-------------------------------

| Using Python 2.7.12 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial
| For 500000 concatenations, GC is ON:

+---------------+--------+
| Method        | Time   |
+===============+========+
| naive         | 32.15s |
+---------------+--------+
| join          |  0.31s |
+---------------+--------+
| stringio      |  0.42s |
+---------------+--------+
| comprehension |  0.12s |
+---------------+--------+

.. image:: test2.py.python.log.png

python running test2.py (GC OFF)
-------------------------------

| Using Python 2.7.12 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial
| For 500000 concatenations, GC is OFF:

+---------------+--------+
| Method        | Time   |
+===============+========+
| naive         | 21.74s |
+---------------+--------+
| join          |  0.30s |
+---------------+--------+
| stringio      |  0.43s |
+---------------+--------+
| comprehension |  0.12s |
+---------------+--------+

.. image:: test2.py.python-g.log.png

python3 running test.py (GC ON)
-------------------------------

| Using Python 3.5.2 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial
| For 50000000 concatenations, GC is ON:

+---------------+--------+
| Method        | Time   |
+===============+========+
| naive         | 13.27s |
+---------------+--------+
| join          | 15.82s |
+---------------+--------+
| stringio      | 16.21s |
+---------------+--------+
| comprehension | 12.74s |
+---------------+--------+

.. image:: test.py.python3.log.png

python3 running test.py (GC OFF)
-------------------------------

| Using Python 3.5.2 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial
| For 50000000 concatenations, GC is OFF:

+---------------+--------+
| Method        | Time   |
+===============+========+
| naive         | 14.26s |
+---------------+--------+
| join          | 15.83s |
+---------------+--------+
| stringio      | 16.18s |
+---------------+--------+
| comprehension | 13.28s |
+---------------+--------+

.. image:: test.py.python3-g.log.png

python3 running test2.py (GC ON)
-------------------------------

| Using Python 3.5.2 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial
| For 500000 concatenations, GC is ON:

+---------------+--------+
| Method        | Time   |
+===============+========+
| naive         |  0.26s |
+---------------+--------+
| join          |  0.29s |
+---------------+--------+
| stringio      |  0.29s |
+---------------+--------+
| comprehension |  0.10s |
+---------------+--------+

.. image:: test2.py.python3.log.png

python3 running test2.py (GC OFF)
-------------------------------

| Using Python 3.5.2 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial
| For 500000 concatenations, GC is OFF:

+---------------+--------+
| Method        | Time   |
+===============+========+
| naive         |  0.27s |
+---------------+--------+
| join          |  0.29s |
+---------------+--------+
| stringio      |  0.30s |
+---------------+--------+
| comprehension |  0.10s |
+---------------+--------+

.. image:: test2.py.python3-g.log.png

