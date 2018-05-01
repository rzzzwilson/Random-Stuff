import subprocess
import signal
import os
import sys
#import Adafruit_MCP4725

#dac = Adafruit_MCP4725.MCP4725()
from tkinter import *
from tkinter import Tk, Label, Radiobutton


class MyGUI:
    rate1 = 60
    def __init__(self, master):
        self.master = master
        master.title("ICP WaveForm Control")
        master.geometry("480x320")

        self.modelone = Radiobutton(master, text = "Normal", bg = 'seashell3', indicatoron = 0, value =1, variable = 1, command = self.modelone)
##        self.modelone.pack(fill = X, expand = 1)
        self.modelone.grid(row = 1, column = 0, sticky ='WNS', padx = 0, pady = 10)

        self.modeltwo  = Radiobutton(master, text = "Leveled",indicatoron = 0, value = 2, variable = 1, bg = 'seashell3',command = self.modeltwo)
##        self.modeltwo.pack(fill = X, expand = 1)
        self.modeltwo.grid(row=2, column=0,sticky = 'WNS', padx =0, pady = 10)
##        mi = PhotoImage("
##        self.modeltwo.config(

        self.modelthree = Radiobutton(master, text = "Abnormal", indicatoron = 0, value = 3, variable = 1, bg = 'seashell3',  command = self.modelthree)
##        self.modelthree.pack(fill = X, expand = 1)
        self.modelthree.grid(row=3, column=0, sticky ='WNS', padx = 0, pady = 10)

        self.donebutton = Radiobutton(master, text = "Zero", indicatoron = 0, variable = 1, value = 4, bg = 'seashell3', command = self.done)
##        self.donebutton.pack(fill = X, expand = 1)
        self.donebutton.grid(row=4, column=0, sticky ='WNS', padx = 0, pady = 10)

        self.quitbutton = Radiobutton(master, text = "Quit", indicatoron = 0, value = 5, variable = 1, bg = 'seashell3', command = self.quit)
##        self.quitbutton.pack(fill = X, expand = 1)
        self.quitbutton.grid(row=5, column=0, sticky ='EWNS', padx = 0, pady = 10)
        
        Label(master, text = "", width = 5, height = 5).grid(row = 2, column = 4, sticky = "WNS")
        self.DisplayButton = Button(master, text = self.rate1)
        self.DisplayButton.grid(column = 1, row = 2, sticky = "WNS")
        self.Plus1Button = Button(master, text = "+1", command=self.plus1, bg="green")
        self.Plus1Button.grid(column = 1, row = 1, sticky = "WNS")
        self.Neg1Button = Button(master, text = "-1", command=self.neg1, bg="green")
        self.Neg1Button.grid(column = 1, row = 3, sticky = "WNS")
        
    
        self.pid = -1
        

    def plus1(self):
        self.done()
        self.rate1 += 5
        self.DisplayButton["text"]=str(self.rate1)


    def neg1(self):
        self.done()
        self.rate1 -= 5
        self.DisplayButton["text"]=str(self.rate1)
    

    def modelone(self):
        self.done()
        self.process = subprocess.Popen('python modelone.py {}'.format(self.rate1), shell=True, preexec_fn=os.setsid)
        self.pid = self.process.pid
                           

    def modeltwo(self):
        self.done()
        self.process = subprocess.Popen('python modeltwo.py {}'.format(self.rate1), shell=True, preexec_fn=os.setsid)
        self.pid = self.process.pid
        
        
    def modelthree(self):
        self.done()
        self.process = subprocess.Popen('python modelthree.py {}'.format(self.rate1), shell=True, preexec_fn=os.setsid)
        self.pid = self.process.pid
        

    def done(self):
        if self.pid > 0: 
            os.killpg(os.getpgid(self.pid), signal.SIGTERM)
            self.pid = -1
            
    def quit(self):
        self.done()
        self.master.quit()

root = Tk()
my_gui = MyGUI(root)
root.mainloop()
