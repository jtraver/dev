#!/usr/bin/env python3
#!/usr/bin/python3

import random

def get_bid(hands):
    bids = []
    for index in xrange(0, 4):
        hand = hands[index]
        print "hand = %s" % str(hand)
        bid = {}
        bid['bid'] = 'pass'
        for suit in ['S', 'C', 'D', 'H', 'NT']:
            bid[suit] = 0
        if 'JOKER' in hand:
            bid['NT'] += 1
            bid['bid'] = '6NT'
        for suit in ['S', 'C', 'D', 'H']:
            for icard in xrange(0, len(hand)):
                card = hand[icard]
                if card.endswith(suit):
                    bid[suit] += 1
                    if card.startswith('J'):
                        bid['bid'] = '6' + suit
        if 'JOKER' in hand:
            if 'JH' in hand and 'JD' in hand:
                bid['bid'] = '8H'
                if bid['D'] > bid['H']:
                    bid['bid'] = '8D'
            if 'JC' in hand and 'JS' in hand:
                bid['bid'] = '8C'
                if bid['S'] > bid['C']:
                    bid['bid'] = '8S'
        else:
            if 'JH' in hand and 'JD' in hand:
                bid['bid'] = '7H'
                if bid['D'] > bid['H']:
                    bid['bid'] = '7D'
            if 'JC' in hand and 'JS' in hand:
                bid['bid'] = '7C'
                if bid['S'] > bid['C']:
                    bid['bid'] = '7S'
        bids.append(bid)
    return bids

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

def old_get_bid(hands):
    bids = []
    for index in xrange(0, 4):
        hand = hands[index]
        print "hand = %s" % str(hand)
        bid = {}
        for suit in ['S', 'C', 'D', 'H']:
            bid[suit] = []
        bid['JOKER'] = None
        bid['bid'] = 'pass'
        bids.append(bid)
        for icard in xrange(0, len(hand)):
            card = hand[icard]
            if card == 'JOKER':
                bid['JOKER'] = card
                bid['bid'] = '6NT'
            elif card.startswith('J'):
                for suit in ['S', 'C', 'D', 'H']:
                    if card.endswith(suit):
                        bid[suit].append(card)
                        bid['bid'] = '6' + suit
    return bids

def main():
    deck = create_deck()
    # print "deck = %s" % str(deck)
    hands = deal(deck)
    for index in xrange(0, 5):
        shand = hands[index]
        print "%s %s" % (str(index), str(shand))
    # print "hands = %s" % str(hands)
    print "your hand = %s" % str(hands[3])
    bids = get_bid(hands)
    # print "bids = %s" % str(bids)
    for index in xrange(0, 4):
        shand = bids[index]
        bid = shand['bid']
        print "bid = %s in %s" % (str(bid), str(shand))

main()
