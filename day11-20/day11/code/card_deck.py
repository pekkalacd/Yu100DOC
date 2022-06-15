"""
This module is responsible for creating the initial deck of cards
"""

import random
from typing import Union,Type,Tuple

class BJCardComparisonError(Exception):
    """
    Custom Exception thrown when a BlackJackCard object is being 
    compared with something other than a BlackJackCard object
    """

    def __init__(self):
        super().__init__("Card objects can only be compared with other Card objects")


class BlackJackCard(object):
    """
    A class describing a BlackJackCard

    attributes:

        + suit: the suit of the card (str)
        + value: the value of the card (int or tuple[int,int])
        + face: (optional) for a given face card

    methods:

        + __gt__ : allows > to act on the instance
        + __lt__ : allows < to act on the instance
        + __eq__ : allows == to act on the instance
        + __hash__ : makes instance immutable 
    """

    __slots__ = ('_BlackJackCard__suit', '_BlackJackCard__value', '_BlackJackCard__face')

    def __init__(self, suit: str, value: Union[int,Tuple[int,int]], face: str=None):
        self.__suit = suit
        self.__value = value
        self.__face = face

    @property
    def suit(self) -> str:
        return self.__suit
    
    @property
    def value(self) -> Union[int,Tuple[int,int]]:
        return self.__value 

    @property
    def face(self) -> Union[None,str]:
        return self.__face

    def __repr__(self) -> str:
        return f"({self.suit},{self.value},{self.face})"

    def __eq__(self, other: 'BlackJackCard') -> bool:
        if not isinstance(other, type(self)):
            raise BJCardComparisonError
        return all((self.suit == other.suit, self.value == other.value, self.face == other.face))

    def __gt__(self, other: 'BlackJackCard') -> bool:
        if not isinstance(other, type(self)):
            raise BJCardComparisonError
        return self.value > other.value

    def __lt__(self, other: 'BlackJackCard') -> bool:
        if not isinstance(other, type(self)):
            raise BJCardComparisonError
        return self.value < other.value 


class BlackJackDeck(object):
    """
    A class describing a BlackJackDeck comprised on BlackJackCards

    attributes:
          
          - deck : a list containing all of the black jack cards
    
    properties:

          + deck : immutable view of the black jack deck

    methods:

          + shuffle: implements random.shuffle for this card deck
          + top: if non-empty, pops the top card off the deck and returns it
          + bottom: if non-empty, pops the bottom card off the deck and returns it
          + empty: returns True if the deck is empty, otherwise False
    """

    __slots__ = ('_BlackJackDeck__deck')
          
    def __init__(self):
        suits = ['hearts','diamonds','clubs','spades']
        values = list(range(2,11)) + [('J',10),('Q',10),('K',10),('A',(1,11))]
        self.__deck = []
        for suit in suits:
            for value in values:
                if isinstance(value,tuple):
                    inst = BlackJackCard(suit=suit,value=value[1],face=value[0])
                else:
                    inst = BlackJackCard(suit=suit,value=value)
                self.__deck.append(inst)

    @property
    def deck(self) -> list:
        return self.__deck

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def top(self) -> Union[None,BlackJackCard]:
        try:
            return self.deck.pop(0)
        except IndexError:
            return
    
    def bottom(self) -> Union[None,BlackJackCard]:
        try:
            return self.deck.pop()
        except IndexError:
            return

    def empty(self) -> bool:
        return len(self.deck) == 0




