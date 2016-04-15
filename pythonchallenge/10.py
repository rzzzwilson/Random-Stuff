#   http://www.pythonchallenge.com/pc/return/bull.html
#
# This page has a title of "what are you looking at?" and a JPG image (640x480)
# showing a bull and young cow.  The image appears to be a 'usemap' image.
# Underneath the image we have the text "len(a[30]) = ?".
#
# Clicking on the image gets a page of text: 'a = [1, 11, 21, 1211, 111221, '
# which is in a file sequence.txt.  So it appears we have to continue the
# sequence and compute the length of element a[30].
#
# The given sequence doesn't contain any digits other than '1' and '2'.  So
# maybe it's binary with '1' = 1 and '2' = 0?  Or maybe it's ternary?  When
# interpreted as ternary we get [1, 4, 7, 49, 376, ] in decimal.
#
# The page title "what are you looking at?" certainly suggests we look at
# different representations of the sequence.

a = [1, 11, 21, 1211, 111221,]

# try different bases
aa = ['1', '11', '21', '1211', '111221',]
for base in [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
    b = [int(x, base) for x in aa]
    print('base %d: %s' % (base, str(b)))

# try the length of each element as the sequence
b = [len(x) for x in aa]
print('len: %s' % str(b))

# what about treating changes as string manipulations?
