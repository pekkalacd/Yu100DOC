"""
Requirements: Silent Auction

1. Each user enters their name and the bid
2. If there is more than one user, then for each user, the console is cleared.
3. When all users have been entered, the maximum bid is calculated.
4. The user's name and their bid for the max bid must be displayed
5. This program utilizes dictionaries
"""

import os
from typing import Tuple

def is_there_another_bidder() -> bool:
    """
    prompts the user to type 'y' for another bidder & bid to be added
    or 'n' to stop adding bidders. returns True if the user wants another bidder.
    False, otherwise.
    """
    print("Type 'y' if you'd like to add another bidder & bid. Type 'n' if not")
    while (ans := input(">> ").lower()) not in {'y','n'}:
        print(f"Ooof. {ans} is invalid. Please try again")
        print("Type 'y' if you'd like to add another bidder & bid. Type 'n' if not")
    return ans == 'y'

def get_name() -> str:
    """
    gets the name of the bidder and returns as string
    """
    name = input("What is your name? ")
    return name 

def get_bid() -> float:
    """
    gets the bid amount from the current bidder and returns as float
    """
    bid = input("What is your bid? ")
    try:
        bid = float(bid)
        if bid < 0:
            raise ValueError
        return bid
    except ValueError:
        print(f"{bid} is an invalid amount. Must be non-negative and numerical!")
        return get_bid()

def add_bidder(all_bidders: dict, name: str, bid: float) -> None:
    """
    adds the current bidder name and bid amount as a (key,value) pair
    in the all_bidders dictionary, in-place (mutable)
    """
    all_bidders[name] = bid 

def find_max_bidder(all_bidders: dict) -> Tuple[str,float]:
    """
    finds the name and bid amount of the highest bidder within
    the all_bidders dictionary, returns as a 2-tuple 
    """

    max_bidder = None
    max_bid = float('-inf')

    for name,bid in all_bidders.items():
        if bid > max_bid:
            max_bid = bid
            max_bidder = name

    return max_bidder,max_bid

def clear() -> None:
    """
    clears the console output
    """
    os.system('clear')


def play_again() -> bool:
    """
    asks the user if they would like to launch the program again.
    returns True if so, False otherwise
    """
    print("Would you like to do this again? (Y|N)")
    while (ans := input(">> ").lower()) not in {'y','n'}:
        print(f"Ooooof. {ans} isn't right. Try again")
        print("Would you like to do this again? (Y|N)")
    return ans == 'y'

def single_run() -> None:
    """
    performs a single run of this program
    """
    all_bidders = {}
    while is_there_another_bidder():
        clear()
        name = get_name()
        bid = get_bid()
        add_bidder(all_bidders,name,bid)
    clear()
    if all_bidders == {}:
        print("There are no bidders! No one wins!")
    else:
        print("All bidders have been added. Calculating...\n")
        max_bidder, max_bid = find_max_bidder(all_bidders)
        print(f"The max bidder is {max_bidder} with a bid of ${max_bid:,.2f}")


def loop() -> None:
    """
    performs (possibly) multiple iterations of game play
    """
    playing = True 
    while playing:
        single_run()
        clear()
        playing = play_again()

if __name__ == "__main__":
    loop()
