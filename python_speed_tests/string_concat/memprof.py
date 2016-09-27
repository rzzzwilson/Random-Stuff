#!/usr/bin/env python

"""Monitor memory usage of a given process.

Usage: memprof.py <PID> <logfile>

where <PID>      is the ID of the process to monitor
      <logfile>  is the file to write data into

Code to get memory used by a process from:
    http://code.activestate.com/recipes/286222/
"""


import sys
import time


_scale = {'kB': 1024.0, 'mB': 1024.0*1024.0,
          'KB': 1024.0, 'MB': 1024.0*1024.0}

def _VmB(pid, VmKey):
    """Private."""

    global _scale

    filepath = '/proc/%d/status' % pid

    # get pseudo file  /proc/<pid>/status
    try:
        with open(filepath, 'r') as fd:
            v = fd.read()
    except (NameError, IOError):
        return 0.0  # non-Linux?

    # get VmKey line e.g. 'VmRSS:  9999  kB\n ...'
    try:
        i = v.index(VmKey)
    except ValueError:
        return 0            # no such line in file
    v = v[i:].split(None, 3)  # whitespace
    if len(v) < 3:
        return 0    # invalid format?

    # convert Vm value to bytes
    return int(v[1]) * _scale[v[2]]

def memory(pid, since=0.0):
    """Return memory usage in bytes."""
    return _VmB(pid, 'VmSize:') - since
    
def resident(pid, since=0.0):
    """Return resident memory usage in bytes."""

    return _VmB(pid, 'VmRSS:') - since
    
def stacksize(pid, since=0.0):
    """Return stack size in bytes."""

    return _VmB(pid, 'VmStk:') - since

def main(pid, logfile):
    """Monitor process 'pid' and write data to 'logfile'."""

    with open(logfile, 'wa') as fd:
        value = 1
        while value:
#            value = resident(pid)
            value = memory(pid)
            fd.write('%d\n' % value)
#            time.sleep(0.01)


if len(sys.argv) != 3:
    usage()
else:
    pid = int(sys.argv[1])
    logfile = sys.argv[2]
    main(pid, logfile)
