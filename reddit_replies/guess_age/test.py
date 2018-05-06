number = 20
tries = 1
 
uname = input("Tell me your name")
print("Hello", uname + ".", )
 
question = input("Guess my age! Y/N?")
if question == "n":
    print("Goodbye")
if question == "y":
    print("Great.")
    guess = int(input("What's your guess?"))
    if guess < number:
        print("I'm not that young.")
    if guess > number:
        print("I'm not that old.")
 
while guess != number:
    tries += 1
    guess = int(input("Guess again"))
    if guess < number:
         print("Higher")
    if guess > number:
        print("Lower")
    if guess == number:
         print("Yeah! You're right")
         print("And it only took you", tries, "tries!")
