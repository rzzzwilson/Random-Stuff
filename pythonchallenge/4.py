url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s'
first = '12345'

prefix = 'and the next nothing is '
len_prefix = len(prefix)

#
# The URL underneath the image is:
#    http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
# and if we goto that address by clicking on the image, we get simple text:
#    and the next nothing is 44827
# and presumably we have to plug in '44827' into the 'nothing' parameter,
# and so on.
#
# The page text has the hint:
#    urllib may help. DON'T TRY ALL NOTHINGS, since it will never end. 400 times is more than enough.
#
# HOW DOES THIS END?  Just follow and see what we get.
#

import sys
import urllib2

def do_loop(last):
    try:
        while True:
            new_url = url % last
            response = urllib2.urlopen(new_url)
            last_good = last
            data = response.read()
            index = data.find(prefix)
            if index == -1:
                print('Next URL: %s' % data)
                sys.exit()
            last = data[index+len_prefix:]
            print('last=%s, data=%s' % (last, data))
    except urllib2.HTTPError:
        return last_good

last = do_loop(first)
print('last=%s' % last)
last = str(int(last) / 2)
print('new last=%s' % last)

last = do_loop(last)
