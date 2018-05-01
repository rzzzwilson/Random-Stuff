from tkinter.scrolledtext import ScrolledText
from tkinter import *
from time import sleep
import socket
import threading
import sys

PORT = 52000
SERVER_IP = "localhost"

class Gui:
    def __init__(self, master):
        self.master = master
        master.title("Client")
        master.geometry("600x750")

        self.chat = ScrolledText(self.master, state = "disabled", width = 72)
        self.chat.grid(padx = 4, pady = 4, columnspan = 2)

        self.chat_entry = ScrolledText(self.master, width = 55, height = 3)
        self.chat_entry.grid(row = 1, padx = 4, pady = 4)

        self.send_button = Button(self.master, text = "Send", width = 10, height = 2)
        self.send_button.grid(row = 1, column = 1, padx = 4, pady = 4)

class Client(Gui):
    def __init__(self, master, ip, port):
        Gui.__init__(self, master)
        master.protocol("WM_DELETE_WINDOW", self.stop)
        self.chat_entry.bind("<Return>", self.enter)
        self.chat.bind("<1>", lambda e:self.chat.focus)
        self.send_button.configure(command = self.enter)

        self.server_ip = ip
        self.port = port

#        self.s = socket.socket()
#
#        try:
#            self.s.connect((self.server_ip, self.port))
#        except ConnectionRefusedError:
#            error = "Can't connect to server on %s:%s!"%(self.server_ip,self.port)
#            self.chat_add(error)
#            sys.exit()

        self.listening = threading.Thread(target=self.listen)
        self.listening.daemon = True
        self.listening.start()

    def stop(self):
#        self.s.shutdown(1)
#        self.s.close()
        self.master.destroy()

    def enter(self,*args):
        message = self.chat_entry.get(1.0,"end-1c")
        if message != "":
            message = message.encode("utf-8", "replace")
            self.s.send(message)
        self.master.after(0,lambda: self.chat_entry.delete(1.0, END))

    def chat_add(self, text):
        text = str(text)
        text += "\n"
        self.chat.configure(state = "normal")
        self.chat.insert(END, text)
        self.chat.yview(END)
        self.chat.configure(state = "disabled")

    def listen(self):
        while True:
            for i in range(10):
                sleep(2.0)
                self.master.after(1, self.chat_add, "Test data")
            self.master.after(1, self.chat_add, "disconnected!")
            break
#            try:
#                sleep(1.0)
#                data = self.s.recv(2048).decode("utf-8", "replace")
#                self.chat_add(data)
#            except Exception as e:
#                print(e)
#                self.chat_add("Server disconnected!")
#                break

root = Tk()
app = Client(root, SERVER_IP, PORT)
root.mainloop()
