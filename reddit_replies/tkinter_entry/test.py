"""
Calculator
"""

from tkinter import *

class frontend:
    def __init__(self,parent):
        self.parent = parent
        parent.title("Calculator")
        parent.maxsize(224,333)
        parent.minsize(224,333)
        parent.configure(background="White")
        string = StringVar()
        blankp = PhotoImage()

        global box

        #parent.bind("<Key>",self.enter)
        scrollbar = Scrollbar(parent)
        scrollbar.grid(row=0,column=9)
        
        self.box = Entry(parent,textvariable=string,relief=FLAT,justify=RIGHT,width=9,xscrollcommand=scrollbar.set,
        font=("arial","32"))
        self.box.grid(row=0,column=0,columnspan=9)
        #self.box.focus_set()

        scrollbar.config(command=self.box.xview)
        
        
        plus = Button(parent,relief=FLAT,image=blankp,compound=CENTER,bg="SteelBlue1",
        fg="White",text="+",font=("arial","24"),width="48",height="48",borderwidth="0",
        command=self.enter("+"))
        #parent.bind("+",self.keyenter("+"))
        plus.image = blankp
        plus.grid(row=3,column=3,padx=2,pady=2)

        minus = Button(parent,relief=FLAT,image=blankp,compound=CENTER,bg="SteelBlue1",
        fg="White",text="-",font=("arial","24"),width="48",height="48",borderwidth="0",
        command=self.enter("-"))
        #parent.bind("-",self.keyenter("-"))
        minus.image = blankp
        minus.grid(row=4,column=3,padx=2,pady=2)

        times = Button(parent,relief=FLAT,image=blankp,compound=CENTER,bg="SteelBlue1",
        fg="White",text="×",font=("arial","24"),width="48",height="48",borderwidth="0",
        command=self.enter("×"))
        #parent.bind("*",self.keyenter("×"))
        times.image = blankp
        times.grid(row=5,column=3,padx=2,pady=2)

        division = Button(parent,relief=FLAT,image=blankp,compound=CENTER,bg="SteelBlue1",
        fg="White",text="÷",font=("arial","24"),width="48",height="48",
        borderwidth="0",command=self.enter("÷"))
        #parent.bind("/",self.keyenter("÷"))
        division.image = blankp
        division.grid(row=6,column=3,padx=2,pady=2)

        equals = Button(parent,relief=FLAT,image=blankp,compound=CENTER,bg="orange",
        fg="White",text="=",font=("arial","24"),width="48",height="48",borderwidth="0",
        command=lambda:self.equal())
        parent.bind("<Return>",self.equal)
        equals.image = blankp
        equals.grid(row=6,column=2,padx=2,pady=2)

        numbers = ["7","8","9","4","5","6","1","2","3"]
        counter = 3
        counter2 = 0
        for i in numbers:
            numberb = Button(parent,relief=FLAT,image=blankp,compound=CENTER,
            bg="gainsboro",text=i,font=("arial","14"),width="48",height="48",
            borderwidth="0",command=self.enter(i))
            numberb.image = blankp
            numberb.grid(row = counter,column = counter2,padx=2,pady=2)
            
            if counter2 == 2: 
                counter += 1
                counter2 = 0
            else:
                counter2 += 1

        zero = Button(parent,relief=FLAT,image=blankp,compound=CENTER,bg="gainsboro",
        text="0",font=("arial","14"),width="48",height="48",borderwidth="0",command=self.enter("0"))
        zero.image = blankp
        zero.grid(row = 6,column = 0,padx=2,pady=2)

        decimal = Button(parent,relief=FLAT,image=blankp,compound=CENTER,text=".",
        bg="gainsboro",font=("arial","14"),width="48",height="48",borderwidth="0",
        command=self.enter("."))
        decimal.image = blankp
        decimal.grid(row = 6,column = 1,padx=2,pady=2)

        bracketopen = Button(parent,relief=FLAT,image=blankp,compound=CENTER,text="(",
        bg="gray59",fg="white",font=("arial","14"),width="48",height="48",borderwidth="0",
        command=self.enter("("))
        bracketopen.image = blankp
        bracketopen.grid(row = 2,column = 0,padx=2,pady=2)

        bracketclose = Button(parent,relief=FLAT,image=blankp,compound=CENTER,text=")",
        bg="gray59",fg="white",font=("arial","14"),width="48",height="48",borderwidth="0",
        command=self.enter(")"))
        bracketclose.image = blankp
        bracketclose.grid(row = 2,column = 1,padx=2,pady=2)

        delete = Button(parent,relief=FLAT,image=blankp,compound=CENTER,text="⌫",bg="gray59",fg="white",
        font=("arial","14"),width="48",height="48",borderwidth="0",
        command=self.backspace)
        delete.image = blankp
        delete.grid(row = 2,column = 2,padx=2,pady=2)

        clear = Button(parent,relief=FLAT,image=blankp,compound=CENTER,text="AC",bg="goldenrod3",fg="black",
        font=("Helvetica Neue Light","14","bold"),width="48",height="48",borderwidth="0",command=self.AC)
        clear.image = blankp
        clear.grid(row = 2,column = 3,padx=2,pady=2)
        
    def AC(self):
        self.box.delete(0,END)

    def backspace(self):
        self.box.delete(len(self.box.get())-1)


    def enter(self,x):
        #if key.char in [list]:
        self.box.xview_moveto(1)
        return lambda: self.box.insert(END,x)

    #entryd = len(self.box)
        #if entryd > 10:
         #   self.box.configure(font=("arial",x))
        
        #self.box.xview_moveto(1.0)

    def keyenter(self,x):
        return lambda a: self.box.insert(1,x)
        #self.box.xview_moveto(1)
        #self.box.xview_moveto(1.0)
        
    def disabler(self):
        wfocus = parent.focus_get()
        pfocus = parent.focus()

    def test(self):
        print('e')
        
    
    def equal(self,event = None):
        self.task = self.box.get()
        self.task = str(self.task)
        self.calculationsetup()
        self.box.delete(0,END)
        self.box.insert(END,self.out)
        
        #back = backend(self.out)
        print("gg")
        #self.box.insert(back.calculations())
        
        
class backend(frontend):
    def calculationsetup(self):
        if "÷" in self.task:
            self.task = self.task.replace("÷","/")
            if "×" in self.task:
                self.task = self.task.replace("×","*")
                self.calculations()
            else:
                self.calculations()
        elif "×" in self.task:
            self.task = self.task.replace("×","*")
            if "÷" in self.task:
                self.task = self.task.replace("÷","/")
                self.calculations()
            else:
                self.calculations()
        else:
            self.calculations()

    def calculations(self):
        self.out = eval(self.task)
        self.out = round(self.out, 9)
        self.out = str(self.out)
        print(self.out)
        
    
        
        
        #self.box.insert(self.out)
        #except SyntaxError:
           # print("Invalid")
      
        
        
        
            

#answer = eval(task)
#self.box.delete(0, END)
#self.box.insert(100,answer)

        

        

root = Tk()
calculator = backend(root)
root.mainloop()
