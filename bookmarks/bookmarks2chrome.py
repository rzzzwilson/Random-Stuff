#!/usr/bin/env python3

"""
Convert a bookmarks data file to a Chrome HTML bookmarks file.

Usage: bookmarks2chrome.py <data file> <HTML file>

where <data file>    is the bookmarks data file to convert
where <HTML file>    is the path to the output Chrome HTML bookmarks file

The Chrome HTML bookmarks file format is that produced by the Chrome
"export bookmarks" function.
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

HTML_Footer = """</DL><p>"""

New_Folder = """<DT><H3>FOLDERNAME_PLACE</H3>
<DL><p>
"""

End_Folder = """</DL><p>"""

New_Bookmark = """<DT><A HREF="HREF_PLACE">NAME_PLACE</A>
"""


def process_bookmarks(in_handle, out_handle):
    """Convert a bookmarks data file to a Google Chrome HTML bookmarks file.
    
    in_handle   handle of the open input file
    out_handle  handle of the open output file

    Returns an error status for sys.exit(): 0 means all OK.
    """

    result = 0

    # print the HTML header
    out_handle.write(HTML_Header)

    # set indent for first bookmark
    indent_count = 4
    indent = ' ' * indent_count

    # process each line in the input file
    prev_path = None
    for (lnum, line) in enumerate(in_handle):
        print(f'line: {line}')
        try:
            (path, url) = line.strip().split('\t')
        except ValueError:
            # bad split, report line
            print(f'line {lnum+1} has bad format: {line}')
            return 1

        # split path into path + bookmark
        (path, bookmark) = os.path.split(path)
        if not path:
            # MUST have something in path
            print(f'line {lnum+1} has bad format: {line}')
            return 1

        print(f'path={path}, bookmark={bookmark}')

        if path != prev_path:
            # change in folder, get divided paths
            div_path = path.split('/')
            if prev_path is None:
                div_prev_path = []
            else:
                div_prev_path = prev_path.split('/')
            print(f'div_path={div_path}, div_prev_path={div_prev_path}')
            print(f'prev_path={prev_path}, div_prev_path={div_prev_path}')

            while len(div_path) < len(div_prev_path):
                print('Deleting older deep paths')
                # close one or more folders
                indent_count -= 4
                indent = ' ' * indent_count
                out_handle.write(f'{indent}{End_Folder}\n')
                del div_prev_path[-1]

            while div_prev_path and (div_path != div_prev_path):
                print('Close one or more folders')
                # close one or more folders
                indent_count -= 4
                indent = ' ' * indent_count
                out_handle.write(f'{indent}{End_Folder}\n')
                del div_prev_path[-1]
                del div_path[-1]

        else:
            # next bookmark in this folder
            out_handle.write(f'{indent}<DT><A HREF="{url}">{bookmark}</A>\n')

        # remember the last path
        prev_path = path

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
