#!/usr/bin/env python3

"""
Convert HTML bookmarks to a JSON format.

Usage: bookmarks.py <HTML file> [<output file>]

where <HTML file>    is the path to the required HTML bookmarks file
and   <output file>  is the path to the output file to write data to
                     (optional, use stdout if not supplied)
"""

"""
Format of output is:

{'title1': url1_1,
 'title2': {'title2_1': url2_1,
            'title2_2': {'url2_2': url2_2,
                         ...
                        },
            ...
           },
 ...
}

Where the dictionary is a collection of bookmarks, a dictionary key is either
the name of a bookmark folder or the title of a bookmark, and the dictionary
value is either another dictionary (for a folder) or a URL (for a bookmark).
"""

from html.parser import HTMLParser

# class to parse HTML and return a bookmark dictionary
class HTML2JSON(HTMLParser):
    # internal states
    GotDT = 1       # got DT start tag
    GotDTA = 2      # got DT then A
    GotDTH3 = 3     # got DT then H3
    GotNone = 4     # got something else

    IndentSpaces = 4

    def __init__(self):
        super().__init__()
        self.state = HTML2JSON.GotNone
        self.current_folder = {}
        self.bookmarks = self.current_folder
        self.folder_stack = [self.current_folder]

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
            self.current_folder = self.folder_stack.pop()
            self.state = HTML2JSON.GotNone
        else:
            self.state = HTML2JSON.GotNone

    def handle_data(self, data):
        if self.state == HTML2JSON.GotDTH3:
            # new bookmark folder
            new_folder = {}
            self.current_folder[data] = new_folder
            self.folder_stack.append(self.current_folder)
            self.current_folder = new_folder
        elif self.state == HTML2JSON.GotDTA:
            # create new bookmark
            self.current_folder[data] = self.url

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

    if len(args) != 1:
        usage()
        sys.exit(1)

    input_file = args[0]

    # process the HTML bookmarks file
    bookmarks = process_bookmarks(input_file)
#    pprint(bookmarks)
    for (k, v) in bookmarks.items():
        if isinstance(v, dict):
            print(f"{k}: folder")
        else:
            print(f"{k}: {v}")

