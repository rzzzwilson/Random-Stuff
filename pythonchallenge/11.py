#   http://www.pythonchallenge.com/pc/return/5808.html
#
# This page has a title of "odd even" and has an image (cave.jpg, 640x480,
# blurred) showing some people.  There is no text showing.
#
# The page source contains nothing special.
#
# The image appears to be 'half-tone' or something similar.  Looking at it with
# the Gimp at 400% scale shows that there is a 'chess board' of black pixels
# on the image with the original image pixels showing through at the white
# square positions.
#
# Maybe the black pixels are introduced and not a mask.  Try removing them
# and getting a 320x240 image.

# cave.jpg converted to PPM by the Gimp
in_pic = 'cave.ppm'
out_pic = 'new_cave.ppm'

with open(in_pic, 'rb') as in_fd:
    in_data = in_fd.readlines()
print('in_data[:10]=%s' % str(in_data[:10]))

with open(out_pic, 'wb') as out_fd:
    # write new header
    out_fd.write('P3\n')
    out_fd.write('# CREATOR: 11.py\n')
    out_fd.write('320 240\n')
    out_fd.write('255\n')

    # start at first data triple
    index = 4

    # read groups of three lines, skipping first and every other thereafter
    # have to handle end of scan line properly
    max_index = len(in_data)
    while index < max_index:
        for _ in range(320):
            # first line
            index += 3      # skip black pixel
            out_fd.write(in_data[index])
            index += 1
            out_fd.write(in_data[index])
            index += 1
            out_fd.write(in_data[index])
            index += 1

        for _ in range(320):
            # next line
            out_fd.write(in_data[index])
            index += 1
            out_fd.write(in_data[index])
            index += 1
            out_fd.write(in_data[index])
            index += 1
            index += 3      # skip black pixel
