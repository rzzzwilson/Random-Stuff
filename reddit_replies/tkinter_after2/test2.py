import time
import tkinter as tk  
from queue import Queue
from threading import Thread

def gui():                  # note that function name is "gui", don't use that name in function!
    global my_gui           # note we have to make things global, that's why classes are cleaner
    my_gui = tk.Tk()        # new variable name
    frame = tk.Frame(my_gui)
    frame.pack()

    Var = tk.StringVar()

    button = tk.Button(frame, text=Var)
    button.pack(side=tk.LEFT)

#    my_gui.after_idle(updater)  # must pass address of "updater", not call it
    my_gui.after(500, updater)

    my_gui.mainloop()

def updater():
    Var = queue.get()
    print(f'updater: got "{Var}"')
    my_gui.after(500, updater)
    return Var

def get_data(threadname, q):
    print(f'q: {dir(q)}')       # debug, see what the queue attributes are, see below
    while True:
        a = str(time.time())
        q.put(a)                # q.put(), not q.set()
        print(f'put "{a}" to queue')
        time.sleep(3)


queue = Queue() # note we have to use the global name, we can't pass params to an after() function

Thread(target = get_data, args=("DATA thread", queue)).start()
print('after starting fetch thread')

gui()
print('after starting GUI')
