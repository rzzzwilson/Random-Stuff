#!/usr/bin/env python3

"""
A template to start tkinter applications.

Usage: template_kinter [-d <debuglevel>] [-h]

Mostly copied from [http://effbot.org/tkinterbook/tkinter-hello-again.htm].
"""

import sys
import os
import getopt
import traceback
from tkinter import Tk, Frame, Button, LEFT


class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print('hi there, everyone!')

def main(debug):
    print(f'main: debug={debug}')
    root = Tk()
    app = App(root)
    root.mainloop()
    return 0

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
    tkinter_error(msg)

# plug our handler into the python system
sys.excepthook = excepthook

# parse the program params
argv = sys.argv[1:]

try:
    (opts, args) = getopt.getopt(argv, 'd:h', ['debug=', 'help'])
except getopt.GetoptError as err:
    usage(err)
    sys.exit(1)

debug = 10              # no logging

for (opt, param) in opts:
    if opt in ['-d', '--debug']:
        try:
            debug = int(param)
        except ValueError:
            usage("-d must be followed by an integer, got '%s'" % param)
            sys.exit(1)
    elif opt in ['-h', '--help']:
        usage()
        sys.exit(0)

# start the whole thing
sys.exit(main(debug))
