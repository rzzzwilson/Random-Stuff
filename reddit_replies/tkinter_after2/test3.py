"""
Template code taken from: http://effbot.org/tkinterbook/tkinter-whats-tkinter.htm
"""

import time
from queue import Queue
from threading import Thread
from tkinter import Tk, Frame, Button, StringVar, LEFT


class App:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()

        self.var = StringVar()
        self.data_queue = Queue()

        self.button = Button(self.frame, text=self.var)
        self.button.pack(side=LEFT)

        # start the "fetch" thread (just generate data from the clock)
        self.stop_thread = False
        self.thread = Thread(target=self.get_data, args=("DATA thread", self.data_queue))
        self.thread.start()

        # when user clicks "close" widget, call self.stop_all()
        master.protocol("WM_DELETE_WINDOW", self.stop_all )

        self.frame.after(500, self.updater)

    def get_data(self, threadname, q):
        while not self.stop_thread:
            a = str(time.time())
            self.data_queue.put(a)
            print(f'get_data: put "{a}" to queue')
            time.sleep(3)

    def updater(self):
        while not self.data_queue.empty():
            var = self.data_queue.get()
            print(f'updater: got {var}')
        self.frame.after(500, self.updater)     # call again after 500ms

    def stop_all(self):
        """Catch the "window close event".

        We must kill the thread and then call normal quit() function.
        """

        self.stop_thread = True
        self.thread.join()      # wait for thread to stop
        self.frame.quit()       # call normal frame quit()


root = Tk()
app = App(root)     # create the App instance
root.mainloop()     # wait here in the main event loop
