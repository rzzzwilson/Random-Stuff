#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ping lots of hosts in parallel, as many threads as there are hosts.

WARNING: little in the way of _proper_ error handling is used here!
"""

import time
import threading
import subprocess
import queue


def parallel_ping(hosts, timeout=5, **kwargs):
    """Perform a massive parallel ping on hosts.

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

    # a thread class to do one ping
    class Worker(threading.Thread):
        def __init__(self, cmd, host, result_q):
            super().__init__()
            self.cmd = cmd
            self.host = host
            self.result_q = result_q

        def run(self):
            # execute the ping, examine the output
            start = time.time()
            #proc = subprocess.run(self.cmd, shell=True, stderr=subprocess.STDOUT)
            try:
                output = subprocess.check_output(self.cmd, shell=True, stderr=subprocess.STDOUT)
            except subprocess.CalledProcessError as e:
                output = e.output       # ignore error and return the output
            delta = time.time() - start
            output = output.decode('utf-8')

            # determine IP, if any
            ip = None       # assume there was no DNS lookup
            if output.startswith('PING'):
                # possible successful ping
                left = output.find('(')
                right = output.find(')')
                if left != -1 and right != -1:
                    ip = output[left+1:right]

            # generate response string
            if 'cannot resolve' in output:
                # no DNS lookup
                response = 'DNS failure (%.4fs)' % delta
            elif '0 packets received' in output:
                response = 'Timeout (%.4fs)' % delta
            else:
                # successful ping
                response = 'Host is up (%.4fs)' % delta

            # put tuple onto result queue
            self.result_q.put((ip, self.host, response))

    # examine the extra args
    if 'timeout' in kwargs:
        timeout = kwargs['timeout']

    # prepare the result queue
    result_q = queue.Queue()

    workers = []

    # do a ping for each host in parallel
    for host in hosts:
        # create the 'ping' command
        cmd = ('ping -c 1 -t %d %s' % (timeout, host))

        # start a parallel worker to execute command
        worker = Worker(cmd, host, result_q)
        workers.append(worker)
        worker.start()

    # wait here for all workers to terminate
    for worker in workers:
        worker.join()

    # get results off the result queue
    result = []

    while not result_q.empty():
        response = result_q.get(block=False)
        result.append(response)

    return result


if __name__ == '__main__':
    import sys
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
            print('%-17s%-40s%s' % (str(ip) if ip else '', str(name), str(response)))
    else:
        print('No results')

