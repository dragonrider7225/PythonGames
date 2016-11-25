"""This module provides base classes for a card and a deck of cards"""

import abc
from random import shuffle

__all__ = ["Deck", "Card", "PlayingCard", "create_playing_card_deck"]

"""The base class for a card."""
class Card:
    __metaclass__ = abc.ABCMeta

    """This method should return a str that contains the name of the
    card.
    """
    @abc.abstractmethod
    def get_name(self):
        return ""

"""A deck of cards."""
class Deck:
    def __init__(self, card_list):
        self.card_list = card_list

    def __len__(self):
        return len(self.card_list)

    """This method returns a list of instances of Card which
    represents the contents of the deck.
    """
    def get_card_list(self):
        return self.card_list

    """Remove the "top" card of the deck from the card list and return
    it.
    """
    def draw_card(self):
        if len(self.card_list) < 1:
            return None
        ret = self.card_list[0]
        self.card_list = self.card_list[1:]
        return ret

    """Shuffle the deck in place"""
    def shuffle(self):
        shuffle(self.card_list)

"""An implementation of the Card class for playing cards, i. e. ranks
of Ace through King and the four suits.
"""
class PlayingCard(Card):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def get_rank(self):
        if 1 < self.rank < 11:
            return str(self.rank)
        if self.rank is 1:
            return "Ace"
        if self.rank is 11:
            return "Jack"
        if self.rank is 12:
            return "Queen"
        if self.rank is 13:
            return "King"

    def get_suit(self):
        return self.suit

    def get_color(self):
        if self.suit == "Clubs" or self.suit == "Spades":
            return "black"
        if self.suit == "Hearts" or self.suit == "Diamonds":
            return "red"
        return None

    def get_name(self):
        return self.get_rank() + " of " + str(self.suit)

    def __str__(self):
        return self.get_name()

    def get_short_name(self):
        if self.get_rank() == "10":
            return "10" + str(self.suit)[0]
        return self.get_rank()[0] + str(self.suit)[0]

    def __repr__(self):
        return self.get_short_name()

"""create_playing_card_deck iterates through the thirteen ranks and four suits
of a standard deck of playing cards and returns a deck containing one instance
of each combination.
"""
def create_playing_card_deck():
    deck_list = []
    for rank in range(1, 14):
        for suit in ["Clubs", "Hearts", "Spades", "Diamonds"]:
            deck_list.append(PlayingCard(rank, suit))
    ret = Deck(deck_list)
    return ret
