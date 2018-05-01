#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test code in reply to:
https://www.reddit.com/r/learnpython/comments/645ig0/may_i_have_advice_on_how_to_address_this_problem/
"""

import json

json_file = 'test.json'

######
# first, create a simple object and write it to the JSON file
# we do this just to create a JSON file that we read
######

obj = [1, 'two', {1: 'one', 2:2}]       # put anything here
print('obj=%s' % str(obj))              # look at original object
with open(json_file, 'w') as fp:
    json.dump(obj, fp)

######
# now read the JSON file and process two different ways
######

out_file1 = 'output1.txt'
out_file2 = 'output2.txt'

def process1(json_obj, out_file_name):
    result = 'JSON object is of type %s\n' % type(json_obj)
    with open(out_file_name, 'w') as fp:
        fp.write(result)

def process2(json_obj, out_file_name):
    with open(out_file_name, 'w') as fp:
        for (ndx, elt) in enumerate(json_obj):
            fp.write('Element %d: %s\n' % (ndx, str(elt)))

# read all the JSON data into memory
with open(json_file) as fp:
    new_obj = json.load(fp)
print('new_obj=%s' % str(new_obj))      # look at the new object from JSON file

# process JSON data two different ways
process1(new_obj, out_file1)
process2(new_obj, out_file2)
