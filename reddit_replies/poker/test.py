# -*- coding: utf-8 -*-

import random

class Card(object):
    value_suit = {4: '♠', 3: '♥', 2: '♣', 1: '♦'}
    suit_value = {'spider': 4, 'heart': 3, 'club': 2, 'diamond': 1}

    face_value = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                  '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 12}
    value_face = {1: 'A', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
                  8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q', 13: 'K'}

    def __init__(self, suit, value):
        self.suit = Card.suit_value[suit]
        self.value = value

    def __lt__(self, other):
        result = self.value < other.value
        if not result:
            if self.value == other.value:
                result = self.suit < other.suit
        return result

    def __gt__(self, other):
        result = self.value > other.value
        if not result:
            if self.value == other.value:
                result = self.suit > other.suit
        return result

    def __repr__(self):
        return '{}{}'.format(Card.value_suit[self.suit], Card.value_face[self.value])

def sort_poker(poker):
    p = sorted(poker, reverse = True)
    return p


poker = []
s = ['spider', 'heart', 'club', 'diamond']
v = [x for x in range(1, 14)]

for suit in s:
    for value in v:
        poker.append(Card(suit, value))

random.shuffle(poker)
poker = sort_poker(poker)

print(poker)
