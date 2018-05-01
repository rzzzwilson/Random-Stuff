#!/usr/bin/env python3

"""
Code for reply to a question on reddit:
https://www.reddit.com/r/learnpython/comments/6jc2n0/quick_question_with_a_simple_program/
"""

import sys

Info = """
Allowed commands are:
    ADD         SUBTRACT    MULTIPLY    DIVIDE      POWER
    +           -           *           /           ^
    CLEAR       EXIT        QUIT        HELP        NEW
                                        ?           =
Only the first letter of a command is examined and is case-insensitive.
"""

def get_value(prompt, ac):
    """Return an integer value, either AC or entered integer."""

    while True:
        try:
            value = input(prompt).upper()
        except EOFError:    # handle EOF as a user quitting
            print()         # ensure we finish nicely
            sys.exit(0)

        if value == 'AC':
            return ac

        try:
            return int(value)
        except ValueError:
            print('Only integers, please!')

def calc():
    ac = 0;
    while True:
        print('AC: %d,  ' % ac, end='')
        try:
            choice = input('command: ')[0].upper()
        except EOFError:
            print()
            sys.exit(0)

        if choice in 'EQ':      # 'exit' or 'quit'
            break
        elif choice in 'H?':
            print(Info)
        elif choice in 'C':     # clear AC
            ac = 0
        elif choice in 'N=':    # set AC to new value
            ac = get_value('New AC: ', ac)
        elif choice in 'A+':
            first = get_value('Enter the first number: ', ac)
            second = get_value('%d + ' % first, ac)
            ac = first + second
        elif choice in 'S-':
            first = get_value('Enter the first number: ', ac)
            second = get_value('%d - ' % first, ac)
            ac = first - second
        elif choice in 'M*':
            first = get_value('Enter the first number: ', ac)
            second = get_value('%d * ' % first, ac)
            ac = first * second
        elif choice in 'D/':
            first = get_value('Enter the first number: ', ac)
            second = get_value('%d / ' % first, ac)
            ac = first // second    # integer division
        elif choice in 'P^':
            first = get_value('Enter the first number: ', ac)
            second = get_value('%d ^ ' % first, ac)
            ac = pow(first, second)
        else:
            print('Invalid command')

print(Info)
calc()
