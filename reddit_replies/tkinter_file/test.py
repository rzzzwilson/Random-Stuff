import os, math, re, Tkinter, tkFileDialog
import time
import sys

# hide root window
root = Tkinter.Tk()
root.withdraw()

origFilePath = tkFileDialog.askopenfilename()
root.update()
origFile = open(origFilePath, "r")
print 'Waiting 5 seconds ...',
sys.stdout.flush()
time.sleep(5)
print 'done.'
data = origFile.read()
origFile.close()
print "Contents of file '%s':'" % origFilePath, data
