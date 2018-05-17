from tkinter import *
root = Tk()
versiontitle = Label(root, text="Keybuddy 0.2")
versiontitle.pack()

#first key text
k1text = Label(root, text="First key:")
k1text.pack()

#first key entry
k1 = IntVar()
k1entry = Entry(textvariable=k1)
k1entry.pack()

#second key text
k2text = Label(root, text="Second key:")
k2text.pack()

#second key entry
k2 = IntVar()
k2entry = Entry(textvariable=k2)
k2entry.pack()

#magic button
def inbalg():
    k1_value = k1.get()
    k2_value = k2.get()
    print(f"k1_value={k1_value}, k2_value={k2_value}")
    inbetween = (k1_value + k2_value) / 2
    if (inbetween % 2) != 0:
        print(inbetween)
    else:
        print('No central frame found. Try', (inbetween - 1), 'or', (inbetween + 1))
magicbutton = Button(text='Magic!', command=inbalg)
magicbutton.pack()

#
root.mainloop()
