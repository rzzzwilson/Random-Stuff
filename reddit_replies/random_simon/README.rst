Code investigating:

https://www.reddit.com/r/learnpython/comments/8404n6/trying_to_randomize_a_number_every_time_a_scope/

After you have solved your randomization problem, you should note that you have
a memory leak because you are using unbounded recursion to loop. "while" or
"for" loops are better at looping - use them.  Using recursion as you have
means that your program will crash after about 1000 player guesses.  You can
see the effect if you lower python's recursion limit with these lines at the
top of your code:

    import sys
    sys.setrecursionlimit(10)       # set recursion limit to 10

and just enter about 5 responses.

You should structure your code differently.  Have a function to play just one
game.  This function should randomize your target number and then loop, getting
the player's response each time around the loop.  Don't worry about playing
again in this function, that's someone else's job.

You should should have a function that manages the "play again?" business.  This
function will have a loop that:

* plays one game
* asks the player if they want to play again
* returns if the player doesn't want to play again

It's also best if you write the code getting the player's response to
"play again?" as another function.  That's because if the player doesn't enter
'y' or 'n' you want to print the error message and then loop, asking again for
a response.  This function will always return 'y' or 'n' and nothing else.
That simplifies the code that calls this function.

So, as a hint, some incomplete code:

    def game():
        print('Guess a number 1-100')
        number = random.randint(1, 100)

        while True:
            guess = int(input())
            if guess < number:
            # etc, "break" if guess is correct
    
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
            # etc, farewell message and "break"

    play()

