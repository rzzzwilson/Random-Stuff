String Concatenation
====================

If you read the Python programming blogs or google for
"python string concatenation" you find statements that the naive

::

    a += b

method of concatenating strings is horribly slow and uses too much memory.

Well, it's not that simple with newer Pythons. The code here tests various
methods of concatenating strings:

=============  =====================================
Method         Description
=============  =====================================
naive          the old 'a += b' method
array          using the array module .join() method
join           using the list object .join() method
stringio       concatenating with a StringIO object
comprehension  creating a string with comprehension
=============  =====================================

An additional method using mutable strings was tried, but it was so slow it
wasn't tested.

The general method used in **test.py** is a tight loop over a large range
appending a numeric string.  This was tried with both python2 and python3
as well as with the garbage collector enabled and disabled.

In addition, the test code in **run.sh** runs a separate thread that monitors
memory usage of the program.

Results are automatically generated in **results.rst**.

Old Results
-----------

I first attempted this a few years ago.  These earlier results are in
**OLD_RESULTS.rst**.
