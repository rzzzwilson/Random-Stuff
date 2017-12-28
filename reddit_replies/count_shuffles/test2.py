#!/usr/bin/env python3

"""
Solve the puzzle vaguely described in:

https://www.reddit.com/r/learnpython/comments/7mdmfh/can_anyone_solve_this_question/

Solve it recursively (new requirement).  This version shuffles recursively.
The problem may require that we do the *counting* recursively.
"""

"""
The shuffle() function takes 'deck' (the deck to shuffle) and 'top' (the top
deck).  The top-most call will have 'top' empty.  The top two cards are
manipulated as in the iterative solution.  If 'deck' is not empty we call
shuffle() again passing current 'deck' and 'top'.  If 'deck' is empty we just
return the shuffled deck (ie, 'top').

This is recursion used to loop, which is fairly boring and not the way recursion
should really be used.  Use iteration instead.  As an exercise in simple
recursion including the trick of a default param that isn't passed initially, it
has some merit.
"""

def shuffle(deck, top=None):
    """Perform a shuffle on given deck, return shuffled deck (ie, 'top')."""

    if top is None:         # if not given, assume 'top' is empty (ie, [])
        top = []

    card = deck.pop(0)      # get top card
    top.insert(0, card)     # put that card on top of 'top' deck
    if deck:
        card = deck.pop(0)  # get next top card
        deck.append(card)   # put into bottom of the deck

    if deck:                # not finished shuffling
        shuffle(deck, top)

    return top              # finished, return "top"

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
