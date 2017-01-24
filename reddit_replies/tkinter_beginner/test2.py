#!/usr/bin/env python

"""
This is a guess the number game.

https://www.reddit.com/r/learnpython/comments/5pkc31/trying_to_learn_tkinter/
"""

from Tkinter import *
import tkMessageBox
import random

class App:
    def __init__(self, master):
        # tie close event to handler
        root.protocol("WM_DELETE_WINDOW", self.on_closing)

        frame = Frame(master)
        frame.pack()

        # the current number the user is guessing
        self.secretNumber = None

        # the current guess number
        self.guess_number = 0

        self.guess = Entry(frame)
        self.guess.pack()
        self.result = Text(frame)
        self.result.pack()

        self.button = Button(frame, text='Guess?', command=self.handle_guess)
        self.button.pack(side=RIGHT)

        self.hi_there = Button(frame, text='Play!', command=self.handle_play)
        self.hi_there.pack(side=LEFT)

    def on_closing(self):
        var = tkMessageBox.askyesno("Quit", "Do you want to quit?")
        if var:
            # do other stuff here, like save results to a file
            root.destroy()

    def handle_guess(self):
        """User says she has made a guess."""

        print('point 0: .guess_number=%d' % self.guess_number)

        # if self.secretNumber is None we aren't playing
        if self.secretNumber is None:
            tkMessageBox.showerror('Error', 'Sorry, you have to press the "Play" button first')
            return

        # get user guess and see if it's legal
        guess = self.guess.get()
        print('guess=%s' % guess)

        print('point 1: .guess_number=%d' % self.guess_number)

        try:
            guess_int = int(guess)
        except ValueError:
            tkMessageBox.showerror('Error', 'Sorry, your guess must be between 1 and 20')
            return

        if not 0 < guess_int < 21:
            tkMessageBox.showerror('Error', 'Sorry, your guess must be between 1 and 20')
            return

        print('point 2: .guess_number=%d' % self.guess_number)

        self.guess_number += 1

        print('point 3: .guess_number=%d' % self.guess_number)

        # see how guess compares with the secret number
        if guess_int == self.guess_number:
            msg = 'Good job! You guessed my number in %d guesses!' % self.guess_number
            self.display(msg)
            self.secretNumber = None        # flag that we are finished
        else:
            print('point 4: .guess_number=%d' % self.guess_number)

            if self.guess_number >= 6:
                msg = 'Nope. The number I was thinking of was %d.' % self.secretNumber
                self.display(msg)
                self.secretNumber = None
                self.guess_number = 0
                self.guess.delete(0, END)
                return

            if guess_int < self.secretNumber:
                msg = '%d: Your guess %d is too low.' % (self.guess_number, guess_int)
            elif guess_int > self.secretNumber:
                msg = '%d: Your guess %d is too high.' % (self.guess_number, guess_int)
            self.display(msg)

        self.guess.delete(0, END)

    def handle_play(self):
        self.secretNumber = random.randint(1, 20)
        self.clear_results()
        self.display('I am thinking of a number between 1 and 20.')

    def clear_results(self):
        """Clear the result display."""

        self.result.delete('1.0', END)

    def display(self, msg):
        """Append a message to the display."""

        #insert(END, msg+'\n', *tags) 
        self.result.insert(END, msg+'\n') 

root = Tk()

app = App(root)

root.mainloop()

