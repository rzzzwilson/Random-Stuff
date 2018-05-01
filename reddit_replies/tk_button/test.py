import Tkinter
import tkMessageBox

top = Tkinter.Tk()

def helloCallBack(text):
   tkMessageBox.showinfo("Hello Python", text)

for x in ['A', 'B']:
    Tkinter.Button(top, text = x, command=lambda x=x: helloCallBack(x)).pack()

top.mainloop()
