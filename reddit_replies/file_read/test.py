#!/usr/bin/env python3

import json

filename = 'test.dat'

# variables to be saved/restored
balance = 180
hit_points = 2000

# try to restore variables from the data file
try:
    with open(filename, 'r') as fd:
        data = json.loads(bytes(fd.read(), 'utf-8'))
except FileNotFoundError:
    # if file not found, use default values above
    data = {'balance': balance, 'hit_points': hit_points}

# restore variables
balance = data['balance']
hit_points = data['hit_points']

print('START: balance=%d, hit_points=%d' % (balance, hit_points))

# increment both variables
balance += 10
hit_points -= 200

# save new values back to the data file
# use 'indent' and 'sort_keys' to make easier for humans
save_data = {'balance': balance, 'hit_points': hit_points}
with open(filename, 'w') as fd:
    fd.write(str(json.dumps(save_data, indent='    ', sort_keys=True)))

print('  END: balance=%d, hit_points=%d' % (balance, hit_points))
