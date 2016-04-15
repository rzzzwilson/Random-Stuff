#    http://www.pythonchallenge.com/pc/def/channel.html
#
# This page shows a zipper and has a PayPal donate button.
#
# The PayPal button appears not to be part of the puzzlle.
#
# The page has a title "now there are pairs" and the page source includes
# a comment: "<!-- <-- zip -->".
#
# Looking at http://www.pythonchallenge.com/pc/def/zip.html just gets a text
# page saying: "yes. find the zip."
#
# Going to www.pythonchallenge.com/pc/def/channel.zip gets a ZIP file.
# This contains [0-9]*.txt files and a README.
#
# This looks similar to the 5 problem.  The readme says:
#    welcome to my zipped list.
#
#    hint1: start from 90052
#    hint2: answer is inside the zip
#
# Running through the text files starting at 90052.txt we find in file
# 46145.txt the text:
#    Collect the comments.
#
# Doing "unzip -l channel.zip" shows there are comments in the ZIP file:
#    Archive:  channel.zip
#      Length     Date   Time    Name
#     --------    ----   ----    ----
#    21  06-06-06 06:06   29.txt
#    E
#    21  06-06-06 06:06   100.txt
#    
#    21  06-06-06 06:06   109.txt
#    Y
#
# Strip out the comments.  We see SOMETHING in the "unzip -l" output, but it
# doesn't look useful.
#
# Maybe we have to order the comments in the order we step through the files?
# Yes!  If we print with a line-length of 64, we see:
# ****************************************************************
# ****************************************************************
# **                                                            **
# **   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
# **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
# **   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
# **   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
# **   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
# **   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
# **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
# **   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
# **                                                            **
# ****************************************************************
#  **************************************************************
#
# (We found the 64 length by printing the data as one line and then
#  changing the termional width seeing how the line wrapped.)
#
# Browsing to: http://www.pythonchallenge.com/pc/def/hockey.html
# we get a page with text: "it's in the air. look at the letters."
#
# Browsing to: http://www.pythonchallenge.com/pc/def/oxygen.html
# we get to problem 7!
#


import sys
import os.path
import subprocess
import re

prefix = 'nothing is '
len_prefix = len(prefix)
first = '90052'
channel_dir = 'channel'
zip_file = 'channel.zip'

def do_loop(last):
    files_seen = [last]

    while True:
        with open(os.path.join(channel_dir, last+'.txt'), 'rb') as fd:
            data = fd.read()
        index = data.find(prefix)
        if index == -1:
            print('Next: %s-> %s' % (last, data))
            return files_seen
        last = data[index+len_prefix:]
        files_seen.append(last)

# flist wll contain ordered list of filenames
flist = do_loop(first)

zip_path = os.path.join(channel_dir, zip_file)

cmd = ['unzip', '-l', '%s' % zip_path]
p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(out, err) = p.communicate()
out = out.split('\n')

# delete first three lines, last 2, then get a list of (filename, comment)
out = out[3:]
out = out[:-4]
#print str(out)
whole_fnames = out[::2]
comments = out[1::2]

fnames = {}
for (name, comment) in zip(whole_fnames, comments):
    n = re.split('\s+', name)[-1]
    fnames[n] = comment

# now step through filenames in time order and print comments
data = ''
for f in flist:
    d = fnames[f+'.txt']
    data += d

line_len = 64
while data:
    print data[:line_len]
    data = data[line_len:]
