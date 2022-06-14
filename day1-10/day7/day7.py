"""
Requirements: Hangman

1. There should be a visual of the hangman itself

2. There should be a visual of the spaces that have been filled / unfilled

3. User will guess 1 letter at a time, if they guess correctly, the letter should show 
up in the spaces allotted and should not add a piece to the hangman; if they guess incorrectly,
then a body part will be added to the hangman. Each should update the visual.

4. A congratulatory or losing message should be shown at the end of the game.

5. There should be a play again option, where another random word will be generated.
"""

import random 
import hangman_words as words
import hangman_art as art 

def display_logo() -> None:
    print(art.logo)

def generate_word() -> str:
    return random.choice(words.word_list)

def make_spaces(word: str) -> list:
    return ['_' for _ in range(len(word))]

def display_spaces(spaces: list) -> None:
    for space in spaces:
        print(space,end=" ")

def guess_letter() -> str:
    guess = input("Guess a letter: ").lower()
    while len(guess) > 1 or (not guess.isalpha()):
        print("You must guess 1 letter")
        guess = input("Guess a letter: ").lower()
    return guess 

def is_correct(letter: str, word: str) -> bool:
    return letter in word

def fill_spaces_with_letter(letter: str, word: str, spaces: list) -> None:
    for i,ch in enumerate(word):
        if ch == letter:
            spaces[i] = letter

def is_win(spaces: list, word: str) -> bool:
    return ''.join(spaces) == word

def is_loss(stage_pos: int) -> bool:
    return stage_pos == len(art.stages)-1

def play_again() -> bool:
    print("\nWould you like to play again? (Y|N)")
    while (ans := input().lower()) not in {'y','n'}:
        print("Err. I don't know what you mean. Try again.")
        print("\nWould you like to play again? (Y|N)")
    return ans == 'y'

def single_game():

    # display the logo
    display_logo()

    # get any letter to begin
    print("Press any letter to begin")
    while not input().isalpha():
        pass
    print("")

    # create the stages list & stage position tracker
    stages = art.stages.copy()[::-1]
    stage_pos = 0

    # generate a word & get the spaces 
    word = generate_word()
    spaces = make_spaces(word)

    # continue until win/lose result
    result = None
    while result is None:

        # display the spaces
        display_spaces(spaces)

        # display the stage of hangman
        print(stages[stage_pos])

        # get the user's guess
        guess = guess_letter()

        # guess is right -> add letter to spaces
        # guess is wrong -> add +1 to stage position
        if is_correct(guess, word):
            fill_spaces_with_letter(guess, word, spaces)
        else:
            stage_pos += 1

        # there is a winner -> result is 'Win'
        if is_win(spaces, word):
            result = 'win'

        # there is a loser -> result is 'lose'
        if is_loss(stage_pos):
            print("\nHang Man!")
            print(stages[stage_pos])
            result = 'lose'

    print(f"The word was {word}")
    print(f"You {result}!\n")


def loop():
    playing = True
    while playing:
        single_game()
        playing = play_again()


if __name__ == "__main__":
    loop()
