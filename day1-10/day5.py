"""
Requirements: Password Generator

1. Ask the user for the amount of letters they want in the password
2. Ask the user for the amount of symbols (punctuation) they want in the password
3. Ask the user for the amount of numbers they want in the password
4. Randomly generate a password and show to user
"""

import random
import string 

def how_many(category: str) -> int:
    print(f"How many {category} do you want in the password?")
    while not (ans := input()).isdigit():
        print(f"Ooof. {ans} is not a non-negative integer. Try again")
        print(f"How many {category} do you want in the password?")
    return int(ans)

def generate_letters(n: int) -> str:
    return ''.join(random.choices(string.ascii_letters,k=n))

def generate_symbols(n: int) -> str:
    return ''.join(random.choices(string.punctuation,k=n))

def generate_numbers(n: int) -> str:
    return ''.join(random.choices(string.digits,k=n))

def make_password() -> None:
    n_letters = how_many("letters")
    n_symbols = how_many("symbols")
    n_numbers = how_many("numbers")
    letters = generate_letters(n_letters)
    symbols = generate_symbols(n_symbols)
    numbers = generate_numbers(n_numbers)
    password = list(letters + symbols + numbers)
    random.shuffle(password)
    print(f"Here is your password: {''.join(password)}")

if __name__ == "__main__":
    make_password()
