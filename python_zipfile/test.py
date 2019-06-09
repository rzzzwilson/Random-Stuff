"""
Compare the speed of accessing pySlip tiles from:

* an unzipped tiles directory
* a zipped tiles file

Also chck that the data read is the same no matter what method
it is read by.
"""

import os
import time
import zipfile


TilesUnzipped = os.path.abspath(os.path.expanduser('~/gmt_local_tiles'))
TilesZipped = os.path.abspath('./gmt_local_tiles.zip')

ZoomLevel = 4
MaxTilesWide = 32
MaxTileHigh = 16
Loop = 100

UnzippedData = []
ZippedData = []

def get_unzipped():
    """Function that gets a number of tiles from an unzipped dicretory."""

    for _ in range(Loop):
        for x in range(MaxTilesWide):
            for y in range(MaxTileHigh):
                path = os.path.join(f'{TilesUnzipped}/{ZoomLevel}/{x}/{y}.png')
                with open(path, 'rb') as tile:
                    data = tile.read()
                    UnzippedData.append(data)

def get_zipped():
    """Function that gets a number of tiles from a zipped directory."""

    for _ in range(Loop):
        with zipfile.ZipFile(TilesZipped) as zf:
            for x in range(MaxTilesWide):
                for y in range(MaxTileHigh):
                    path = os.path.join(f'gmt_local_tiles/{ZoomLevel}/{x}/{y}.png')
                    data = zf.read(path)
                    ZippedData.append(data)

start = time.time()
get_unzipped()
delta = time.time() - start
print(f'unzipped took {delta:.2f}s')

start = time.time()
get_zipped()
delta = time.time() - start
print(f'  zipped took {delta:.2f}s')

# compare the two lists of tile data to make sure they are the same
if UnzippedData != ZippedData:
    print(f'\nData read from unzipped source is NOT THE SAME as data from zipped source')
