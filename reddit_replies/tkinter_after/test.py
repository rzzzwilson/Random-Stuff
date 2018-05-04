from tkinter import *

UnselectedFile = 'glassy_button_6.gif'
SelectedFile = 'selected_glassy_button_6.gif'

class App:
    def __init__(self, master):
        self.master = master
        frame = Frame(master)
        frame.pack()

        # note that we must keep a reference to these images (the "self." part)
        # if we don't, the images dissappear at the end of __init__() - try it!
        self.unseleted_photo = PhotoImage(file=UnselectedFile)
        self.seleted_photo = PhotoImage(file=SelectedFile)

        self.hi_there = Button(frame, text="Hello",
                               image=self.unseleted_photo, command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print('Blue image shown ...', end='', flush=True)
        self.hi_there.config(image=self.seleted_photo)
        self.master.after(2000, self.reset_image)

    def reset_image(self):
        print(' red image restored.', flush=True)
        self.hi_there.config(image=self.unseleted_photo)

root = Tk()
app = App(root)
root.mainloop()
