"""
This is the unit test module for the ComputerHand class.

note:
    to run go to project dir day11/
    then
    python -m test.computer_test

"""

import unittest
from code.computer_hand import ComputerHand
from code.card_deck import BlackJackDeck,BlackJackCard

class TestComputerHand(unittest.TestCase):
    
    def test_creation(self):
        ch = ComputerHand()
        self.assertIsInstance(ch,ComputerHand)

    def test_repr_empty(self):
        ch = ComputerHand()
        self.assertEqual(str(ch),"ComputerHand([])")

    def test_get_score(self):
        ch = ComputerHand()
        self.assertEqual(ch.get_score(), 0)

    def test_add_card(self):
        card = BlackJackCard(suit="diamonds",value=10,face="K")
        ch = ComputerHand()
        ch.add_card(card)
        hand = ch._ComputerHand__hand
        self.assertEqual(hand[-1],card)

    def test_repr_one_card(self):
        card = BlackJackCard(suit="hearts",value=10,face="J")
        ch = ComputerHand()
        ch.add_card(card)
        self.assertEqual(str(ch),"ComputerHand([('?', '?', '?')])")

    def test_decision_hit(self):
        bjd = BlackJackDeck()
        ch = ComputerHand()
        card = bjd.top()
        ch.add_card(card)
        self.assertEqual(ch.decision(),"hit")

    def test_decision_stay(self):
        card1 = BlackJackCard(suit="hearts",value=10,face="J")
        card2 = BlackJackCard(suit="diamonds",value=9)
        ch = ComputerHand()
        ch.add_card(card1)
        ch.add_card(card2)
        self.assertEqual(ch.decision(),"stay")




if __name__ == "__main__":
    unittest.main()

