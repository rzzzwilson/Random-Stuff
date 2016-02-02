I wrote the original of this program a *very* long time ago (1978).  I was
studying at Sydney University in the Basser Department of Computer Science.  One
of the lecturers had a puzzle that consisted of a chessboard (all one colour)
that was cut into a small number of irregular contiguous shapes consisting of
board squares glued together.  The puzzle was to place all the pieces such that
the original board was reconstructed.  A challenge was laid down - solve the
puzzle using a computer.

I did so, initially using Pascal on a CDC Cyber mainframe to get the basic idea
tested which was exhaustive search with backtrack.  My student account on that
machine was just about to run out but I had learned that the accounting test
was applied only at the **beginning** of a session.  So I started my first real
test of the program and waited, hoping it would work.  After about 20 minutes
the program printed a first solution!

Next I rewrote the program in BCPL and ran it on a Burroughs 1700.  Some effort
was required to make the program fit on that machine but it eventually worked
well.  I believe it was called *puzz* on the Burroughs.

I had in the back of my mind the idea that it would be possible to write a
similar program that would accept a description of the board and the puzzle
pieces and compute solutions (if any).  I tried to write this in C some years
later but could never get it debugged.

Then python came along.  I always try to learn new languages by reimplementing
various programs I had written in the past in the new language, so my first
attempt at anything other than a toy program was **solver**.  It went together
surprisingly quickly and much more easily than the equivalent C program.  It
also needed far less debugging. This version just printed solutions to the
console.

I wanted to *see* the algorithm doing its backtracking, so I wrote a new version
that displayed the board to solve and the current possible solution pieces on
the board, using Tkinter.  The hard part was generating representations of the
pieces from the input data file.

This was solved by pre-generating partial tiles that showed each quarter portion
of a tile with all combinations of possible neighbour quarter tiles.  These were
put into the **tiles** subdirectory.  The program uses those quarter tiles when
constructing the picture of each puzzle piece.

A small run showing operation of the program is:

    solver [-g] <datafile>

where the **-g** option turns on the graphical display.  Note that program is
much slower with that option.

A simple run would be:

    solver -g test.dat

Some effort has been made to make this run at reasonable speeds:
. Doesn't use piece shapes that are the same as previous shapes (isomorphs)
. Precalculate what can be precalculated

What remains to be done:
. Handle isomorph *pieces*, not just isomorph shapes for the same piece
  (not sure this will speed things up though)
. Recognize 'impossible' situations and backtrack immediately
  (eg, single empty square in filled pieces and no single square piece)

Optimization:
Simple changes, like replacing p.isInUse() with p.inUse == True, do make
solver faster, such as reducing runtime for test3.dat from 9m19.6s to
8m33.5s.  These changes aren't in the latest version.

Read the program source for more details.
