#   http://www.pythonchallenge.com/pc/def/integrity.html
#
# This page has a title of "working hard?" and shows an image of a bee on some
# flowers.  Text under the image says "Where is the missing link?".  The image
# is active.
#
# Looking at the page source shows the image has a 'usemap'.  Clicking on the
# active part of the image (which is the bee itself) gets an authentication
# dialog which requires a username and password.
#
# Looking again at the page surce shows a comment:
#    <!--
#    un: 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
#    pw: 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
#    -->
# which obviously (?) contains the encoded username and password.  The un/pw
# strings start with "BZ" which suggests they are 'bzip' encoded.  Try using
# the 'bz2' module.
#
# We get a username of 'huge' and password of 'file' which sends us to puzzle 9.

import bz2


un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

result = bz2.decompress(un)
print('username=%s' % result)

result = bz2.decompress(pw)
print('password=%s' % result)
