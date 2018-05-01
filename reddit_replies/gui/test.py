import sys
from tkinter import *
from tkinter.font import Font

Turn = 1
str_resourcegain = [str(x) for x in range(1, 8)]
resources = [str(x) for x in range(1, 8)]
new_resources = [str(x) for x in range(10, 18)]
ResourceLabels = []

def refresh():
    for (i, lab) in enumerate(ResourceLabels):
        print('type(lab)=%s' % type(lab))
        lab['text'] = '%s: %s' % (str_resourcegain[i], new_resources[i])
    print(ResourceLabels)

root = Tk()
root.title("Virus Attack!")
root.geometry('1920x1080')

mLabel = Label(text=('Turn %s'%(Turn)),fg='red',bg='green')

###LABELR###
for x in range(0,7):
    t = Label(text = '%s: %s'%(str_resourcegain[x], resources[x]))
    t.place(relx=0.01,rely=0.02+(0.05*x))
    print('append t=%s' % str(t))
    ResourceLabels.append(t)
###LABELR###

TimesNewRoman = Font(family="times new roman",size=12)
mLabel.configure(font=TimesNewRoman)
mLabel.pack()

RefreshButton = Button(text = 'Refresh',command = refresh).place(relx=0.1, rely=.85)

root.mainloop()
