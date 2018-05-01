import random
import csv
import tkinter as tk

total_rows = ['1', '2', '3']
questions = ['alpha OR beta?',
             'gamma OR delta OR epsilon',
             'zeta OR theta',
             'kappa OR lambda?',
             'mu OR nu?',
            ]

x = random.randrange(0, len(total_rows), 1)
y = questions[x]
yy = y.replace("?", "")
yyy = yy.split("OR")   

def option1():
    result = [rightnow, yyy[0], variable.get()] 

def option2():
    result = [rightnow, yyy[1], variable.get()]

def nextquestion():
    with open('save.csv', 'a') as f:
        writer = csv.writer(f)
        result = ['1', '2', '3', '4']
        writer.writerow(result)
    f.close()

root = tk.Tk()

#Button1 = tk.Button(root, text=yyy[0], width=17, height=2, command=option1)
Button1 = tk.Button(root, text=yyy[0], command=option1)
Button1.place(x=160, y=200)
Button1.pack()
#Button2 = tk.Button(root, text=yyy[1], width=17, height=2, command=option2)
Button2 = tk.Button(root, text=yyy[1], command=option2)
Button2.place(x=300, y=200)
Button2.pack()
#Button3 = tk.Button(root, text="Next Question", width=10, height=2, bg="lightblue", command=nextquestion)
Button3 = tk.Button(root, text="Next Question", command=nextquestion)
Button3.place(x=400, y=250)
Button3.pack()

root.mainloop()
