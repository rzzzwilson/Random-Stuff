import random
import time

LINE_DELAY = 0.5

def timed_print(msg):
    """Print a message line by line, with a delay before each line."""

    lines = msg.split('\n')
    for line in lines:
        time.sleep(LINE_DELAY)
        print(line)

def get_input(prompt):
    """Get a user's response, return lowercase."""

    print()         # blank line to make prompt standout
    result = input(prompt)
    return result.lower()

def intro():
    timed_print('Text Adventure\nA Story\n')
    path = choice1()
    path2 = choice2(path)
    choice3(path2)
 
def choice1():
    timed_print('While walking you stumble across a path\n'
                'Confused you are unsure of which way to go')
    return get_input('Do you go right or left? ')
 
def choice2(path):
    if path == 'right':
        timed_print('You go right\nYou see shady man in the woods')
        answer = get_input('He asks if you want to see lizard, it has tongue that spits. '
                           'Do you pet the lizard or no? ')
    elif path == 'left':
        timed_print('You encounter a thief, do you give him your watch or run away')
        answer = get_input('Do you give him your watch or run away? ')
    else:
        timed_print('return')
    return answer
 
def choice3(path2):
    if path2 == 'pet':
        timed_print('lizard spit in your face\nRIP')
    elif path2 == 'no':
        timed_print('blabla')
    elif path2 == 'give watch':
        timed_print('you lost your watch')
    elif path2 == 'run away':
        timed_print('thief catches you and kills you')
    else:
        timed_print('return')
 
intro()
