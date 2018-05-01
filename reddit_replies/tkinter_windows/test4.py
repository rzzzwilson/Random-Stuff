from tkinter import *
from tkinter import ttk

class App:
    def __init__(self, master):
        self.mainframe = ttk.Frame(master, padding="3 6 3 6")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, S, E))
        ttk.Button(self.mainframe, text="CLICK ME", command=self.second_layer).grid(column=0, row=0)
        self.master = master

    def second_layer(self):
        t = Toplevel(self.mainframe)
        ttk.Label(t, text="Huzzah!").pack(side=LEFT)
        ttk.Button(t, text="IT WORKED", command=self.third_layer).pack(side=RIGHT)

    def third_layer(self):
        top = Toplevel()
        ttk.Label(top, text="Python is awesome").pack(side=RIGHT)
        
root = Tk()
app = App(root)
root.mainloop()

