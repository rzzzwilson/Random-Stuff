#!/usr/bin/env python3

'''
A small function to put an error message on the screen with Tkinter.

Used by GUI programs started from a desktop icon.
'''

import string
from tkinter import *


def tkinter_error(msg, title=None):
    """Show an error message in a Tkinter dialog.

    msg    text message to display (may contain newlines, etc)
    title  the window title (defaults to 'ERROR')

    The whole point of this is to get *some* output from a python GUI
    program when run from an icon double-click.  We use Tkinter since it's
    part of standard python and we may be trying to say something like:

        +-----------------------------+
        |  you must install wxPython  |
        +-----------------------------+

    Under Linux and OSX we can run the program from the commandline and we would
    see printed output.  Under Windows that's hard to do, hence this code.

    NOTE: For some reason, Ubuntu python doesn't have tkinter installed as
    part of the base install.  Do "sudo apt-get install python-tk".
    """

    ######
    # Define the Application class
    ######

    class Application(Frame):
        def createWidgets(self):
            self.LABEL = Label(self, text=self.text, font=("Courier", 14))
            self.LABEL["fg"] = "black"
            self.LABEL["bg"] = "yellow"
            self.LABEL["justify"] = "left"
            self.LABEL.pack()

        def __init__(self, text, master=None):
            self.text = text
            Frame.__init__(self, master)
            self.pack()
            self.createWidgets()
            self.tkraise()


    # set the title string
    if title is None:
        title = 'ERROR'

    # get the message text
    msg = '\n' + msg.strip() + '\n'

    msg = msg.replace('\r', '')
    msg = msg.replace('\n', '   \n   ')

    app = Application(msg)
    app.master.title(title)
    app.mainloop()


if __name__ == '__main__':
    tkinter_error('A short message:\n\tHello, world!\n\n'
                  'Some Unicode (広島, ภูเก็ต) and extended characters (\v\a\b).',
                  title='Test Error Message')
