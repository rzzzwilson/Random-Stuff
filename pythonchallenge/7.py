#   http://www.pythonchallenge.com/pc/def/oxygen.html
#
# This page has a title of "smarty" and shows an image of a rural scene with a
# monochrome stripe across the middle (left to right).  The stripe appears to be
# pixellated coarsely.  The pixellation could possibly some sort of encoding.
# The page source shows nothing of interest.
#
# The image is a PNG of size (629 x 95).  The pixellated strip has a height of
# 9 pixels and appears to have 'bits' of 9x7 bits.
#
# I initially thought that the strip was something similar to serial data as the
# blackest dot appeared just before a set of 8 other dots, but this failed later
# in the strip.  In addition, there are MANY grey levels in the pixellation, not
# just two if it were serial data.
# 
# The 'dots' are grey, so their RGB values are the same in the R, G and B values.
# From the left, we see these values:
#
#     115, 109, 97, 114, 116, 32, 103, 117, 121, 44, 121, 111, ...
#
# which looks like decimal ASCII characters.  Converting, we get:
#    smart guy, yo...
#
# How do we get the text without doing a lot of work by hand?  Convert the PNG
# to a PPM file which is ASCII text.  Here's the start of oxygen.ppm:
#
#    P3
#    # CREATOR: GIMP PNM Filter Version 1.1
#    629 95
#    255
#    79
#    92
#    23
#    72
#    87
#    18
#    61
#    77
#    
# The first 4 lines are:
#    1. identifier P3 (colour PPM)
#    2. a comment
#    3. image width and height in pixels
#    4. maximum pixel RGB value
#
# The following lines are decimal values for R, then G and finally B for one
# pixel.  We want to look at the pixellated pixels, which are in pixel row 47,
# starting from 0.  The data dots are 7 pixels wide and the first dot is short.
#
# Write code to read oxygen.ppm and output the data in ASCII.
#

ppm_file = 'oxygen.ppm'
row = 47
header_lines = 4
image_width = 629

# get raw data into memory
with open(ppm_file, 'rb') as fd:
    lines = fd.readlines()

# drop 4 header lines
lines = lines[4:]

# get only every third value (the R value)
r_lines = lines[::3]

# now get data starting at row 47
row_data = r_lines[image_width * row:]

# now get every 7th pixel
a_data = row_data[::7]

# and convert to ASCII, stopping after we find ']'
result = ''
for x in a_data:
    x_val = int(x)
    asc_val = chr(x_val)
    result += asc_val
    if asc_val == ']':
        break
print result

# we get "smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]"
level = [105, 110, 116, 101, 103, 114, 105, 116, 121]
result = ''
for x in level:
    x_val = int(x)
    asc_val = chr(x_val)
    result += asc_val
print result
