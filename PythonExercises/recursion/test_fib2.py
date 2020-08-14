"""
Code to run each Fibonacci implementation and compare run times.

Runs each file in this directory that start "fibonacci*.py".
Imports and executes each module found.

Usage: python3 test_fib.py <fib_num>
"""

import sys
import os
import time
import glob
import subprocess

LOOP = 1000

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

# import each module
fib_modules = []
for path in files:
    # get module name
    (module_name, _) = os.path.splitext(os.path.basename(path))
    imp_mod = __import__(module_name)
    fib_modules.append((module_name, imp_mod))

# now execute fibonacci() from each module passing the test number
# accumulate times in a dictionary
results = {}
for (module_name, imp_mod) in fib_modules:
    fib_func = getattr(imp_mod, 'fibonacci')
    start = time.time()
    fib_n = fib_func(num)
    delta = time.time() - start
# this doesn't work since the "memo" functions are really quick the second time!
#    if delta < 1:
#        start = time.time()
#        for _ in range(LOOP):
#            fib_n = fib_func(num)
#        delta = (time.time() - start) / LOOP
    results[module_name] = delta

# figure out the maximum module name width
max_path_width = 0
for (module_name, time) in results.items():
    if len(module_name) > max_path_width:
        max_path_width = len(module_name)

# get file+time into a list of tuples and sort by ascending time
results = sorted(results.items(), key=lambda x: x[1])

# now display the results: file | time | speed
(fast_path, fast_time) = results[0]
print(f" {'FILE':{max_path_width}s} |  RUNTIME    | RESULTS")
print(f"{'-'*max_path_width}--+-------------+--------------------------------")
for (path, time) in results:
    if path == fast_path:
        print(f' {path:{max_path_width}s} | {time:10.7f}s | this is the fastest')
    else:
        print(f' {path:{max_path_width}s} | {time:10.7f}s | {time/fast_time:10.1f} times slower')
