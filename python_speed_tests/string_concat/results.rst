The results file.  Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah.
Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah.
Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah.
Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah.
Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah.
Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah.
Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah.
Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah. Blah.

python2 running test.py
=======================

Using Python 2.7.12 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial
For 50000000 concatenations:

+-------------+-------+
| Method      | Time  |
+=============+=======+
| naive | 10.31s |
+-------------+-------+
| join | 12.72s |
+-------------+-------+
| stringio | 19.83s |
+-------------+-------+
| comprehension | 9.74s |
+-------------+-------+

.. image:: test.2.log.png

python3 running test.py
=======================

Using Python 3.5.2 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial
For 50000000 concatenations:

+-------------+-------+
| Method      | Time  |
+=============+=======+
| naive | 13.44s |
+-------------+-------+
| join | 15.61s |
+-------------+-------+
| stringio | 16.23s |
+-------------+-------+
| comprehension | 12.47s |
+-------------+-------+

.. image:: test.3.log.png

python2 running test2.py
=======================

Using Python 2.7.12 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial
For 500000 concatenations:

+-------------+-------+
| Method      | Time  |
+=============+=======+
| naive | 134.59s |
+-------------+-------+
| join | 0.22s |
+-------------+-------+
| stringio | 0.25s |
+-------------+-------+

.. image:: test2.2.log.png

python3 running test2.py
=======================

Using Python 3.5.2 on Linux-4.4.0-38-generic-x86_64-with-Ubuntu-16.04-xenial
For 500000 concatenations:

+-------------+-------+
| Method      | Time  |
+=============+=======+
| naive | 127.60s |
+-------------+-------+
| join | 0.19s |
+-------------+-------+
| stringio | 0.20s |
+-------------+-------+

.. image:: test2.3.log.png

