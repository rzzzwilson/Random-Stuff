#!/usr/bin/env python2
from Tkinter import *
import datetime

this_year = datetime.datetime.now().year

class TxLedGui:
    def __init__(self, master):
        self.master = master
        master.title("TxLED Reporting")

        frame = Frame(master)
        frame.pack()

        # Date range selection in the form of quarterly options and year entry
        lbl = Label(frame, text="Quarter:")
        lbl.grid(row=0, column=0, sticky=E)

        self.quarter = StringVar(frame)
        self.quarter.set("Q1 (Jan 1 - Mar 31)")

        self.quarter_options = ["Q1 (Jan 1 - Mar 31)", "Q2 (Apr 1 - Jun 30)",
                                "Q3 (Jul 1 - Sep 30)", "Q4 (Oct 1 - Dec 31)"]

        self.quarter_select = OptionMenu(frame, self.quarter, *self.quarter_options)
        self.quarter_select.grid(row=0, column=1)

        lbl = Label(frame, text="Year:")
        lbl.grid(row=1, column=0, sticky=E)

        self.year_entry = Entry(frame)
        self.year_entry.insert(END, this_year)
        self.year_entry.grid(row=1, column=1)
        # End date range selection

        # DB Credentials
        lbl = Label(frame, text="DB User:")
        lbl.grid(row=2, column=0, sticky=E)

        self.user_entry = Entry(frame)
        self.user_entry.grid(row=2, column=1)

        lbl = Label(frame, text="DB Pass:")
        lbl.grid(row=3, column=0, sticky=E)

        self.pass_entry = Entry(frame, show='*')
        self.pass_entry.grid(row=3, column=1)
        # End DB Creds

        # Button to start process
        btn = Button(frame, text="Generate Report", command=self.gen_report)
        btn.grid(row=4, column=1, sticky=E)

    def gen_report(self):
        print "working"

root = Tk()
txledgui = TxLedGui(root)
root.mainloop()
