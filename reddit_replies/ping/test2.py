#!/usr/bin/python

import subprocess

nrange = "192.168.0."

for i in range(1, 254):
    address = nrange + str(i)
    try:
        out = subprocess.check_output('ping -c 3 -W 3 %s' % address,
                                      stderr=subprocess.STDOUT, shell=True)
        res = 0
    except subprocess.CalledProcessError as e:
        out = e.output
        res = e.returncode
    if res == 0:
        print address 
