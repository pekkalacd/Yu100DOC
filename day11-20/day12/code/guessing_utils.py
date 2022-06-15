"""
common utility module for the guessing game between hard & easy modes.

"""

import random

def too_low() -> None:
    """
    displays a message that the number provided was too low & asks to guess again
    """
    print("Too low!")
    print("Guess again.")


def too_high() -> None:
    """
    displays a message that the number provided was too high & asks to guess again
    """
    print("Too high!")
    print("Guess again.")


def make_guess() -> int:
    """
    asks the user for their guess and returns it as an integer
    """
    while not (guess := input("Make a guess: ")).isdigit():
        print("Guess must be non-negative integer.")
    return int(guess)


def attempts_remaining(attempts: int) -> None:
    """
    displays how many attempts remain for the user to guess the number.
    """
    print(f"You have {attempts} attempts remaining.")


def secret_number() -> int:
    """
    generates an integer 0 to 100 (inclusive) and returns as int
    """
    return random.choice(range(101))

def win_msg(original: int, remaining: int) -> None:
    """
    displays a congratulatory message that the guess was got in (original-remaining) amt 
    of attempts and that remaining attempts were unused
    """
    print(f"You got the number in {original-remaining} attempts with {remaining} to spare!")

def lose_msg(original: int) -> None:
    """
    displays a message stating the user lost
    """
    print(f"You exhausted all {original} attempts to no avail. You lose!")


