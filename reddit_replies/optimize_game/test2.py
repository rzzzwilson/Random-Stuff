import random 

MacNumGuesses = 10
MinNumber = 1
MaxNumber = 100
ExitResponses = ['exit', "'exit'", 'x', '']

# get a random number
number = random.randint(MinNumber, MaxNumber)

print(f'Guess my number, which is between {MinNumber} and {MaxNumber}.')
print("Type 'exit' to exit the game.")

# loop until game over
while MacNumGuesses:    # don't really need the "game" variable
    # get users response, lower case
    user_input = input(f'\nYou have {MacNumGuesses} tries left, '
                       'enter your number: ').strip().lower()

    # if user wants to exit, break out
    if user_input in ExitResponses:
        print('\nThank you for playing.')
        break

    # see if the user entered a legal number
    try:
        user_num = int(user_input)
    except ValueError:
        print('That is not a number.\n'
              f'Please enter a number between {MinNumber} and {MaxNumber}')
        continue

    if not MinNumber <= user_num <= MaxNumber:
        print('That is not an allowable number, please try again.\n'
              f'Please enter a number between {MinNumber} and {MaxNumber}.')
        continue

    if user_num > number:
        MacNumGuesses -= 1
        print(f'{user_num} is too high, please try again.')
        continue

    if user_num < number:
        MacNumGuesses -= 1
        print(f'{user_num} is too low, please try again.')
        continue

    print(f'\nCongratulations, {user_num} is the correct number!\n'
          'You win the game!')
    break
else:
   print('\nYou have 0 tries remaining. Game over. Thanks for playing.\n'
         f'The correct number was {number}.')

