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
    deck.append('JOKER')
    return deck

def deal_card(deck):
    # print "deck = %s" % str(deck)
    index = random.randint(0, len(deck) - 1)
    # print "index = %s" % str(index)
    card = deck[index]
    while card == None:
        index = random.randint(0, len(deck) - 1)
        # print "index = %s" % str(index)
        card = deck[index]
    deck[index] = None
    return card

def deal(deck):
    hands = []
    for index in xrange(0, 5):
        # print "index = %s" % str(index)
        hands.append([])
    for index in xrange(0, len(hands)):
        for card in xrange(0, 3):
            hands[index].append(deal_card(deck))
    for index in xrange(0, len(hands)):
        for card in xrange(0, 2):
            hands[index].append(deal_card(deck))
    for index in xrange(0, len(hands) - 1):
        for card in xrange(0, 3):
            hands[index].append(deal_card(deck))
    for index in xrange(0, len(hands) - 1):
        for card in xrange(0, 2):
            hands[index].append(deal_card(deck))
    # print "hands = %s" % str(hands)
    return hands

def bid(hands):
    bids = []
    for index in xrange(0, 4):
        hand = hands[index]
        print "hand = %s" % str(hand)
        bid = {}
        bids.append(bid)
    return bids

def main():
    deck = create_deck()
    # print "deck = %s" % str(deck)
    hands = deal(deck)
    # print "hands = %s" % str(hands)
    print "your hand = %s" % str(hands[3])
    bids = bid(hands)
    print "bids = %s" % str(bids)

main()
