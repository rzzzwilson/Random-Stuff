import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        #create the main window widget
        self.main_window=tkinter.Tk()

        #Create a Button Widget. The text
        #Should appear on the face of the button. The
        #do_something method should execute when the
        #user click the Button.

        self.my_button1=tkinter.Button(self.main_window,                                      text='10 Digit ISBN Check',                                      command=self.check_digit_10)
        self.my_button2=tkinter.Button(self.main_window,                                        text='13 Digit ISBN Check',                                        command=self.check_digit_13)
        self.my_button3=tkinter.Button(self.main_window,                                       text='Convert 10 to 13 ISBN',                                       command=self.convert_10_to_13)
        self.my_button4=tkinter.Button(self.main_window,                                       text='Convert 13 to 10 ISBN',                                       command=self.convert_13_to_10)
        
    

        #Create a Quit Button. When this button is clicked the root
        #widget's destroy method is called.
        #(The main_window variable references the root widget, so the
        #callback function is self.main_window.destroy.)

        self.quit_button=tkinter.Button(self.main_window,                                        text='Quit',                                        command=self.main_window.destroy)
        #pack the buttons
        self.my_button1.pack()
        self.my_button2.pack()
        self.my_button3.pack()
        self.my_button4.pack()
        self.quit_button.pack()

        #Enter the tkinter main loop
        tkinter.mainloop()

        #callback functions for the button widgets.


    def check_digit_10(self):
        isbn=(input('Enter a number to check:'))
        assert len(isbn) == 9
        sum = 0
        for i in range(len(isbn)):
            c = int(isbn[i])
            w = i + 1
            sum += w * c
        r = sum % 11
        if r == 10:
            return 'X'
        else:
            return str(r)

    def check_digit_13(self):
        isbn=(input('Enter a number to check:'))
        assert len(isbn) == 12
        sum = 0
        for i in range(len(isbn)):
            c = int(isbn[i])
            if i % 2: w = 3
            else: w = 1
            sum += w * c
        r = 10 - (sum % 10)
        if r == 10:
            return '0'
        else:
            return str(r)
    def convert_10_to_13(self):
        isbn=(input('Enter a number to convert:')
        assert len(isbn) == 10
        prefix = '978' + isbn[:-1]
        check = check_digit_13(prefix)
        return prefix + check



    def convert_13_to_10(self):
     isbn=(input('Enter a number to convert:')
           

    #Create an instance of the MyGUI class
my_gui=MyGUI()
