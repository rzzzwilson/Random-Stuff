#
# http://www.pythonchallenge.com/pc/def/peak.html
#
# Page 5 shows a 'peak' image with the text:
#    pronounce it
#
# The page text has a hint in a comment:
#    peak hell sounds familiar ?
#
# I must admit I didn't get this, possibly because of accent differences.
# I also didn't pick up on the significance of the 'banner.p' file as I
# associate .P files with Pascal.
#
# Anyway, 'banner.p' is a pickle file, which contains a list something like:
#    [[(' ', 95)],
#     [(' ', 14), ('#', 5), (' ', 70), ('#', 5), (' ', 1)],
#     [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)],
#     ...
#    ]
#
# This looks like a run-length encoded picture.  When decoded, it shows:
#                                   
#               #####                                                                      ##### 
#                ####                                                                       #### 
#                ####                                                                       #### 
#                ####                                                                       #### 
#                ####                                                                       #### 
#                ####                                                                       #### 
#                ####                                                                       #### 
#                ####                                                                       #### 
#       ###      ####   ###         ###       #####   ###    #####   ###          ###       #### 
#    ###   ##    #### #######     ##  ###      #### #######   #### #######     ###  ###     #### 
#   ###     ###  #####    ####   ###   ####    #####    ####  #####    ####   ###     ###   #### 
#  ###           ####     ####   ###    ###    ####     ####  ####     ####  ###      ####  #### 
#  ###           ####     ####          ###    ####     ####  ####     ####  ###       ###  #### 
# ####           ####     ####     ##   ###    ####     ####  ####     #### ####       ###  #### 
# ####           ####     ####   ##########    ####     ####  ####     #### ##############  #### 
# ####           ####     ####  ###    ####    ####     ####  ####     #### ####            #### 
# ####           ####     #### ####     ###    ####     ####  ####     #### ####            #### 
#  ###           ####     #### ####     ###    ####     ####  ####     ####  ###            #### 
#   ###      ##  ####     ####  ###    ####    ####     ####  ####     ####   ###      ##   #### 
#    ###    ##   ####     ####   ###########   ####     ####  ####     ####    ###    ##    #### 
#       ###     ######    #####    ##    #### ######    ###########    #####      ###      ######
#

import pickle

fname = 'banner.p'

with open(fname, 'rb') as fd:
    data = pickle.load(fd)

for l in data:
    line = ''
    for (ch, num) in l:
        line += ch * num
    print line
