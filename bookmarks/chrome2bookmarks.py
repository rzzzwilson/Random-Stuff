#!/usr/bin/env python3

"""
Convert Chrome HTML bookmarks to a data file format.

Usage: chrome2bookmarks.py <HTML file> [<output file>]

where <HTML file>    is the path to the required Chrome HTML bookmarks file
and   <output file>  is the path to the output file to write data to
                     (optional, use stdout if not supplied)

The data file format consists of multiple lines of:
    bookmark_path\tURL
where the "bookmark_path" is like "Bookmarks Bar/Daily/The Guardian".
The last "file" in the "bookmark_path" is the bookmark name.  Preceding
"files" are folder names.
"""

from html.parser import HTMLParser

class HTML2JSON(HTMLParser):
    """A class to parse HTML and return a bookmark data structure.

    The data structure is a list of tuples:
        (<bookmark path>, <URL>)

    Uses a state machine to parse the Chrome bookmarks HTML data.
    """

    # internal states
    GotDT = 1       # got DT start tag
    GotDTA = 2      # got DT then A
    GotDTH3 = 3     # got DT then H3
    GotNone = 4     # got something else

    def __init__(self):
        super().__init__()
        self.state = HTML2JSON.GotNone
        self.bookmarks = []
        self.path_stack = ['']

    def handle_starttag(self, tag, attrs):
        self.url = None
        if tag == 'dt':
            self.state = HTML2JSON.GotDT
        elif tag == 'h3':
            # start of a folder title, maybe
            if self.state == HTML2JSON.GotDT:
                # new bookmark folder
                self.state = HTML2JSON.GotDTH3
        elif tag == 'a':
            # start of a bookmark name+URL
            if self.state == HTML2JSON.GotDT:
                # new bookmark item
                self.state = HTML2JSON.GotDTA
                self.url = None
                for (tag, value) in attrs:
                    if tag == 'href':
                        self.url = value
                        break
        else:
            self.state == HTML2JSON.GotNone

    def handle_endtag(self, tag):
        if tag == 'h3':
            if self.state == HTML2JSON.GotDTH3:
                self.state = HTML2JSON.GotDT
        elif tag == 'a':
            if self.state == HTML2JSON.GotDTA:
                self.state = HTML2JSON.GotDT
        elif tag == 'dl':
            # end of bookmark folder, restore previous dictionary
            self.path_stack.pop()
            self.state = HTML2JSON.GotNone
        else:
            self.state = HTML2JSON.GotNone

    def handle_data(self, data):
        if self.state == HTML2JSON.GotDTH3:
            # new folder name added to path
            self.path_stack.append(data)
        elif self.state == HTML2JSON.GotDTA:
            # create new bookmark
            bmark = ('/'.join(self.path_stack+[data]), self.url)
            self.bookmarks.append(bmark)

    def get_bookmarks(self):
        return self.bookmarks

def process_bookmarks(bmark_file):
    """Process an HTML bookmarks file and produce a dictionary of bookmarks."""

    parser = HTML2JSON()
    with open(bmark_file) as f:
        text = f.read()
    parser.feed(text)
    return parser.get_bookmarks()

if __name__ == '__main__':
    import sys
    import getopt
    import traceback
    from pprint import pprint

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

    if len(args) not in (1, 2):
        usage()
        sys.exit(1)

    input_file = args[0]

    output_filehandle = sys.stdout
    if len(args) == 2:
        output_file = args[1]
        output_filehandle = open(output_file, 'w')

    # process the HTML bookmarks file
    bookmarks = process_bookmarks(input_file)
    for (path, url) in bookmarks:
        output_filehandle.write(f'{path}\t{url}\n')

    if output_filehandle != sys.stdout:
        output_filehandle.close()
