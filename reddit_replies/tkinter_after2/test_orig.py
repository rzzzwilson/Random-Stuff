import tkinter as tk  
from queue import Queue
import serial
from threading import Thread

gps = serial.Serial("com2" , baudrate = 9600)

def gui(threadname,q):
    gui = tk.Tk()
    frame = tk.Frame(gui)
    frame.pack()

    Var = tk.StringVar()

    button = tk.Button(frame, text=Var)
    button.pack(side=tk.LEFT)

    gui.after_idle(updater(q))
    gui.mainloop()

def updater(q):
    Var = q.get()
    return Var

def get_data(threadname, q):
    while True:
        a = str(gps.readline())
        q.set(a)




queue = Queue()


if __name__ == '__main__':
    Thread(target = gui, args=("GUI thread",queue)).start()
    Thread(target = get_data, args=("DATA thread", queue)).start()
