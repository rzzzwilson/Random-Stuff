# -*- coding: utf-8 -*-

import random

class Card(object):
    symbol = {'spider':'♠',
              'heart':'♥',
              'club':'♣',
              'diamond':'♦'}
    value = {1:'A',
             2:'2',
             3:'3',
             4:'4',
             5:'5',
             6:'6',
             7:'7',
             8:'8',
             9:'9',
             10:'10',
             11:'J',
             12:'Q',
             13:'K'}

    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return '{}{}'.format(Card.symbol.get(self.suit),Card.value.get(self.value))

def sort_poker(poker):
    p = sorted(poker,key=lambda card: (card.value, card.suit),reverse = True)
    return p


poker = []
s = ['spider','heart','club','diamond']
v = [x for x in range(1,14)]

for suit in s:
    for value in v:
        poker.append(Card(suit,value))

random.shuffle(poker)
poker = sort_poker(poker)

print(poker)
