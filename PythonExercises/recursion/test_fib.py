"""
Code to run each Fibonacci implementation and compare run times.

Runs each file in this directory that start "fibonacci*.py".

Usage: python3 test_fib.py <number>
"""

import sys
import os
import glob
import subprocess

def usage(msg=None):
    if msg:
        print('=' * 60)
        print(msg)
        print('=' * 60)
    print(__doc__)

def test_file(path, num):
    result = subprocess.check_output(['python3', path, num]).decode("utf-8")
    return result

# get the number for which the Fibonacci number is required
if len(sys.argv) != 2:
    usage()
    sys.exit(1)

try:
    num = int(sys.argv[1])
except ValueError:
    usage('You must enter an integer number!')
    sys.exit(1)

# get all executable python files that start "fibonacci".
files = glob.glob('./fibonacci*.py')

# now execute each file passing the test number
# accumulate times in a dictionary
results = {}
for path in files:
    path = os.path.basename(path)
    results[path] = subprocess.check_output(['python3', path, f'{num}']).decode("utf-8")

# parse each result string and replace with the time value
# each value string has the form "fibonacci_memo(40)=102334155     took 0.0000310s\n"
# also gather the fastest file name and the time
max_path_width = 0
for (key, value) in results.items():
    (_, time) = value.split('took ')
    time = float(time[:-2])
    results[key] = time
    if len(key) > max_path_width:
        max_path_width = len(key)

# get file+time into a list of tuples and sort by ascending time
results = sorted(results.items(), key=lambda x: x[1])

# now display the results: file | time | speed
(fast_path, fast_time) = results[0]
print(f" {'FILE':{max_path_width}s} |  RUNTIME   | RESULTS")
print(f"{'-'*max_path_width}--+------------+--------------------------------")
for (path, time) in results:
    if path == fast_path:
        print(f' {path:{max_path_width}s} | {time:9.6f}s | this is the fastest')
    else:
        print(f' {path:{max_path_width}s} | {time:9.6f}s | {time/fast_time:9.1f} times slower')
