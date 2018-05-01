import random

def guess_number():
    # the number which the player must guess
    mystery_number = random.randint(1, 10)
    print('mystery_number=%d' % mystery_number)

    #number of attempts the player has to guess the number
    guess_tries = 5

    while guess_tries > 0:      # "while guess_tries:" also works
        guess = int(input("I picked a number between 1 & 10...guess what it is: "))
        guess_tries -= 1        # we've made a guess, so decrement tries remaining

        if guess == mystery_number:
            print("You got it, but it took you {} times to get it!".format(5 - guess_tries))
            return              # or "break"

        print("Sorry, but that number isn't right. You have {} guesses left.".format(guess_tries))
    else:                       # "else" on "while" executes only when the loop is exhausted
        print("You have no more guesses. The mystery_number was {}".format(mystery_number))

guess_number()
