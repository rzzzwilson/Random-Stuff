The code here investigates using a zipped directory to access
cached objects like tiles.  The idea is to see if it's feasible
to store the pySlip GMT tiles in the original zipped form and
not need to unzip it before using it.  If it works, get some
idea of the relative speeds zipped/unzipped.

Results
-------

The final timing show that reading tiles from a zipped directory is
between 2 and 3 times slower than reading from the unzipped directory.

So we will keep the unzipped *~/gmt_local_tiles* directory for pySlip,
but keep the unzipped approach in mind.
