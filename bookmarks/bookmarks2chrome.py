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

HTML_Header = """<!DOCTYPE NETSCAPE-Bookmark-file-1>
<!-- This is an automatically generated file.
     It will be read and overwritten.
     DO NOT EDIT! -->
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks</H1>
<DL><p>
"""

HTML_Footer = """</DL><p>\n"""

New_Folder = """%s<DT><H3>%s</H3><DL><p>\n"""

End_Folder = """%s</DL><p>\n"""

New_Bookmark = """<DT><A HREF="%s">%s</A>\n"""

indent_size = 4


def process_bookmarks(in_handle, out_handle):
    """Convert a bookmarks data file to a Google Chrome HTML bookmarks file.
    
    in_handle   handle of the open input file
    out_handle  handle of the open output file

    Returns an error status for sys.exit(): 0 means all OK.
    """

    result = 0

    # print the HTML header
    out_handle.write(HTML_Header)

    # how deep we are in folders
    depth = 0

    # process each line in the input file
    prev_path = ''
    for (lnum, line) in enumerate(in_handle):
        line = line.strip()
        if line.startswith('#'):
            print(f'Ignoring: {line}')
            continue

        print('###########################################')
        print(f'line: {line}')
        try:
            (path, url) = line.strip().split('@')
        except ValueError:
            # bad split, report line
            print(f'line {lnum+1} has bad format: {line}')
            return 1

        # split path into path + title
        (path, title) = os.path.split(path)
        if not path:
            # MUST have something in path
            print(f'line {lnum+1} has bad format: {line}')
            return 1

        print(f'prev_path={prev_path}, path={path}, title={title}, url={url}')

        if not prev_path:
            # first folder, create new folder hierachy
            div_path = path.split('/')      # get split path
            for folder in div_path:
                out_handle.write(New_Folder % (" " * depth, folder))
                depth += indent_size

            # create first bookmark in new folder stack
            out_handle.write(f'{" " * depth}<DT><A HREF="{title}">{url}</A>\n')
        else:
            # have previous path, anything in common?
            prefix = os.path.commonpath([path, prev_path])
            print(f'prefix={prefix}, prev_path={prev_path}')
            if prefix == prev_path:
                # same folder, so just add new bookmark
                out_handle.write(f'{" " * depth}<DT><A HREF="{title}">{url}</A>\n')
            else:
                # new folder, unwind back to common prefix (which may be empty)
                div_prefix = prefix.split('/')
                div_prev = prev_path.split('/')
                while div_prev != div_prefix:
                    print(f'loop: div_prev={div_prev}, div_prefix={div_prefix}')
                    # close one folder
                    depth -= indent_size
                    out_handle.write(End_Folder % (" " * depth))
                    if div_prev:
                        del div_prev[-1]
                # add new folder(s)
                for folder in div_path[len(prefix):]:
                    out_handle.write(New_Folder % (" " * depth, folder))
                    depth += indent_size
                # add new bookmark
                out_handle.write(f'{" " * depth}<DT><A HREF="{title}">{url}</A>\n')

        # remember the last path
        prev_path = path

    # close outstanding folders
    while depth > 0:
        print(f'loop, depth={depth}')
        depth -= indent_size
        out_handle.write(End_Folder % (" " * depth))

    # print the HTML footer
    out_handle.write(HTML_Footer)

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
