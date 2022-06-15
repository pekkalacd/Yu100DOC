"""
This module supports a simple ComputerHand (dealer) AI.

"""

import random
from code.card_deck import BlackJackCard, BlackJackDeck
from typing import Union, Type, List

class ComputerHand(object):

    __slots__ = ("_ComputerHand__score", "_ComputerHand__hand")

    def __init__(self):
        self.__hand = []
        self.__score = 0

    def __repr__(self) -> str:
        """
        displays all cards in the computer's hand except the most recent one
        """
        if not self.is_empty():
            return f"ComputerHand({self.__hand[:-1]+[('?','?','?')]})"
        else:
            return "ComputerHand([])"

    def get_score(self) -> int:
        """
        for calculating who won in the end
        """
        return self.__score


    def show_all(self) -> None:
        """
        shows all of the cards in the computer's hand,
        used for the climax of the game, when a winner is to be determined.
        """
        print(f"ComputerHand({self.__hand})")


    def is_empty(self) -> bool:
        """
        returns true if the computer's hand is empty; false otherwise
        """
        return len(self.__hand) == 0

    def add_card(self, card: BlackJackCard) -> Union[None,Type[Exception]]:
        """adds a card to the computer's hand and increments score"""
        
        if not isinstance(card, BlackJackCard):
            raise ValueError("ComputerHand must only contain BlackJackCard objects")

        self.__hand.append(card)
        if isinstance(card.value,tuple):
            self.__score += card.value[random.randint(0,1)]
        else:
            self.__score += card.value

    def decision(self) -> str:
        """
        simple decision function, if the computer's hand < 17 -> "hit",
        if it's >= 17 "stay"
        """
        return "hit" if self.__score < 17 else "stay"
        
