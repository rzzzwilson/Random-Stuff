#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test code for a persistent dictionary.

https://www.reddit.com/r/learnpython/comments/5nvyc9/how_can_i_define_a_dictionary_at_the_start_of_a/
"""

import pickle


PersistentDictFilename = 'mydict.data'


def load_dict(filename):
    """Restore a dictionary from a disk file."""

    try:
        with open(filename, 'rb') as handle:
            my_dict = pickle.load(handle)
    except FileNotFoundError:
        my_dict = {}

    return my_dict

def process(data_dict):
    """Do something to the dictionary."""

    if not 'counter' in data_dict:
        data_dict['counter'] = 0

    data_dict['counter'] = data_dict['counter'] + 1
    print("Updated data_dict['counter']: is %d after incrementing"
            % data_dict['counter'])

def save_dict(filename, my_dict):
    """Save the dictionary into the given file."""

    with open(filename, 'wb') as handle:
        pickle.dump(my_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

def main():
    """Recover dict, process and then save dict to a file."""

    data_dict = load_dict(PersistentDictFilename)
    process(data_dict)
    save_dict(PersistentDictFilename, data_dict)


main()
