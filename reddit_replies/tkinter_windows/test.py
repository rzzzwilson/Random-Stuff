from tkinter import *
from tkinter import ttk


class App:
    def __init__(self, master):

        mainframe = ttk.Frame(master, padding="3 6 3 6")
        mainframe.grid(column=0, row=0, sticky=(N, W, S, E))

        self.button = ttk.Button(mainframe, text="CLICK ME", command=self.second_layer)
        self.button.grid(column=0, row=0)

    def second_layer(self):
        self.t = Toplevel(root) # I'm surprised I needed to do Toplevel(root) instead of Toplevel(mainframe) here. I'm still unsure why is that. 

        self.time = ttk.Label(self.t, text="Huzzah!")
        self.time.pack(side=LEFT)

        self.jst = ttk.Button(self.t, text="IT WORKED", command=self.third_layer)
        self.jst.pack(side=RIGHT)

    def third_layer(self):
        self.top = Toplevel(root) # Same thing here, I don't know why this needs (root) instead of my previous layer (t). 

        self.voila = ttk.Label(self.top, text="Python is awesome")
        self.voila.pack(side=RIGHT)

# The next line produces an error. Without the next line, the new window is created normally with the text. This is the error:
#Exception in Tkinter callback
# ...
#_tkinter.TclError: bad window path name ".!toplevel2"
        #self.end = ttk.Button(self.top, text="QUIT", command=self.top.destroy())


        
root = Tk()

app = App(root)

root.mainloop()

