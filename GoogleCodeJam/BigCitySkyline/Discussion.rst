Big City Skyline
================

This was the first Google Code Jam problem I attempted a *long* time ago.  I
have fond memories of this problem, and still feel proud that I got it to run
within the memory and time limits **with python**.

I should have my original attempt somewhere on backup, but I will attempt it
again here.

Since we have no given test data and time/memory limits, we create a program
to generate test data of configurable size.  See **make_data.py**.

How do we solve this?
---------------------

The major problem is that it's not good enough to just remember the most recent
biggest block.  A following building that is shorter than previous buildings
will create a smaller block than previous blocks, but before the end of the
buildings is reached the smaller block may have grown bigger in size than
existing bigger blocks.

This suggests that we must keep track of *all* open blocks (blocks that can
get bigger) as well as the single *biggest* closed block (a block that will not
grow any more).

A block needs these attributes:

* start coordinate
* height
* open (True or False)
* area (updated if open)

We might not need the **.open** attribute as we are going to have a list of
open blocks and a single reference to the largest closed block.

So the algorithm, after initializing with the first block, is:

1. Get the next building width and height, if none:
   * print area of largest closed or open blocks
   * exit
2. If the new height is > last_height:
   * start a new open block
   * extend all existing open blocks (change .width and .area)
   * set last_height to new height
   * goto step 1
3. if the new height == last_height
   * extend all existing open blocks (change .width and .area)
   * goto step 1
4. if the new height < last_height:
   * modify all existing open blocks with height > new height (.width, .height and .area)
   * close all modified blocks (save with pre-modified values)
   * choose largest closed block
   * set last_height to new height
   * goto step 1

Initial attempt running.  It gets the correct answer for the *small.in* dataset.
Generating a very large dataset in *largest.in* with **make_data.py** makes
the program use almost 2GB of memory and it runs for about 3m40s.  No idea if
the answer it gives is correct.

Generate a smaller test dataset that we know the answer for (by hand).  Debug
the current program to ensure we are deleting things we expect to be deleted,
like closed blocks with small areas.
