#!/bin/env python
# -*- coding: utf-8 -*-

"""
This is a program to solve the Google Code Jam "File Fixit" puzzle:
    https://code.google.com/codejam/contest/635101/dashboard#s=p0

Usage: file_fixit <input_file>
"""

class Node(object):

    def __init__(self, name):
        self.name = name
        self.sub_dirs = []

    def add_dir(self, name):
        self.sub_dirs.append(Node(name))

def print_dirs(root, indent=0):
    """Debug routine to print a directory structure."""

    str_indent = ' ' * indent

    if root:
        print('%s%s' % (str_indent, root.name))

        for sd in root.sub_dirs:
            print_dirs(sd, indent=indent+4)

def get_mkdirs(given, reqd):
    """Solve the File File problem.

    given  list of given directory paths
    reqd   list of required directory paths

    Return the number of 'mkdir' commands executed (can be 0).
    """

#    print('get_mkdirs: given=%s' % str(given))
#    print('get_mkdirs: reqd=%s' % str(reqd))

    # create the empty directory tree
    root = Node('/')
#    print('Before:')
#    print_dirs(root)

    # decorate the tree with the given directories
    for path in given:
        sub_dirs = path.split('/')
        sub_dirs = sub_dirs[1:]             # drop first, as we start with '/'
#        print('given sub_dirs=%s' % str(sub_dirs))

        node_ptr = root
        for name in sub_dirs:
            found = False
            for child in node_ptr.sub_dirs:
                if name == child.name:
                    # we have this dir already
                    node_ptr = child
                    found = True
            if not found:
                # have to create child directory
                new_node = Node(name)
                node_ptr.sub_dirs.append(new_node)
                node_ptr = new_node

#    print('After:')
#    print_dirs(root)

    # now we take the required directories and add them to the tree, counting 'mkdir'
    # this code is similar to that above where we added given directories
    result = 0

    for path in reqd:
        sub_dirs = path.split('/')
        sub_dirs = sub_dirs[1:]             # drop first, as we start with '/'
#        print('reqd sub_dirs=%s' % str(sub_dirs))

        node_ptr = root
        for name in sub_dirs:
            found = False
            for child in node_ptr.sub_dirs:
                if name == child.name:
                    # we have this dir already
                    node_ptr = child
                    found = True
            if not found:
                # have to create child directory
                result += 1
                new_node = Node(name)
                node_ptr.sub_dirs.append(new_node)
                node_ptr = new_node

    return result

def main(input_file):
    """Solve the File Fixit problem.

    input_file  the input data file

    The solution is written to standard output:
        Case #x: y
    where x is the case number, and
          y is the number of intersection points (you see).
    """
    
    # read file into memory, removing trailing '\n'
    with open(input_file, 'rb') as handle:
        l = handle.readlines()
    lines = [ll.strip() for ll in l]

    # gather each test case, solve
    num_cases = int(lines[0])
    lines = lines[1:]

    for case in range(num_cases):
        num_given_reqd = lines[0]
        lines = lines[1:]

        (num_given, num_reqd) = num_given_reqd.split()
        num_given = int(num_given)
        num_reqd = int(num_reqd)

        given = lines[:num_given]
        reqd = lines[num_given:num_given+num_reqd]
        lines = lines[num_given+num_reqd:]
        num_mkdirs = get_mkdirs(given, reqd)

        print('Case #%d: %d' % (case+1, num_mkdirs))
#        print('-'*80)

    return 0

##############################################################################

if __name__ == '__main__':
    import sys
    import getopt
    import traceback

    # to help the befuddled user
    def usage(msg=None):
        if msg:
            print(('*'*80 + '\n%s\n' + '*'*80) % msg)
        print(__doc__)

    # our own handler for uncaught exceptions
    def excepthook(type, value, tb):
        msg = '\n' + '=' * 80
        msg += '\nUncaught exception:\n'
        msg += ''.join(traceback.format_exception(type, value, tb))
        msg += '=' * 80 + '\n'
        print(msg)
        sys.exit(1)

    # plug our handler into the python system
    sys.excepthook = excepthook

    # parse the CLI params
    argv = sys.argv[1:]

    try:
        (opts, args) = getopt.getopt(argv, 'h', ['help'])
    except getopt.error:
        usage()
        sys.exit(1)

    for (opt, param) in opts:
        if opt in ['-h', '--help']:
            usage()
            sys.exit(0)

    # check for the input file
    if len(args) != 1:
        usage()
        sys.exit(1)
    input_file = args[0]

    # run the program code
    result = main(input_file)
    sys.exit(result)

