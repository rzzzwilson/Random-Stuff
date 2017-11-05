#!/usr/bin/env python3

import pickle

filename = 'test.dat'

# variables to be saved/restored
balance = 180
hit_points = 2000

# try to restore variables from the data file
try:
    with open(filename, 'rb') as fd:
        data = pickle.load(fd)
except FileNotFoundError:
    # if file not found, use default values above
    data = {'balance': balance, 'hit_points': hit_points}

# restore variables
balance = data['balance']
hit_points = data['hit_points']

print('START: balance=%d, hit_points=%d' % (balance, hit_points))

# modify both variables
balance += 10
hit_points -= 200

# save new values back to the data file
# use 'indent' and 'sort_keys' to make easier for humans
save_data = {'balance': balance, 'hit_points': hit_points}
with open(filename, 'wb') as fd:
    pickle.dump(save_data, fd)

print('  END: balance=%d, hit_points=%d' % (balance, hit_points))
