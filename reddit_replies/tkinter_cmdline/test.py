#!/usr/bin/env python3

"""
A small program to investigate mixing tkinter code and pre-existing
commandline code.  Inspired by this reddit post:

https://www.reddit.com/r/learnpython/comments/7bnvw9/mixing_command_line_and_tkinter_inputoutput/

The idea is to write a commandline cwprogramcode that takes a string and does
a ROT13 translation on it.  Then write a tkinter program that will execute
the commandline program passing the string to translate to STDIN and
reading SDTOUT and placing the translated text into a widget for display.
"""

from tkinter import *
from subprocess import Popen, PIPE, STDOUT


def do_cmdline(cmd, text):
    """Execute program in 'cmd' and pass 'text' to STDIN.
    Returns STDOUT output.

    Code from: https://stackoverflow.com/questions/8475290/how-do-i-write-to-a-python-subprocess-stdin

    Note that any prompt the program writes is included in STDOUT.
    """

    process = Popen([cmd], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    result = process.communicate(input=bytes(text, 'utf-8'))[0].decode('utf-8') 
    return result.strip()


class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.plain = Entry(frame, width=30)
        self.plain.pack()

        self.translate = Button(frame, text="ROT13", command=self.do_rot13)
        self.translate.pack()

        self.rot13 = Entry(frame, width=30)
        self.rot13.pack()
        self.rot13.config(state='disabled')

    def do_rot13(self):
        # get the text we have to ROT13
        plaintext = self.plain.get()

        # use the commandline program to do the translation
        rot13text = do_cmdline('./rot13.py', plaintext)

        # strip off the prompt stuff
        (_, rot13text) = rot13text.split(': ')

        # update the ROT13 display
        self.rot13.config(state='normal')
        self.rot13.delete(0, END)
        self.rot13.insert(0, rot13text)
        self.rot13.config(state='disabled')
        

root = Tk()
app = App(root)
root.mainloop()
