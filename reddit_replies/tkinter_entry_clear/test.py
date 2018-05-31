#!/usr/bin/env python3

"""
Clear an Entry field upon Enter.

https://old.reddit.com/r/learnpython/comments/8m4121/how_do_i_clear_whatever_is_inside_a_tkentry_when/
"""

import sys
from tkinter import Tk, Frame, Entry, LEFT

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.entry = Entry(frame)
        self.entry.pack(side=LEFT)

        self.entry.bind('<Return>', self.on_click)

    def on_click(self, event):
        print('ENTER')
        self.entry.delete(0, 'end')


# start the whole thing
root = Tk()
app = App(root)
root.mainloop()
