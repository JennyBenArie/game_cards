#import deckofcards
from Player_class import Player



class CardGame:
    def __init__(self, playername1, playername2, num_cards1, num_cards2):
        self.player1=Player(playername1,num_cards1)
        self.player2=Player(playername2,num_cards2)
        self.deck=#DeckOfCards
        self.new_game()

    def __new_game(self):
        shuff=self.deck.card_shuflle
        one=Player.set_hand(self.player1, shuff)
        two=Player.set_hand(self.player2, shuff)

    def get_winner(self):
        if self.player1.num_of_cards>self.player2.num_of_cards:
            return f"{self.player1.player_name}, is the winner!"
        elif self.player2.num_of_cards>self.player1.num_of_cards:
            return f"{self.player2.player_name}, is the winner!"
        else:
            return None