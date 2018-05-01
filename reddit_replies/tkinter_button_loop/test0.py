#!/usr/bin/env python2
from Tkinter import *
import datetime

this_year = datetime.datetime.now().year

class TxLedGui:
    def __init__(self, master):
        self.master = master

        master.title("TxLED Reporting")

        # Date range selection in the form of quarterly options and year entry
        Label(master, text="Quarter:", width=10, anchor=W).grid(row=0, column=0)

        self.quarter = StringVar(master)
        self.quarter.set("Q1 (Jan 1 - Mar 31)")

        self.quarter_options = ["Q1 (Jan 1 - Mar 31)", "Q2 (Apr 1 - Jun 30)",
                                "Q3 (Jul 1 - Sep 30)", "Q4 (Oct 1 - Dec 31)"]

        self.quarter_select = OptionMenu(master, self.quarter, *self.quarter_options)

        self.quarter_select.grid(row=1, column=0)

        Label(master, text="Year:", width=10).grid(row=0, column=1)
        self.year_entry = Entry(master)
        self.year_entry.insert(END, this_year)

        self.year_entry.grid(row=1, column=1)
        # End date range selection

        # DB Credentials
        Label(master, text="DB User:").grid(row=2, column=0)
        Label(master, text="DB Pass:").grid(row=2, column=1)

        self.user_entry = Entry(master)
        self.user_entry.grid(row=3, column=0)

        self.pass_entry = Entry(master, show='*')
        self.pass_entry.grid(row=3, column=1)
        # End DB Creds

        # Button to start process
        Button(master, text="Generate Report", command=self.gen_report).grid(row=4, column=1)

    def gen_report(self):

        print "working"


root = Tk()
txledgui = TxLedGui(root)
root.mainloop()
