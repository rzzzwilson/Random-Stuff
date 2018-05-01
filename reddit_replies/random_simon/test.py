import sys
import random
number = random.randint(1, 100)

sys.setrecursionlimit(10)

def game():
    print('Guess a number 1-100')

    guess = int(input())

    if guess < number:
        print('Higher')
        game()
    if guess > number:
        print('Lower')
        game()
    if guess == number:
        print('Great Guess. Play Again? (y/n)')
        again()


def again():
    response = input()
    if response == 'y':
        game()
    if response == 'n':
        print('Goodbye')
    if response != 'n' or 'y':
        print('Please say y or n')
        again()


game()
