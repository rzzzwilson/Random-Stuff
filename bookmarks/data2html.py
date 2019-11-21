#!/usr/bin/env python3

"""
Convert a bookmarks data file to a Chrome HTML bookmarks file.

Usage: data2html.py <data file> <HTML file>

where <data file>    is the bookmarks data file to convert
where <HTML file>    is the path to the output Chrome HTML bookmarks file

The Chrome HTML bookmarks file format is one or more lines:

    path/to/bookmark\tURL

where path/to/bookmark is a '/' delimited bookmark folder path with the last
                           element of the path being the bookmark title,
and   URL              is the associated bookmark URL
"""

import sys
from pprint import pprint


# any folder path with this at the start has it removed
IgnorePrefix = 'Bookmarks Bar/'

# if these strings appear in a URL, ignore the bookmark
BadUrlList = ['ps.reddit', 'old.reddit']


indent_size = 3
indent = 0

def open_header(out):
    out.write('<!DOCTYPE NETSCAPE-Bookmark-file-1>\n')
    out.write('<!-- This is an automatically generated file.  It will be read and overwritten.  DO NOT EDIT! -->\n')
    out.write('<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">\n')
    out.write('<TITLE>Bookmarks</TITLE>\n')
    out.write('<H1>Bookmarks</H1>\n')
    out.write('<DL>\n')

def close_header(out):
    out.write('</DL>\n')

def open_folder(out, depth, folder):
    out.write('%s<DT><H3>%s</H3>\n' % (' ' * (depth * indent_size), folder))
    out.write('%s<DL>\n' % (' ' * (depth * indent_size)))

def close_folder(out, depth):
    out.write('%s</DL>\n' % (' ' * (depth * indent_size)))
    out.write('%s</DT>\n' % (' ' * (depth * indent_size)))

def new_bookmark(out, depth, url, title):
    out.write('%s<DT><A HREF="%s">%s</A></DT>\n' % (' ' * (depth * indent_size), url, title))

def get_line_data(lnum, line):
    """Parse line and return (path_list, title, url)."""

    # strip off leading '/'
    if line.startswith('/'):
        line = line[1:]

    # split into path/title/url
    try:
        (path, url) = line.split('\t')
    except ValueError:
        # bad split, report line
        print(f'line {lnum+1} has bad format: {line}')
        sys.exit(1)

    (path, title) = os.path.split(path)

    # remove the "IgnorePrefix" it it's there
    if path.startswith(IgnorePrefix):
        path = path[len(IgnorePrefix):]

    if path:
        path_list = path.split('/')
    else:
        path_list = []

    return (path_list, title, url)

def dump_dict(out, root, depth=1):
    """Dump "root" dict to "out" file-like object."""

    # dump folders first
    for (key, value) in root.items():
        if isinstance(value, dict):
            # folder
            open_folder(out, depth, key)
            dump_dict(out, value, depth+1)
            close_folder(out, depth)

    # then dump bookmarks
    for (key, marks) in root.items():
        if not isinstance(value, dict):
            # simple bookmark, dump one or more bookmarks
            for value in marks:
                for bad_url in BadUrlList:
                    if bad_url in value:
                        continue
                new_bookmark(out, depth, value, key)

def process_bookmarks(in_handle, out_handle):
    """Convert a bookmarks data file to a Google Chrome HTML bookmarks file.
    
    in_handle   handle of the open input file
    out_handle  handle of the open output file

    Returns an error status for sys.exit(): 0 means all OK.
    """

    # process each line in the input file
    root = {}
    prev_path = ''
    for (lnum, line) in enumerate(in_handle):
        # get line into canonical form
        line = line.strip()

        # ignore comments
        if line.startswith('#'):
            continue

        # get (path_list, title, url) from line
        (path_list, title, url) = get_line_data(lnum, line)

        # using path_list, step through 'root' dict to find appropriate place
        current = root
        while path_list:
            path = path_list.pop(0)
            if path not in current:
                current[path] = {}
            current = current[path]

        # create new bookmark at the appropriate place
        if title not in current:
            # no bookmark yet, create empty list
            current[title] = []

        # append new url to value list
        current[title].append(url)

    # now walk through "root" creating HTML as we go
    open_header(out_handle)
    dump_dict(out_handle, root)
    close_header(out_handle)

    return 0


if __name__ == '__main__':
    import sys
    import os
    import getopt
    import traceback

    # to help the befuddled user
    def usage(msg=None):
        if msg:
            print(('*'*80 + '\n%s\n' + '*'*80) % msg)
        print(__doc__)

    # a function to report errors
    def error(msg):
        print(msg)
        sys.exit(1)

    # our own handler for uncaught exceptions
    def excepthook(type, value, tb):
        msg = '\n' + '=' * 80
        msg += '\nUncaught exception:\n'
        msg += ''.join(traceback.format_exception(type, value, tb))
        msg += '=' * 80 + '\n'
        print(msg)

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

    if len(args) != 2:
        usage()
        sys.exit(1)

    input_file = args[0]
    output_file = args[1]

    # check that the input file exists
    try:
        input_handle = open(input_file)
    except FileNotFoundError:
        error(f"File '{input_file}' doesn't exist?")

    # prepare the output file, don't overwrite if it already exists
    if os.path.isfile(output_file) or os.path.isdir(output_file):
        error(f"Sorry, won't overwrite existing file '{output_file}'.")

    try:
        output_handle = open(output_file, 'w')
    except PermissionError:
        error(f"Sorry, permissions error creating '{output_file}'.")
    except FileNotFoundError:
        error(f"Name not found in the given path: '{output_file}'.")
    except:
        raise

    # process the HTML bookmarks file
    result = process_bookmarks(input_handle, output_handle)

    # close files and exit
    input_handle.close()
    output_handle.close()
    sys.exit(result)
