import sys
import argparse
from multiprocessing import Process

def main():
    parser = argparse.ArgumentParser(description='A thing I wrote.', add_help=False)
    parser.add_argument('-w', '--warning', type=float, required=True)
    parser.add_argument('-c', '--critical', type=float, required=True)
    parser.add_argument('--version', action='version', version='version 0.1')
    parser.add_argument('-h', '--help', action='help')

    args = parser.parse_args()
    print "args=%s" % str(args)
    sys.exit(0)

p = Process(target=main)
p.start()
p.join()
if p.exitcode == 2:
    print "Error: command line option values unexpected"
    sys.exit(3)
