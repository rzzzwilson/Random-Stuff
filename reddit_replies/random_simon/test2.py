import sys
import random

sys.setrecursionlimit(10)

def game():
    print('Guess a number 1-100')
    number = random.randint(1, 100)
    print(number)

    while True:
        guess = int(input())

        if guess < number:
            print('Higher')
        if guess > number:
            print('Lower')
        if guess == number:
            print('Great Guess.\n')
            break

def again():
    while True:
        response = input('Play again? (y/n) ')
        if response in ['y', 'n']:
            return response

        print('Please say y or n')

def play():
    while True:
        game()

        if again() == 'y':
            continue

        print('Goodbye')
        break

play()
