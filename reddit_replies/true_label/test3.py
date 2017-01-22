#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://www.reddit.com/r/learnpython/comments/5p8j55/i_need_a_way_to_create_a_search_system_for_a_list/

Enhanced version, including reply code.  Pastebin: http://pastebin.com/CWMnBtLL
"""

from tkinter import *
import random        # needed only for the fake 'my_search' function

# the animal 'database'
Animals = [
           'cat',
           'dog',
           'mouse',
           'python',
           'hamster'
          ]

def my_search(search_string):
    """Search for 'search_string' in Animals.

    Returns True if 'search_string' was found.
    """

    lower_str = search_string.lower()  # ensure the search string is lowercase
    if lower_str in Animals:
        return True
    return False

def button_press():
    """The user pressed a button."""

    # get search string and look for it
    search_string = Textfield.get()
    result = my_search(search_string)

    # convert True/False result into a string
    result_str = str(result)

    # put 'result_str' into the label text
    Label1.config(text=result_str)


window = Tk()

window.title("ListingExample")
window.geometry("200x100")

Textfield = Entry(window) # textfield to type something in (ex: STEAM_0:0:xxxxxxxxxx)
Textfield.pack()

Button1 = Button(window, text="Search", command=button_press)
Button1.pack()

Label1 = Label(text="xxxxxx") # True or False
Label1.pack()

mainloop()
