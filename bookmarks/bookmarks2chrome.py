#!/usr/bin/env python3

"""
Convert a bookmarks data file to a Chrome HTML bookmarks file.

Usage: bookmarks2chrome.py <data file> <HTML file>

where <data file>    is the bookmarks data file to convert
where <HTML file>    is the path to the output Chrome HTML bookmarks file

The Chrome HTML bookmarks file format is one or more lines:

    path/to/bookmark@URL

where path/to/bookmark is a '/' delimited bookmark folder path with the last
                           element of the path being the bookmark title,
and   URL              is the associated bookmark URL
"""

indent_size = 3
indent = 0

def open_header(out):
    out.write('<!DOCTYPE NETSCAPE-Bookmark-file-1>\n')
    out.write('<!-- This is an automatically generated file.  It will be read and overwritten.  DO NOT EDIT! -->\n')
    out.write('<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">\n')
    out.write('<TITLE>Bookmarks</TITLE>\n')
    out.write('<H1>Bookmarks</H1>\n')

def open_folder(out, depth, folder):
    out.write('%s<DL>\n' % (' ' * (depth * indent_size)))
    out.write('%s<DT><H3>%s</H3>\n' % (' ' * (depth * (indent_size+1)), folder))

def close_folder(out, depth):
    out.write('%s</DL>\n' % (' ' * (depth * indent_size)))

def new_bookmark(out, depth, url, title):
    out.write('%s<DT><A HREF="%s">%s</A></DT>\n' % (' ' * (depth * indent_size), url, title))

def close_folder(out, depth):
    out.write('%s</DL>\n' % (' ' * (depth * indent_size)))

def get_list_common_prefix(a, b):
    """Get number of common prefix elements of two lists."""

    result = 0
    for (a_elt, b_elt) in zip(a, b):
        if a_elt != b_elt:
            break
        result += 1
    return result


def process_bookmarks(in_handle, out_handle):
    """Convert a bookmarks data file to a Google Chrome HTML bookmarks file.
    
    in_handle   handle of the open input file
    out_handle  handle of the open output file

    Returns an error status for sys.exit(): 0 means all OK.
    """

## test file with simple data
#/Bookmarks Bar/Daily/www.theguardian.com	https://www.theguardian.com/world
#/Bookmarks Bar/Daily/The Register: Sci/Tech News for the World	http://www.theregister.co.uk/
#/Bookmarks Bar/Daily/Physics	http://www.reddit.com/r/Physics/new
#/Bookmarks Bar/Daily/programming	http://www.reddit.com/r/programming/new
#/Bookmarks Bar/Daily/Hacker News	https://news.ycombinator.com/newest
#/Bookmarks Bar/Daily/µnit — C Unit Testing Framework	https://nemequ.github.io/munit/
#/Bookmarks Bar/Music/Classical music radio stations	http://www.listenlive.eu/classical.html
#/Bookmarks Bar/Music/ABC Classic FM - ABC Radio	https://radio.abc.net.au/stations/classic/live?play=true
#/Bookmarks Bar/Music/İTÜ Radyosu Klasik	http://eskiweb.radyo.itu.edu.tr/flash/klasik.html
#/Bookmarks Bar/Music/Classical radio	http://www.radio.net/genre/Classical/
#/Dilbert 	http://dilbert.com/

    result = 0

    # print the HTML header
    open_header(out_handle)

    # how deeply we are indented
    depth = 0

    # process each line in the input file
    prev_path = ''
    for (lnum, line) in enumerate(in_handle):
        line = line.strip()

        print(f'{lnum:02d}: {line}')

        # ignore comments
        if line.startswith('#'):
            continue

        # strip off leading '/'
        if line.startswith('/'):
            line = line[1:]

        # split into path/title/url
        try:
            (path, url) = line.split('\t')
        except ValueError:
            # bad split, report line
            print(f'line {lnum+1} has bad format: {line}')
            return 1

        (path, title) = os.path.split(path)
        path_list = path.split('/')
        print(f'{lnum:02d}: path={path}, path_list={path_list}, title={title}, url={url}')
        if path == prev_path:
            # link in same folder as previous
            new_bookmark(out_handle, depth, url, title)
#            out_handle.write(New_Bookmark % (' ' * depth * indent_size, url, title))
            pass
        else:
            # need to analyze situation.
            # if path an EXTENSION of previous, start new folder
            # if path shorter than previous, close N folders
            # else close all folders, open new set
            prev_path_list = prev_path.split('/')

            prefix_size = get_list_common_prefix(prev_path_list, path_list)
            if prefix_size == 0:
                # completely close all folders
                while depth > 1:
                    depth -= 1
#                    out_handle.write('%s</DL>\n' % (' ' * depth * indent_size))
                    close_folder(out_handle, depth)
                # open new folders
                for folder in path_list:
                    open_folder(out_handle, depth, folder)
                    depth += 1
            else:
                # close only a few folders
                for _ in prev_path_list[:prefix_size]:
                    depth -= 1
#                    out_handle.write('%s</DL>\n' % (' ' * depth * indent_size))
                    close_folder(out_handle, depth)
                for folder in path_list[prefix_size:]:
                    open_folder(out_handle, depth, folder)
                    depth += 1

#        if not prev_path:
#            # first folder, create new folder hierachy
#            div_path = path.split('/') # [1:]      # get split path, ignore first empty field
#            print(f'div_path={div_path}')
#            for folder in div_path:
#                out_handle.write(New_Folder % (" " * depth, folder))
#                depth += indent_size
#
#            # create first bookmark in new folder stack
#            out_handle.write(New_Bookmark % (" " * depth, url, title))
#        else:
#            # have previous path, anything in common?
#            prefix = os.path.commonpath([path, prev_path])
#            div_prefix = prefix.split('/')
#            div_prev = prev_path.split('/')
#            div_path = path.split('/')
#            if div_prefix == ['']:
#                div_prefix = []
#            if div_prev == ['']:
#                div_prev = []
#            if div_path == ['']:
#                div_path = []
#
#            if prefix == prev_path:
#                # possibly same folder or an increase on previous
#                if path != prev_path:
#                    # increase, make new folder(s)
#                    for folder in div_path[len(div_prev):]:
#                        out_handle.write(New_Folder % (" " * depth, folder))
#                        depth += indent_size
#                # add new bookmark
#                out_handle.write(New_Bookmark % (" " * depth, url, title))
#            else:
#                # new folder, unwind back to common prefix (which may be empty)
#                while div_prev != div_prefix:
#                    # close one folder
#                    depth -= indent_size
#                    out_handle.write(End_Folder % (" " * depth))
#                    if div_prev:
#                        del div_prev[-1]
#                # add new folder(s)
#                for folder in div_path[len(prefix):]:
#                    out_handle.write(New_Folder % (" " * depth, folder))
#                    depth += indent_size
#                # add new bookmark
#                out_handle.write(New_Bookmark % (" " * depth, url, title))

        # remember the last path
        prev_path = path

    # close outstanding folders
    while depth > 0:
        depth -= 1
        close_folder(out_handle, depth)

    # print the HTML footer
#    out_handle.write(HTML_Footer)

    return result


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
