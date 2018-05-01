import time

def game_over():
    print('*********')
    print('Game over')
    print('*********')
    time.sleep(5)
    quit()

def play_the_game():
    while True:
        answer = input('Enter a number ')
        if answer == '2':
            game_over()
        print('Try again')

play_the_game()

