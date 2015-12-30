#!/usr/bin/python

import random

def create_deck():
    deck = []
    for suit in ['S', 'C', 'D', 'H']:
        deck.append('A' + suit)
        deck.append('J' + suit)
        deck.append('Q' + suit)
        deck.append('K' + suit)
        for card in xrange(4, 11):
            deck.append(str(card) + suit)
    deck.append('J')
    return deck

def main():
    deck = create_deck()
    print "deck = %s" % str(deck)

main()
