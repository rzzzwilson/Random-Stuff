This program solves puzzles consisting of a rectangular board made up of squares
cut up into puzzle pieces.  The aim of the puzzle is to reassemble the board.

A small simple run showing operation of the program is:

::

    solver [-g] <datafile>

where the **-g** option turns on the graphical display.  Note that program is
much slower with that option.  In addition to printing solutions to the console
a picture of each solution is saved in an encapsulated postscript file in the
current directory.  I really wanted a bitmap file, but Tkinter only allowed a
simple save to postscript.

A simple run would be:

::

    solver -g test.dat

There are more details in the wiki:
<https://github.com/rzzzwilson/Random-Stuff/wiki/puzzle-solver>.

solver3
-------

This is a rewrite of the program for python3.

Postscript
----------

On reflection, this is probably the first *real* graphics program I ever wrote
in python.  Looking at the code I see that my style is sort of similar to my
current style so I had been using python for a while already.

My oldest archived copy of *solver* is **solver.archive**.  The main substantive
changes are:

* Moved pre-function block comments into the function doc string
* Removed unnecessary *global* statements (I hadn't yet learned that they are
  necessary only if changing the global)
* Removing backslash line continuations and using () enclosing instead

Not bad for greater than 10 year old code!

I think part of the reason for so little change over that time is partly due
to me having a lot of experience prior to that point in time and also to
python having such a simple syntax that there is really **only one way to do it™**.
