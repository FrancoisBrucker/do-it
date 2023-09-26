import random

class Blackjack_methods():
    def __init__(self):
        self.newdeck()
    
    def newdeck(self):
        suits = ["diamonds", "clubs" ,"hearts", "spades"]
        values = range(1,14)
        initial_deck = []
        for suit in suits:
            for value in values:
                if value < 10:
                    initial_deck.append(Card(f"{value}_of_{suit}", value))
                if value >= 10:
                    initial_deck.append(Card(f"{value}_of_{suit}", 10))

        self.deck = initial_deck * 6
    
    def sum_hand(self, hand):
        if 1 in (card.value for card in hand):
            sum1 = sum([card.value for card in hand]) + 10
            if sum1 > 21:
                return(sum([card.value for card in hand]))
            else:
                return(sum1)
        else:
            return(sum([card.value for card in hand]))

class Card():
    def __init__(self, name, value):
        self.value = value
        self.name = name