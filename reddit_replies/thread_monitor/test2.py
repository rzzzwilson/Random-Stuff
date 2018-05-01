#!/usr/bin/env python
#
#import ctypes
import io
import os
import random
import string
import sys
import time
import threading
from optparse import OptionParser

#libc = ctypes.CDLL("libc.so.6")

class FSWatch(threading.Thread):
    def __init__(self, destination, interval):
        threading.Thread.__init__(self)
        self.destination = destination
        self.interval = interval
        self.stats = {}
        self.state_id = 0

    def monitor(self):
        print "Starting FS Watcher monitor thread..."
        state_id = 0
        fail_count = 1

        while True:
            new_state_id = self.get_state()
            print "INFO: state_id: {0}, Time: {1}".format(state_id, time.time())
            if new_state_id == state_id:
                print "FAILURE: Worker has not finished. Fail count: {0}".format(fail_count)
                time.sleep(float(self.interval))
                fail_count += 1
                continue
            else:
                print "SUCCESS: stats: {0}".format(self.get_stats())
                state_id = new_state_id
                time.sleep(float(options.interval))
                fail_count = 1
        return

    def watch(self):
        print "Starting FS Watcher..."
        while True:
            # generate directory and file name
            directory_basename = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(8)])
            file_basename = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(8)])

            directory = os.path.join(self.destination, directory_basename)
            filename = os.path.join(directory, file_basename)
            buf = bytearray(1024 * 1024 * 1024)

            start_time = time.time()

            # Some file system checks

            overall_time = time.time() - start_time
            self.stats['overall_time'] = overall_time
            self.state_id += 1
            time.sleep(float(self.interval))

        return

    def get_stats(self):
        return self.stats

    def get_state(self):
        return self.state_id


def main(options, args):
    fswatcher = FSWatch(options.destination, options.interval)

    threads = []

    monitor_thread = threading.Thread(target=fswatcher.monitor)
    monitor_thread.start()
    threads.append(monitor_thread)

    watch_thread = threading.Thread(target=fswatcher.watch)
    watch_thread.start()
    threads.append(watch_thread)

    for t in threads:
        t.join()

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-d', '--destination', dest='destination', metavar='DIRECTORY', help='directory to run checks')
    parser.add_option('-i', '--interval', dest='interval', metavar='SECONDS', help='thread loop interval')

    options, args = parser.parse_args()

    for k, v in vars(options).iteritems():
        if v is None:
            print "Make sure you've set all of the command line options, which are mandatory."
            parser.print_help()
            sys.exit(1)

    main(options, args)
