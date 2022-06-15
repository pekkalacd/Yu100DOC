"""
Requirements: Black Jack Game 

1. Implement a black jack game
2. User vs the computer (dealer)
3. Bust @ over 21, player closest to 21 (without going over) wins
4. User gets to select "hit" (draw another card) or "stay" (don't draw another card)
5. Computer (dealer) always plays as best as possible
6. Deck is limited per game, shuffled after every move.

Additional Features:
    - Card & Deck is implemented in OOP
    - Unit tests written for each of the classes 
 """

import random
import code.black_jack_art as art
from code.card_deck import BlackJackDeck, BlackJackCard
from code.computer_hand import ComputerHand
from typing import Union, List

def display_logo() -> None:
    """
    displays the logo for the Black Jack game from black_jack_art.py
    """
    print(art.logo)

def get_name() -> str:
    """
    gets the name of the user and returns as a string
    """
    return input("Enter your name: ")


def draw_card(deck: BlackJackDeck) -> BlackJackCard:
    """
    draws one card from the deck.
    50%/50% chance to draw from top or bottom.
    deck is shuffled after each draw.
    """
    card = None
    if random.randint(0,1):
        card = deck.top()
    else:
        card = deck.bottom()
    deck.shuffle()
    return card

def hit_or_stay() -> str:
    """
    asks the user if they would like to hit or stay
    """
    print("Type 'hit' to add a card to your hand. Type 'stay' to stay where you are")
    while (ans := input().lower()) not in {'hit','stay'}:
        print("Oooof. I don't know what you mean")
        print("Type 'hit' to add a card to your hand. Type 'stay' to stay where you are")
    return ans

def show_limited(user_name: str, user_hand: List[BlackJackCard], dealer: ComputerHand) -> None:
    """
    shows a limited view of the cards at play,
    including all of the user's cards and all but 1 of the dealer's cards
    """
    print(f"{user_name}'s Hand: {user_hand}")
    print(dealer)
    print("")

def show_all(user_name: str, user_hand: List[BlackJackCard], dealer: ComputerHand) -> None:
    """
    shows all of the cards the user has to the console along with all of dealer's hand
    """
    print("\nFinal Hand")

    print(f"{user_name}'s Hand: {user_hand}")
    dealer.show_all()
    print("")

def ace_handler(card: BlackJackCard) -> int:
    """
    asks the user if they would like to play an ace as a 1 or 11
    """
    print(f"You have an ace, {card}, would you like to play this as a 1 or 11")
    while (ans := input()) not in {'1','11'}:
        print("Oooof. I do not know what you mean. Try again.")
        print(f"You have an ace, {card}, would you like to play this as a 1 or 11")
    return int(ans)


def calculate_user_score(user: List[BlackJackCard]) -> int:
    """
    calculates the current score for the user's hand and returns as integer.
    """
    user_score = 0
    for card in user:
        if isinstance(card.value,int):
            user_score += card.value
        elif isinstance(card.value,tuple):
            user_score += ace_handler(card)
    return user_score


def check_bust(score: int) -> bool:
    """
    determines if the given user_type's (user_name or dealer) score is a bust (> 21)
    """
    if score > 21:
        return True
    return False


    
def who_won(user_name: str, user: List[BlackJackCard], dealer: ComputerHand) -> str:
    """
    determines who the winner of the BlackJack game is.
    adds the scores of each of the user and dealer's decks.
    returns a string user_name if user won, otherwise, 'dealer' or 'draw' if no one won
    """
    user_score = calculate_user_score(user)
    dealer_score = dealer.get_score()

    print(f"{user_name}'s Hand Score: {user_score}")
    print(f"dealer's Hand Score: {dealer_score}")

    # no one has busted -> closest to 21 wins
    proximity_user = 21-user_score
    proximity_dealer = 21-dealer_score

    # both are equally close to 21 -> no one wins
    if proximity_user == proximity_dealer:
        return "draw"

    # dealer is closer to 21 -> dealer wins
    if min(proximity_user, proximity_dealer) == proximity_dealer:
        return "dealer"

    # otherwise -> user wins
    return user_name


def play_again() -> bool:
    """
    asks the user if they'd like to play again.
    returns True if so; False, otherwise.
    """
    print("Would you like to play again? (Y|N)")
    while (ans := input(">> ").lower()) not in {'y','n'}:
        print("Oooof. I don't understand. Try again.")
        print("Would you like to play again? (Y|N)")
    return ans == 'y'


def single_round() -> None:
    """
    responsible for conducting a single round of blackjack
    """
    # create deck & computer hand
    bjd = BlackJackDeck()
    dealer_hand = ComputerHand()
    
    # display blackjack logo & get name
    display_logo()
    print("")
    user_name = get_name()

    # user's hand
    user_hand = []

    # initially, deal 2 cards each to user & computer
    for i in range(4):
        card = draw_card(bjd)
        if i % 2 == 0:
            dealer_hand.add_card(card)
        else:
            user_hand.append(card)
    
    winner = None
    while winner is None and bjd.deck:

        # display the cards in each hand (limited for dealer)
        show_limited(user_name, user_hand, dealer_hand)

        # each player makes a decision to 'hit' or 'stay'
        user_decision = hit_or_stay()
        dealer_decision = dealer_hand.decision()

        if user_decision == 'hit':
            card = draw_card(bjd)
            user_hand.append(card)
        
        if dealer_decision == 'hit':
            card = draw_card(bjd)
            dealer_hand.add_card(card)

        if user_decision == 'stay' and dealer_decision == 'stay':
            show_all(user_name, user_hand, dealer_hand)
            winner = who_won(user_name, user_hand, dealer_hand)

        is_user_bust = check_bust(calculate_user_score(user_hand))
        is_dealer_bust = check_bust(dealer_hand.get_score())

        if is_user_bust and (not is_dealer_bust):
            print(f"{user_name} has busted!")
            show_all(user_name, user_hand, dealer_hand)
            winner = 'dealer'

        if is_dealer_bust and (not is_user_bust):
            print("dealer has busted!")
            show_all(user_name, user_hand, dealer_hand)
            winner = user_name

    print(f"The winner is {winner}")


def loop() -> None:
    """
    responsible for (possibly) conducting multiple iterations of blackjack
    """
    playing = True
    while playing:
        single_round()
        playing = play_again()


if __name__ == "__main__":
    loop()
        

        

