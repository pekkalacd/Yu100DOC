"""
this module contains a generic version of 'any' mode (hard or difficult)
that is to be used in the day12.py
"""

import code.guessing_utils as utils
import os

def any_game(difficulty: str='easy') -> None:
    """
    conducts a guessing game in one of two modes {'easy','hard'}.
    easy mode allows 10 attempts. hard mode allows 5 attempts.
    other than that, all things are equal.
    """

    if difficulty not in {'easy','hard'}:
        raise ValueError(f"{difficulty} is not supported. Must be 'easy' or 'hard'")

    attempts = 10 if difficulty == 'easy' else 5
    original = attempts
    secret: int = utils.secret_number()
    guess = None

    while attempts > 0:

        guess: int = utils.make_guess()
        attempts -= 1

        if guess < secret:
            utils.too_low()

        elif guess > secret:
            utils.too_high()

        else:
            break

        utils.attempts_remaining(attempts)
    
    # user exhausted all attempts -> win / lose possible
    if attempts == 0:

        # user's last guess is right -> win
        if guess == secret:
            utils.win_msg(original, attempts)

        # last guess was wrong -> lose
        else:
            utils.lose_msg(original)

    # user didn't exhaust all attempts -> they won
    else:
        utils.win_msg(original,attempts)


def play_again() -> bool:
    """
    asks the user if they would like to play again,
    if so, returns True, False otherwise.
    """
    print("Would you like to play again? (Y|N)")
    while (ans := input().lower()) not in {'y','n'}:
        print("Ooof. I didn't get that. Say it again.")
        print("Would you like to play again? (Y|N)")
    return ans == 'y'

def clear_console() -> None:
    """
    clears the console output.
    """
    os.system("clear")

