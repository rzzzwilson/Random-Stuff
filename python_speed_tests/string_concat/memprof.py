#!/usr/bin/env python

"""Monitor memory usage of a given process.

Usage: memprof.py <PID> <logfile>

where <PID>      is the ID of the process to monitor
      <logfile>  is the file to write data into
"""


import time
import platform

def main(pid, logfile):
    """Monitor process 'pid' and write data to 'logfile'."""


