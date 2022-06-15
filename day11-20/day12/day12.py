"""
This module is the main guessing game.

Requirements: Guessing Game 

1. User is asked to play 'easy' or 'hard' mode
2. User gets a different amount of attempts per mode
3. Computer randomly picks a number [0,100] and the user has to guess in allotted attempts.
4. If they're successful, they win; else they lose.

"""

import code.game_utils as game


def get_difficulty() -> str:
    """
    asks the user if they would like to play in 'easy' or 'hard' mode.
    Returns the user's choice as a string
    """
    print("Type 'easy' to play in easy mode. Type 'hard' to play in hard mode.")
    while (opt := input().lower()) not in {'easy','hard'}:
        print(f"Oooof. {opt} isn't an option! Try again.")
        print("Type 'easy' to play in easy mode. Type 'hard' to play in hard mode.")
    return opt


def single_run() -> None:
    """
    conducts a single run of the game
    """
    difficulty = get_difficulty()
    game.any_game(difficulty=difficulty)


def loop() -> None:
    """
    conducts (possibly) multiple iterations of the game
    """
    playing = True
    while playing:
        single_run()
        playing = game.play_again()
        game.clear_console()


if __name__ == "__main__":
    loop()
