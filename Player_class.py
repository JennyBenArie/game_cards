#import deckofcards and deal one
#import card
from random import choice


class Player:

    def __init__(self, player_name:str, num_of_cards:int):
        self.player_DeckOfCards = []
        self.player_name = player_name
        if 10 <= num_of_cards <= 26:
            self.num_of_cards = num_of_cards
        else:
            self.num_of_cards = 26


    def set_hand(self, deckofcards):
        deckofcards=#deckofcards
        for i in range(len(self.num_of_cards)):
            card = deckofcards.deal_one
            self.player_DeckOfCards.append(card)

    def get_card(self):
        one_card = choice(self.player_DeckOfCards)
        return one_card

    def add_card(self, card):
        self.player_DeckOfCards.append(card)


