import random

def guess_number():

  def guess_attempt():
    guess = int(input("I picked a number between 1 & 10...guess what it is: "))

    return guess

  #the number for which the player must guess
  mystery_number = random.randint(1, 10)

  #the number player guesses
  player_guess = guess_attempt

  #number of attempts the player has to guess the number
  guess_tries = 5

  while guess_tries >= 1:
    if player_guess() != mystery_number:
      guess_tries -= 1
      if guess_tries > 0:
        print("Sorry, but that number isn't right. You have {} guesses left.".format(guess_tries))
        continue
      else:
        print("You have no more guesses. The mystery_number was {}".format(mystery_number))
        break
    else:
      print("You got it, but it took you {} times to get it!".format(5 - guess_tries))
      break


guess_number()
