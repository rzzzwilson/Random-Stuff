#!/usr/bin/env python3

"""
An example of limiting a path length for display in a widget.

This is for UNIX-like filesystems.  On Windows would need extra code to
handle the drive.
"""

import sys
import os
from tkinter import Frame, Tk, Button, Label, StringVar
from tkinter import LEFT, RIGHT, BOTTOM, TOP, W
from tkinter import filedialog


LabelWidth = 60


def limit_path(path, limit):
    """Limit a path to 'limit' characters."""

    # decide if we need to limit path string length
    if len(path) <= limit:
        return path

    # split path into list of directories/file
    path_list = []
    while True:
        (head, tail) = os.path.split(path)
        if not tail:
            break
        path_list.insert(0, tail)
        path = head

    # create the default path 'head' plus terminal file
    # for Windows we would look for the drive letter
    head_path = os.path.join('/', path_list.pop(0), '...')
    tail_path = path_list.pop()
    result = os.path.join(head_path, tail_path)

    # add extra tail directories until limited path too long
    while path_list:
        new_tail_path = os.path.join(path_list.pop(), tail_path)
        new_result = os.path.join(head_path, new_tail_path)
        if len(new_result) > limit:
            break
        tail_path = new_tail_path
        result = new_result

    return result


class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.fdialog = Button(master=frame, text="File", command=self.get_file)
        self.fdialog.pack()

        self.lab_text = StringVar()
        self.lab_text.set('')
        self.label = Label(textvariable=self.lab_text, width=LabelWidth, anchor=W, justify=LEFT)
        self.label.pack()

        root.resizable(width=False, height=False)

    def get_file(self):
        name = filedialog.askopenfilename(title = "Choose a file.")
        if name != '':
            self.lab_text.set(limit_path(name, LabelWidth))


root = Tk()
app = App(root)
root.mainloop()
sys.exit(0)

def main():
    return 0

if __name__ == "__main__":
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

    sys.exit(main())
