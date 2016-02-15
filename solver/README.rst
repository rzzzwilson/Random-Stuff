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

Postscript
----------

On reflection, this is probably the first *real* graphics program I ever wrote
in python.  Looking at the code I see that my style is sort of similar to my
current style so I had been using python for a while already.
