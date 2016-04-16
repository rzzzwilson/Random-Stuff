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
# different representations of the sequence.  In particular, "len(a[30])"
# implies that the 'a' elements must be interpreted as strings - can't have
# a length of an integer.
#
# [the next day] OK, I cheated by getting a hint.  I did google for the site
# that gave me the sequence name, but I didn't find it.  The hint at
# http://garethrees.org/2007/05/07/python-challenge/ gave me the site used
# to identify the sequence: https://oeis.org/A005150 .

# the sequence
a = ['1', '11', '21', '1211', '111221',]

# a function that, given a sequence string, produces the next sequence string.
def look_and_say(elt):
    """Generate the next sequence string following 'elt'."""

    index = 0
    result = ''
    max_index = len(elt)
    while index < max_index:
        letter = elt[index]
        count = 1
        index += 1
        if index >= max_index:
            result += '%d%s' % (count, letter)
            break
        if elt[index] == letter:
            count += 1
            index += 1
            if index >= max_index:
                result += '%d%s' % (count, letter)
                break
            if elt[index] == letter:
                count += 1
                index += 1
                if index >= max_index:
                    result += '%d%s' % (count, letter)
                    break
        result += '%d%s' % (count, letter)

    return result

count = 0
next = '1'
print('%d=%s' % (count, next))
count += 1

while count <= 30:
    next = look_and_say(next)
    print('len(%d)=%d' % (count, len(next)))
    count += 1
