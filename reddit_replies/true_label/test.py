#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://www.reddit.com/r/learnpython/comments/5p8j55/i_need_a_way_to_create_a_search_system_for_a_list/
"""

from tkinter import *

window = Tk()

window.title("ListingExample")
window.geometry("200x100")

Listexample = 'STEAM_0:0:187162090 STEAM_0:0:18714757 STEAM_0:0:1897544' # example of a list

Textfield = Entry(window) # textfield to type something in (ex: STEAM_0:0:xxxxxxxxxx)
Textfield.pack()

Button1 = Button(window, text="Search")
Button1.pack()

Label1 = Label(text="xxxxxx") # True or False
Label1.pack()

mainloop()
