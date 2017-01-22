#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://www.reddit.com/r/learnpython/comments/5p8j55/i_need_a_way_to_create_a_search_system_for_a_list/

Enhanced version, including reply code.  Pastebin: http://pastebin.com/ymfDtDqV
"""

from tkinter import *
import random        # needed only for the fake 'my_search' function

def my_search(search_string):
    """Search for 'search_string' in <something>.

    Returns True if 'search_string' was found.

    Change the code here to do an actual search.
    For the moment, we just return a random True/False.
    """

    if random.random() < 0.5:
        return False
    return True

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

Listexample = 'STEAM_0:0:187162090 STEAM_0:0:18714757 STEAM_0:0:1897544' # example of a list

Textfield = Entry(window) # textfield to type something in (ex: STEAM_0:0:xxxxxxxxxx)
Textfield.pack()

Button1 = Button(window, text="Search", command=button_press)
Button1.pack()

Label1 = Label(text="xxxxxx") # True or False
Label1.pack()

mainloop()
