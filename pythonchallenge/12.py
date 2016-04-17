#   http://www.pythonchallenge.com/pc/return/evil.html
#
# This page has a title of "dealing evil" and contains an image (evil1.jpg,
# 640x480) of cards being dealed.  There is no hint text.
#
# The page source has nothing of interest.
#
# So the image must contain clues.  The image appears modified - it looks
# 'streaky' horizontally.  A closer look with the Gimp shows patterns that
# remind me of a closeup of a Sony Trinitron TV screen.
#
# After some thought, WHY is the image labelled 'evil1.jpg'?  Try:
#    http://www.pythonchallenge.com/pc/return/evil2.jpg
# This gets an image containing 'not jpg - _.gfx'.  Try:
#    http://www.pythonchallenge.com/pc/return/evil2.gfx
# This gets us an authentication dialog.  Enter huge/file and we download
# a 67.5kb file which the 'file' which the 'file' command helpfully identifies
# as 'data'.  Dumping the first few lies of the file as hgex+ascii we see:
#    0000  ff 89 47 89 ff d8 50 49 50 d8 ff 4e 46 4e ff e0  |..G...PIP..NFN..|  0
#    0010  47 38 47 e0 00 0d 37 0d 00 10 0a 61 0a 10 4a 1a  |G8G...7....a..J.|  16
#    0020  40 1a 4a 46 0a 01 0a 46 49 00 f0 00 49 46 00 00  |@.JF...FI...IF..|  32
#    0030  00 46 00 00 e7 00 00 01 0d 00 0d 01 01 49 00 49  |.F...........I.I|  48
#    0040  01 01 48 00 48 01 00 44 01 44 00 b4 52 00 52 b4  |..H.H..D.D..R.R.|  64
#    0050  00 00 00 00 00 b4 00 01 00 b4 00 01 04 01 00 00  |................|  80
#    0060  90 02 40 00 ff 00 00 00 ff e1 00 05 00 e1 08 01  |..@.............|  96
#    0070  00 00 0b a4 2c 02 f0 df 45 08 00 08 45 78 02 06  |....,...E...Ex..|  112
# which isn't too helpful.
#
# Trying:
#    http://www.pythonchallenge.com/pc/return/evil3.jpg
# gets a JPG file containing the text "no more evils...".  There is no evil3.gfx
# file.
# Trying:
#    http://www.pythonchallenge.com/pc/return/evil4.jpg
#
# Stumped - looked at http://garethrees.org/2007/05/07/python-challenge/ which
# the GFX file to be five interleaved files.  Splitting the GFX file into the
# five files gets us:
#     gfx_1.dat: JPEG image data, JFIF standard 1.01
#     gfx_2.dat: PNG image data, 400 x 300, 8-bit/color RGB, non-interlaced
#     gfx_3.dat: GIF image data, version 87a, 320 x 240
#     gfx_4.dat: PNG image data, 320 x 240, 8-bit/color RGB, non-interlaced
#     gfx_5.dat: JPEG image data, JFIF standard 1.01
#
# The five files, when viewed, get us "disproportional".


gfx_file = 'evil2.gfx'

with open(gfx_file, 'rb') as fd:
    gfx_data = fd.read()

with open('gfx_1.dat', 'wb') as fd:
    fd.write(gfx_data[0::5])

with open('gfx_2.dat', 'wb') as fd:
    fd.write(gfx_data[1::5])

with open('gfx_3.dat', 'wb') as fd:
    fd.write(gfx_data[2::5])

with open('gfx_4.dat', 'wb') as fd:
    fd.write(gfx_data[3::5])

with open('gfx_5.dat', 'wb') as fd:
    fd.write(gfx_data[4::5])

# gets a curious page that appears to hold a small white image with a double
# line border.  Using 'wget' to save evil4.jpg shows that the file is really
# text and contains "Bert is evil! go back!".  There is no evil4.gfx file.
#
# So it looks like all we have is the evil1.jpg file and the evil2.gfx file.
# And the possible clue "Bert is evil! go back!".
#

