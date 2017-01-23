#!/usr/bin/env python

"""
This is a guess the number game.

https://www.reddit.com/r/learnpython/comments/5pkc31/trying_to_learn_tkinter/
"""

from Tkinter import *
import random

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.guess = Entry(frame)
        self.guess.pack()
        self.result = Text(frame)
        self.result.pack()

        self.button = Button(frame, text='QUIT', fg='red', command=frame.quit)
        self.button.pack(side=RIGHT)

        self.hi_there = Button(frame, text='Play!', command=self.play)
        self.hi_there.pack(side=LEFT)

    def play(self):
        secretNumber = random.randint(1, 20)
        print('I am thinking of a number between 1 and 20.')
        guess = 0
        # Ask the player to guess 6 times.
        for guessesTaken in range(1, 7):
            try:
                guess = int(input('Take a guess?'))

                if guess < secretNumber:
                    print('Your guess is too low.')
                elif guess > secretNumber:
                    print('Your guess is too high.')
                else:
                    break  # This condition is the correct guess!
            except ValueError:
                print('Invalid Number')
        if guess == secretNumber:
            print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
        else:
            print('Nope. The number I was thinking of was ' + str(secretNumber))

root = Tk()

app = App(root)

root.mainloop()
#root.destroy() # optional; see description below

