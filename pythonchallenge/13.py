#   http://www.pythonchallenge.com/pc/return/disproportional.html
#
# This page has a title of "call him" and contains an image (disprop.jpg,
# 640x480) of a telephone.  The hint text is "phone that evil".  The image
# appears to have nothing hidden within.
#
# The page source shows the image has a usemap which is a circle placed over
# the "5" button of the phone.  Activating the button runs "../phonebook.php"
# and gets an XML response # with a "faultCode" of 105 and "faultString" of:
#     XML error: Invalid document end at line 1, column 1
#
# The page source has the following to display the hint:
#    <font color="gold"/>
#    <br><b>
#        phone that <remote /> evil
#    </br>
# Not sure what that "<remote />" is telling me.
#
# Argh! Stuck, and the hints at http://garethrees.org/2007/05/07/python-challenge/
# show I need to use XML-RPC to solve this.  The answer is "ITALY".
