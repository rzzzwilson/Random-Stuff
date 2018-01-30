import sys
import argparse

parser = argparse.ArgumentParser(description='A thing I wrote.', add_help=False)
parser.add_argument('-w', '--warning', type=float, required=True)
parser.add_argument('-c', '--critical', type=float, required=True)
parser.add_argument('--version', action='version', version='version 0.1')
parser.add_argument('-h', '--help', action='help')

try:
    args = parser.parse_args()
except:
    print "Error: command line option values unexpected"
    sys.exit(3)

