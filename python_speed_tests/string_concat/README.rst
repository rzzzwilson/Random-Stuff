String Concatenation
====================

If you read the Python programming blogs or google for
"python string concatenation" you find statements that the naive::

    a += b

method of concatenating strings is horribly slow and uses too much memory.

Well, it's not that simple with newer Pythons after 2.5 or so. The code here
tests various methods of concatenating strings:

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

The general method used in each test executable is a tight loop over a large
range appending a numeric string.  This was tried with both python2 and python3
as well as with the garbage collector enabled and disabled, just to see if that
made a difference.

Each test of various concatenation method is done in a standalone executable. 
The executable is run by *memprof.py* with the memory results saved in a single
file and the timing results saved in the stdout save files produced by memprof.py.
These results are automatically generated in **results.rst** which will be
displayed through github.

There is also code that attempts to defeat the python interpreters *inlining*
of string concatenation.  It appears to be enough to declare the variable
we are concatenating into as a global.

The real surprise is in the memory used by each concatenation method.  The
memory results for python3 are unexpected, and this is still being investigated.

Old Results
-----------

I first attempted this a few years ago.  These earlier results are in
**OLD_RESULTS.rst** for python 2 only.
