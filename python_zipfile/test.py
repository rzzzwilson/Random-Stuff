"""
Compare the speed of accessing pySlip tiles from:

* an unzipped tiles directory
* a zipped tiles file
# same data but *.tar.gz

Also chck that the data read is the same no matter what method
it is read by.
"""

import os
import time
import zipfile
import tarfile


TilesUnzipped = os.path.abspath(os.path.expanduser('~/gmt_local_tiles'))
TilesZipped = os.path.abspath('./gmt_local_tiles.zip')
TilesTarred = os.path.abspath('./gmt_local_tiles.tar.gz')

ZoomLevel = 4
MaxTilesWide = 32
MaxTileHigh = 16
Loop = 10

UnzippedData = []
ZippedData = []
TarredData = []
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

    with zipfile.ZipFile(TilesZipped) as zf:
        for _ in range(Loop):
            for x in range(MaxTilesWide):
                for y in range(MaxTileHigh):
                    path = os.path.join(f'gmt_local_tiles/{ZoomLevel}/{x}/{y}.png')
                    data = zf.read(path)
                    ZippedData.append(data)

def get_tarred():
    """Function that gets a number of tiles from a tar.gz directory."""

    with tarfile.open(TilesTarred, 'r') as zf:
        for _ in range(Loop):
            for x in range(MaxTilesWide):
                for y in range(MaxTileHigh):
                    path = os.path.join(f'gmt_local_tiles/{ZoomLevel}/{x}/{y}.png')
                    data = zf.extractfile(path).read()
                    TarredData.append(data)

print()
start = time.time()
get_unzipped()
delta = time.time() - start
print(f'unzipped took {delta:5.2f}s')

start = time.time()
get_zipped()
delta = time.time() - start
print(f'  zipped took {delta:5.2f}s')

start = time.time()
get_tarred()
delta = time.time() - start
print(f'  tarred took {delta:5.2f}s')

# compare the two lists of tile data to make sure they are the same
error = False
if UnzippedData != ZippedData:
    print(f'\nData read from unzipped source is NOT THE SAME as data from zipped source')
    error = True
if UnzippedData != TarredData:
    print(f'\nData read from unzipped source is NOT THE SAME as data from tar.gz source')
    error = True
if not error:
    print(f'\nData the same no matter what the source')
