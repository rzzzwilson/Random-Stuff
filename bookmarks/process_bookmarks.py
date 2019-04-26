#!/usr/bin/env python3

"""
Convert HTML bookmarks to a JSON format.

where a dictionary is a collection of bookmark folders,
a dictionary key is the name of a bookmark folder,
and the dictionary value is either another dictionary or
a list of bookmark items: (name, URL).

Usage: bookmarks.py <HTML file> [<output file>]

where <HTML file>    is the path to the required HTML bookmarks file
and   <output file>  is the path to the output file to write data to
                     (optional, use stdout if not supplied)
"""

"""
Format of output is:

{'title1': [('title1_1', 'url1_1'),
            ('title1_2', 'url1_2'),
            ...
           ],
 'title2': {'title2_1': [(,), ..., (,)],
            'title2_2': {'url2_2': ...,
                         ...
                        },
            ...
           },
 ...
}
"""

from html.parser import HTMLParser

html_file = 'bookmarks_3_22_19.html'

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
        self.folder_stack = []

    def handle_starttag(self, tag, attrs):
        self.url = None
        if tag == 'dt':
            self.state = HTML2JSON.GotDT
        elif tag == 'h3':
            # start of a folder title, maybe
            if self.state == HTML2JSON.GotDT:
                print(f'start DT/H3: attrs={attrs}')
                # new bookmark folder
                self.state = HTML2JSON.GotDTH3
        elif tag == 'a':
            # start of a bookmark name+URL
            if self.state == HTML2JSON.GotDT:
                print(f'start DT/A: attrs={attrs}')
                # new bookmark item
                self.state = HTML2JSON.GotDTA
                self.url = None
                for (tag, value) in attrs:
                    print(f'tag={tag}, value={value}')
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
        else:
            self.state = HTML2JSON.GotNone

    def handle_data(self, data):
        if self.state == HTML2JSON.GotDTH3:
            print(f'data DT/H3: creating new folder: {data}')
            # new bookmark folder
            self.folder_stack.append(self.current_folder)
            new_folder = {}
            self.current_folder[data] = new_folder
            self.current_folder = new_folder

        elif self.state == HTML2JSON.GotDTA:
            print(f'data DT/A: creating new bookmark: {data}: {self.url}')
            # create new bookmark
            self.current_folder[data] = self.url

    @property
    def json(self):
        return self.bookmarks
#        return json.dumps(self.bookmarks, indent=4)

    def get_bookmarks(self):
        return self.bookmarks

def process_bookmarks(bmark_file):
    """Process an HTML bookmarks file and produce JSON dictionary."""

    pass


parser = HTML2JSON()
with open(html_file) as f:
    text = f.read()
parser.feed(text)
d = parser.get_bookmarks()
print('='*80)
print(f'len(d)={len(d)}')
for (k, v) in d.items():
    print(f'{k}: {v}')
#print(parser.json)
#for (k, v) in parser.json.items():
#    print(f'{k}: {v}')


if __name__ == '__main__':
    import sys
    import argparse
    import json

    # parse the CLI parameters

    # process the HTML file
    process_bookmarks(input_file, output_file)
