import random 

#When counter is at 1, game is over.
COUNTER = 10
MIN_GUESS = 1
MAX_GUESS = 100
EXIT_RESPONSES = ['exit', "'exit'"]
number = random.randint(MIN_GUESS, MAX_GUESS)
game = True

#Must be integer in order to proceed. Only strings allowed are EXIT_RESPONSES.
def must_be_int(user_input):
    while type(user_input) == str:
        try:
            user_input = user_input.lower()
            user_input = int(user_input)
            return user_input
        except ValueError:
            if user_input in EXIT_RESPONSES:
                return user_input
            else:
                user_input = input('That is not a number.\n'
                                   'Please enter a number between {} and {}: '
                                   .format(MIN_GUESS, MAX_GUESS))
                continue

#Game start prompt.
user_input = input('Guess my number, which is between {} and {}.\n'
                  'You have {} tries.\n'
                  "Type 'exit' to exit the game.\n"
                  'Enter your number: '.format(MIN_GUESS, MAX_GUESS, COUNTER))

#Loop to tell user if their guess is: exit; game over; too high or low; or win.
while game:
    user_input = must_be_int(user_input)
    if user_input in EXIT_RESPONSES:
        print('Thank you for playing.')
        game = False
    elif COUNTER == 1:
        print('\nYou have 0 tries remaining. Game over. Thanks for playing.\n'
              'The correct number was {}.'.format(number))
        game = False
    elif user_input not in range(MIN_GUESS, MAX_GUESS+1):
        user_input = input('That is not an allowable number, please try again.\n'
                          'Enter your number: ')
    elif user_input > number:
        COUNTER -= 1
        user_input = input('{}is too high, please try again.\n'
                          'You have {} tries remaining.\n'
                          'Enter your number: '.format(user_input, COUNTER))
    elif user_input < number:
        COUNTER -= 1
        user_input = input('{} is too low, please try again.\n'
                          'You have {} tries remaining.\n'
                          'Enter your number: '.format(user_input, COUNTER))
    else:
        print('\nCongratulations, {} is the correct number!\n'
              'You win the game!'.format(number))
        game = False
