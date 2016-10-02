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
| naive         | 10.91s |
+---------------+--------+
| join          | 12.41s |
+---------------+--------+
| stringio      | 22.09s |
+---------------+--------+
| comprehension | 11.33s |
+---------------+--------+

.. image:: test.py.python.log.png

python running test.py (GC OFF)
-------------------------------

| Using Python 2.7.12 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial
| For 50000000 concatenations, GC is OFF:

+---------------+--------+
| Method        | Time   |
+===============+========+
| naive         | 11.21s |
+---------------+--------+
| join          | 12.49s |
+---------------+--------+
| stringio      | 21.71s |
+---------------+--------+
| comprehension | 10.47s |
+---------------+--------+

.. image:: test.py.python-g.log.png

python running test2.py (GC ON)
-------------------------------

| Using Python 2.7.12 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial
| For 500000 concatenations, GC is ON:

+---------------+--------+
| Method        | Time   |
+===============+========+
| naive         | 23.15s |
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
| naive         | 37.25s |
+---------------+--------+
| join          |  0.30s |
+---------------+--------+
| stringio      |  0.42s |
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
| join          | 17.80s |
+---------------+--------+
| stringio      | 15.10s |
+---------------+--------+
| comprehension | 11.53s |
+---------------+--------+

.. image:: test.py.python3.log.png

python3 running test.py (GC OFF)
-------------------------------

| Using Python 3.5.2 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial
| For 50000000 concatenations, GC is OFF:

+---------------+--------+
| Method        | Time   |
+===============+========+
| naive         | 13.25s |
+---------------+--------+
| join          | 19.00s |
+---------------+--------+
| stringio      | 15.99s |
+---------------+--------+
| comprehension | 12.54s |
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
| stringio      |  0.30s |
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

