The code here investigates using a zipped directory to access
cached objects like tiles.  The idea is to see if it's feasible
to store the pySlip GMT tiles in the original zipped (or *.tar.gz*)
form and not need to unzip it before using it.  If it works, get some
idea of the relative speeds zipped/tarred/unzipped.

Results
-------

The final timing show that reading tiles from a zipped directory is
about teice as slow as reading from the unzipped directory.  The tarred
directory was about 300 times slower than reading the unzipped directory::

    $ python3 test.py
    
    unzipped took  0.26s
      zipped took  0.58s
      tarred took 76.52s
    
    Data the same no matter what the source

So we will keep the unzipped *~/gmt_local_tiles* directory for pySlip,
but keep the unzipped approach in mind.
