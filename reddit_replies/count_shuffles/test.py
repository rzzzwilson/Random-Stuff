#!/usr/bin/env python3

"""
Solve the puzzle vaguely described in:

https://www.reddit.com/r/learnpython/comments/7mdmfh/can_anyone_solve_this_question/
"""

deck = [x for x in range(52)]

def shuffle(deck):
    """Perform a shuffle on given deck, return shuffled deck."""

    new = []
    while deck:
        card = deck.pop(0)      # get top card
        new.insert(0, card)     # put that card on top of new
        if len(deck):
            card = deck.pop(0)  # get next top card
            deck.append(card)   # put into bottom of the deck
    return new

print(f'deck={deck}')

orig = deck[:]      # get copy of original deck
count = 0

while True:
    count += 1
    deck = shuffle(deck)
    if deck == orig:
        break

print(f'count={count}')
print(f'deck={deck}')
