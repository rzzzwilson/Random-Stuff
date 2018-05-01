from tkinter import *
from tkinter import ttk

class App:
    def __init__(self, master):
        self.master = master
        self.mainframe = ttk.Frame(master, padding="3 6 3 6")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, S, E))
        self.button = ttk.Button(self.mainframe, text="CLICK ME", command=self.second_layer)
        self.button.grid(column=0, row=0)

    def second_layer(self):
        self.t = Toplevel()
        self.time = ttk.Label(self.t, text="Huzzah!")
        self.time.pack(side=LEFT)
        self.jst = ttk.Button(self.t, text="IT WORKED", command=self.third_layer)
        self.jst.pack(side=RIGHT)

    def third_layer(self):
        self.top = Toplevel()
        self.voila = ttk.Label(self.top, text="Python is awesome")
        self.voila.pack(side=RIGHT)
        
root = Tk()
app = App(root)
root.mainloop()

