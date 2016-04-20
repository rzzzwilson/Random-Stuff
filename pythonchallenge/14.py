#   http://www.pythonchallenge.com/pc/return/italy.html
#
# This page has a title of "walk around" and contains an image (italy.jpg,
# 640x480) of a spiral pastry.  The hint text is an image that looks like an
# edge diffraction pattern (wire.jpg, 10000x1, forced to 100x100),
#
# The page source shows nothing besides a comment:
#    <!-- remember: 100*100 = (100+99+99+98) + (...  -->
# and 10000 is 100*100.
#
# The image has some colour (red) at the left.  Looking closely at the image
# shows some structure.  Dump the image data by converting to wire.ppm.
#
# Try splitting into R, G and B channels: wire_r.ppm, wire_g.ppm and wire_b.ppm.
# Hmm, nothing obvious.
#
# The source comment and size of hint image seems to be implying the 10000x1
# image is a scan that should be displayed as 100x100.  On second thought, the
# 10000x1 data should SPIRAL out (or in) (hint: italy.jpg).  Another hint is
# the name of the 10000x1 image: wire.png.

in_file = 'wire.ppm'
out_file = 'spiral_wire.ppm'

# get all P3 PPM data
with open(in_file, 'rb') as fd:
    data = fd.readlines()

# skip first 4 lines
data = data[4:]

# create a new image 100x100 spiralling out from the centre

