"""
This module is for testing the BlackJackCard class in card_deck.py

note:
    to run go to
    project directory in day11/
    then 
    python -m test.card_test

"""

import unittest
from code.card_deck import BlackJackCard, BJCardComparisonError

class TestBlackJackCard(unittest.TestCase):

    def test_create_card_non_ace(self):
        card = BlackJackCard(suit="spades",value=10)
        self.assertIsInstance(card, BlackJackCard)

    def test_create_card_as_ace(self):
        card = BlackJackCard(suit="hearts",value=(1,11),face="A")
        self.assertIsInstance(card, BlackJackCard)

    def test_card_repr(self):
        card = BlackJackCard(suit="diamonds",value=10)
        self.assertEqual(str(card),"(diamonds,10,None)")

    def test_card_has_att_suit(self):
        card = BlackJackCard(suit="hearts",value=2)
        self.assertTrue(hasattr(card,'suit'))

    def test_card_has_att_value(self):
        card = BlackJackCard(suit="hearts",value=2)
        self.assertTrue(hasattr(card,'value'))

    def test_card_has_att_face(self):
        card = BlackJackCard(suit="hearts",value=10, face='J')
        self.assertTrue(hasattr(card,'face'))

    def test_throws_compare_error(self):
        card = BlackJackCard(suit="hearts",value=10,face="K")
        value = 20
        self.assertRaises(BJCardComparisonError, lambda: card == value)

    def test_same_card_equal(self):
        card = BlackJackCard(suit="spades",value=10,face='K')
        self.assertEqual(card,card)

    def test_different_card_not_equal(self):
        card1 = BlackJackCard(suit="spades",value=10,face='K')
        card2 = BlackJackCard(suit="hearts",value=10,face='K')
        self.assertNotEqual(card1,card2)

    def test_gt_card(self):
        card1 = BlackJackCard(suit="spades",value=10)
        card2 = BlackJackCard(suit="spades",value=4)
        self.assertGreater(card1, card2)

    def test_lt_card(self):
        card1 = BlackJackCard(suit="hearts",value=3)
        card2 = BlackJackCard(suit="diamonds",value=10)
        self.assertLess(card1, card2)


if __name__ == "__main__":
    unittest.main()
