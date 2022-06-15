"""
This module is for testing the BlackJackCardDeck in card_deck.py

note:

    to run go to project dir in day11/
    then do
    python -m test.deck_test
"""

import unittest
from code.card_deck import BlackJackDeck

class TestBlackJackDeck(unittest.TestCase):
    
    def test_creation(self):
        deck = BlackJackDeck()
        self.assertIsInstance(deck, BlackJackDeck)

    def test_deck_private_attr(self):
        deck = BlackJackDeck()
        self.assertTrue(hasattr(deck,'_BlackJackDeck__deck'))

    def test_shuffle(self):
        deck = BlackJackDeck()
        old = deck.deck.copy()
        deck.shuffle()
        new = deck.deck
        self.assertNotEqual(old,new)

    def test_top(self):
        deck = BlackJackDeck()
        first = deck.deck[0]
        self.assertEqual(first,deck.top())

    def test_bottom(self):
        deck = BlackJackDeck()
        last = deck.deck[-1]
        self.assertEqual(last,deck.bottom())

    def test_top_empty(self):
        deck = BlackJackDeck()
        for _ in range(52):
            _ = deck.top()
        self.assertIsNone(deck.top())

    def test_bottom_empty(self):
        deck = BlackJackDeck()
        for _ in range(52):
            _ = deck.bottom()
        self.assertIsNone(deck.bottom())

    def test_false_empty(self):
        deck = BlackJackDeck()
        for _ in range(40):
            _ = deck.top()
        self.assertFalse(deck.empty())

    def test_true_empty(self):
        deck = BlackJackDeck()
        for _ in range(52):
            _ = deck.top()
        self.assertTrue(deck.empty())



if __name__ == "__main__":
    unittest.main()
