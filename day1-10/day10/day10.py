"""
Requirements: Simple Calculator App

1. Display a logo
2. Ask the user to select an operation (binary operands)
3. Ask the user for two numbers
4. Perform the operation on them
5. Save the result for the next calculation, should the user select option 'y',
   else if option 'n' is chosen, clear result output for new calculation.
"""

import ascii_art as art
import os
from typing import Union, Sequence

def display_logo() -> None:
    """
    displays the logo from ascii_art module for the calculator
    """
    print(art.logo)

def get_operand(place: str) -> Union[int,float]:
    """
    asks the user for a number where place is either 'first' or 'next',
    returns that number as either a float or int
    """
    operand = input(f"What's the {place} number? ")
    try:
        op = float(operand)
        if op % 1 == 0:
            return int(op)
        return op
    except ValueError:
        print(f"{operand} is an invalid number. Must be int or float")
        return get_operand(place)

def display_operators(operators: Sequence) -> None:
    """
    displays the operator options for the user to select
    """
    print(*operators,sep="\n")

def get_operator(*operators: Union[int,float]) -> str:
    """
    user chooses an operation from the available operands sequence,
    returns the user's choice as a string
    """
    display_operators(operators)
    choice = input("Pick an operator: ")
    while choice not in operators:
        print(f"{choice} is an invalid operation. Try again")
        display_operators(operators)
        choice = input("Pick an operator: ")
    return choice

def again(prompt, current_result: Union[int,float]=None) -> bool:
    """
    asks if the user would like to do whatever the prompt suggests again.
    This is generalized. current_result is optional, as this will be used for both playing again (entirely)
    and continuing the calculation.
    """
    print(prompt)
    while (ans := input(">> ").lower()) not in {'y','n'}:
        print(f"Oooof. {ans} is not a satisfiable response. Try again")
    return ans == 'y'

def single_run() -> None:
    """
    conducts a single run of the program
    """
 
    keep_going = True
    result = get_operand(place="first")
    ops = ('+','-','*','/','//','**','%')
    
    while keep_going:
        operator = get_operator(*ops)
        next_num = get_operand(place="next")
        print("")
        try:
            og = result
            result = eval(f"{result}{operator}{next_num}")
            print(f"{og} {operator} {next_num} = {result}")
        except ZeroDivisionError:
            print("Cannot divide by zero! Calculation not performed! Try again")
            continue
        pmpt = f"Type 'y' to continue calculating with {result}, type 'n' to quit current run"
        keep_going = again(prompt=pmpt, current_result=result)


def loop() -> None:
    """
    conducts (possibly) multiple iterations of single runs of the program
    """
    playing = True
    clear = lambda: os.system("clear")
    while playing:
        clear()
        display_logo()
        single_run()
        playing = again("Want to play again? (Y|N)")
    print("")
    print("Thanks for playing!")



if __name__ == "__main__":
    loop()

    
