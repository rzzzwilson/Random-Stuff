#!/usr/bin/env python3

"""
Show how to load/update/store a list of dictionaries.
"""

import json
import time


def get_data(filename):
    """Get stored list, returns empty list if no file."""

    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def put_data(filename, dict_list):
    """Store list in data file."""

    with open(filename, 'w') as f:
        json.dump(dict_list, f)

DataFilename = "test.dat"

# get stored data
dict_list = get_data(DataFilename)

# get highest count so far, create a new dictionary & append to list
max_count = 0
if dict_list:
    max_count = max([x['count'] for x in dict_list])
dict_list.append({'count': max_count+1, 'time': time.time()})

# store updated list
put_data(DataFilename, dict_list)
print(dict_list)   # debug - see what is happening
