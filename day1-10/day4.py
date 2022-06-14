"""
Requirements

1. Implement a rock, paper, scissors game.
2. User will play against the computer.
3. Computer will have a random choice.
4. User will input their choice.
5. Count down will commence for both user and computer's choice to show.
6. Winner or tie should be determined.
7. User will be asked to play again.
"""

import random 

def display_menu() -> None:
    """
    displays the menu option for the user to enter either 0, 1, or 2,
    where 0 is Rock, 1 is Paper, and 2 is Scissors
    """
    available = ('Rock','Paper','Scissors')
    print("Choose from:")
    for i,option in enumerate(available):
        print(f"{i}\t{option}")
    print("")

def get_user_choice() -> str:
    """
    gets the user's option 0, 1, or 2, and returns it as a string
    """
    display_menu()
    while (ans := input("option: ")) not in {'0','1','2'}:
        print("Oooo. You must enter 0, 1, or 2")
        display_menu()
    return ans 

def get_computer_choice() -> str:
    """
    generates the computer's choice of 0, 1, or 2 and returns as a string
    """
    return random.choice('012')


def translate(number: str) -> str:
    """
    looks up the given number string and returns the option, where
    0 - Rock, 1 - Paper, 2 - Scissors, as a string.
    """
    mapp = {k:v for k,v in zip("012",("Rock","Paper","Scissors"))}
    return mapp[number]

def find_winner(user_num: str, computer_num: str) -> str:
    """
    determines whether the user has won against the computer.
    if the user has won, then 'user' is returned. if the computer
    has won, then 'computer' is returned. if the user and computer
    chose the same option then 'tie' is returned.
    """
    user_choice = translate(user_num)
    computer_choice = translate(computer_num)

    if user_choice == computer_choice:
        return 'tie'

    if user_choice == 'Rock':
        if computer_choice == 'Paper':
            return 'computer'
        if computer_choice == 'Scissors':
            return 'user'

    if user_choice == 'Paper':
        if computer_choice == 'Scissors':
            return 'computer'
        if computer_choice == 'Rock':
            return 'user'

    if user_choice == 'Scissors':
        if computer_choice == 'Rock':
            return 'computer'
        if computer_choice == 'Paper':
            return 'user'


def play_again() -> bool:
    """
    asks the user if they would like to play again.
    if so, then True is returned; otherwise, False.
    """
    print("\nWould you like to play again? (Y|N)")
    while (ans := input().lower()) not in {'y','n'}:
        print("Err. I do not understand. Try again.")
        print("Would you like to play again? (Y|N)")
    if ans == 'y':
        return True
    return False

def game_loop() -> None:
    """
    a game loop to conduct multiple rounds of rock, paper, scissors
    """
    playing = True
    while playing:
        print("Welcome to Rock, Paper, Scissors!\n")
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()
        print(f"User chooses: {translate(user_choice)}")
        print(f"Computer chooses: {translate(computer_choice)}")
        winner = find_winner(user_choice, computer_choice)
        if winner == 'tie':
            print("It appears there is a tie!")
        else:
            print(f"The winner is {winner}!")
        playing = play_again()


if __name__ == "__main__":
    game_loop()
