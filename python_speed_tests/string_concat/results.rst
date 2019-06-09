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

make_table.py: test.py.python.out

.. image:: test.py.python.log.png

python running test.py (GC OFF)
-------------------------------

make_table.py: test.py.python-g.out

.. image:: test.py.python-g.log.png

python running test2.py (GC ON)
-------------------------------

make_table.py: test2.py.python.out

.. image:: test2.py.python.log.png

python running test2.py (GC OFF)
-------------------------------

make_table.py: test2.py.python-g.out

.. image:: test2.py.python-g.log.png

python3 running test.py (GC ON)
-------------------------------

make_table.py: test.py.python3.out

.. image:: test.py.python3.log.png

python3 running test.py (GC OFF)
-------------------------------

make_table.py: test.py.python3-g.out

.. image:: test.py.python3-g.log.png

python3 running test2.py (GC ON)
-------------------------------

make_table.py: test2.py.python3.out

.. image:: test2.py.python3.log.png

python3 running test2.py (GC OFF)
-------------------------------

make_table.py: test2.py.python3-g.out

.. image:: test2.py.python3-g.log.png

