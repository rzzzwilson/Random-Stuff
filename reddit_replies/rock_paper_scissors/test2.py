p1 = input('Enter the sign for person 1: ').lower()
p2 = input('Enter the sign for person 2: ').lower()
winner = None
if p1 == 'rock':
    if p2 == 'rock':
        winner = 0    # tie - no winner
    elif p2 == 'paper':
        winner= 2    # person 2 is winner
    elif p2 == 'scissors':
        winner = 1    # person 1 is winner
elif p1 == 'paper':
    if p2 == 'rock':
        winner = 1
    elif p2 == 'paper':
        winner= 0
    elif p2 == 'scissors':
        winner = 2
elif p1 == 'scissors':
    if p2 == 'rock':
        winner = 2
    elif p2 == 'paper':
        winner= 1
    elif p2 == 'scissors':
        winner = 0

if winner == 0:
    print('tie!')
elif winner == 1:
    print(f'Person 1 wins, {p1} beats {p2}')
elif winner == 2:
    print(f'Person 2 wins, {p1} beats {p2}')
