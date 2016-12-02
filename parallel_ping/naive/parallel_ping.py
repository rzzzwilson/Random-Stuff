#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ping lots of hosts in series, one at a time.
(Despite the filename!)

WARNING: little in the way of _proper_ error handling is used here!
"""

import os
import sys
import time
import subprocess

# default timeout in seconds
DefaultTimeout = 5


def parallel_ping(hosts, timeout=DefaultTimeout, **kwargs):
    """Perform a serial ping on hosts.

    hosts    a list of hosts to ping
    timeout  timeout for the ping command
    kwargs   dict of possible extra ping args

    Any 'timeout' in 'kwargs' overrides the 'timeout' parameter.
    Any 'count number' in 'kwargs' is ignored.

    Returns a list of tuples:
        [(IP, host, result), ...]
    where IP      is the IP address of the host (from ping)
          host    is the original given host name (may be a domain or IP)
          result  is a summary response
    """

    # examine the extra args
    if 'timeout' in kwargs:
        timeout = kwargs['timeout']

    # prepare result list
    result = []

    # do a ping for each host
    for host in hosts:
        # create the 'ping' command
        cmd = ('ping -c 1 -t %d %s' % (timeout, host))

        # execute the ping, examine the output
        start = time.time()
        try:
            output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            output = e.output       # ignore error and return the output
        delta = time.time() - start
        output = output.decode('utf-8')

        # determine IP, if any
        ip = ''         # assume there was no DNS lookup
        if output.startswith('PING'):
            # possible successful ping
            left = output.find('(')
            right = output.find(')')
            if left != -1 and right != -1:
                ip = output[left+1:right]

        if 'cannot resolve' in output:
            # no DNS lookup
            response = 'DNS failure (%.4fs)' % delta
        elif '0 packets received' in output:
            response = 'No response (%.4fs)' % delta
        else:
            # successful ping
            response = 'Host is up (%.4fs)' % delta

        result.append((ip, host, response))

    return result


if __name__ == '__main__':
    import getopt

    def usage(msg=None):
        if msg:
            print(('*'*80 + '\n%s\n' + '*'*80) % msg)
        print('Usage: parallel_ping [-t <seconds>]')


    # hosts to ping
    hosts = ('google.com',       # OK
             '127.1.1.2',        # expect 'no response'
             'example.com',      # OK
             'no_such_site.xyz', # expect DNS failure
             '8.8.8.8',          # google DNS server, OK
             '8.8.4.4',          # google DNS server, OK
             '127.0.0.1',        # local machine
             '127.1.1.1',        # expect 'no response'
            )

    # handle extra CLI params
    argv = sys.argv[1:]

    try:
        (opts, args) = getopt.getopt(argv, 'ht:', ['help', 'timeout='])
    except getopt.GetoptError as err:
        usage(err)
        sys.exit(1)

    kwargs = {}
    for (opt, param) in opts:
        if opt in ['-h', '--help']:
            usage()
            sys.exit(0)
        elif opt in ['-t', '--timeout']:
            timeout = int(param)
            kwargs['timeout'] = timeout

    result = parallel_ping(hosts, **kwargs)

    if result:
        for (ip, name, response) in result:
            print('%-17s%-40s%s' % (str(ip), str(name), str(response)))
    else:
        print('No results')

