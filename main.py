from Card import Card
from Deck import Deck
from Hand import Hand

def deal_dem_cards_boi():
    player = input("What's your name?")
    cards = input('How many cards do you want')
    deck = Deck()
    deck.shuffle()
    hand = Hand(player)
    deck.deal([hand],5)
    print(hand)

deal_dem_cards_boi()