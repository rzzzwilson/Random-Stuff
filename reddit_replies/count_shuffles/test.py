#!/usr/bin/env python3

"""
Solve the puzzle vaguely described in:

https://www.reddit.com/r/learnpython/comments/7mdmfh/can_anyone_solve_this_question/
"""

def shuffle(deck):
    """Perform a shuffle on given deck, return shuffled deck."""

    top = []                    # set 'top' deck to be empty
    while deck:                 # loop while 'deck' has cards in it
        card = deck.pop(0)      #   get top card
        top.insert(0, card)     #   put that card on top of 'top'
        if deck:                #   if 'deck' isn't empty
            card = deck.pop(0)  #     get next top card
            deck.append(card)   #     put into bottom of the deck
    return top                  # return 'top' which is the shuffled 'deck'

deck = [x for x in range(52)]
orig = deck[:]      # get copy of original deck
count = 0

print(f'deck={deck}')

while True:
    count += 1
    deck = shuffle(deck)
    if deck == orig:
        break

print(f'deck={deck}')
print(f'count={count}')
