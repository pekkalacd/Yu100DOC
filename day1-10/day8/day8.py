"""
Requirements: Caesar Cipher

1. Welcome message 

2. Ask user for encode or decode

3. Ask the user for an original message & shift amount -> do encryption

4. Ask the user for the encrypted message & shift amount -> do decryption.

5. Implement play again.
"""

import encrypt as encode
import decrypt as decode

def welcome() -> None:
    """
    welcomes the user to the caesar cipher
    """
    print("Welcome to the (Lowercase) Caesar Cipher\n")

def option_prompt() -> None:
    """
    presents a prompt to the user to encrypt or decrypt
    """
    print("Type 'encode' to encrypt. Type 'decode' to decrypt:")

def get_option() -> str:
    """
    gets the user's option to encode (encrypt) or decode (decrypt)
    and returns as a string
    """
    option_prompt()
    while (ans := input(">> ").lower()) not in {'encode','decode'}:
        print("Invalid option selected. Try again")
        option_prompt()
    return ans

def get_message() -> str:
    """
    gets the user's message that is to be encoded or decoded,
    and returns as a string
    """
    print("Type your message:")
    msg = input(">> ").lower()
    while any((not c.isalpha()) for c in msg):
        print("Invalid message. Must be all letters. No spaces or punctuation!")
        msg = input(">> ").lower()
    return msg

def get_shift() -> int:
    """
    gets the shift amount from the user as a non-negative integer
    and returns it
    """
    print("Type the shift amount:")
    while not (amt := input(">> ")).isdigit():
        print("Invalid amount. Shift amount must be non-negative integer.")
        print("Type the shift amount:")
    return int(amt)

def again() -> bool:
    """
    determines if the user would like to run the program again.
    returns True if so, otherwise False.
    """
    print("Would you like to do it again? (Y|N)")
    while (ans := input(">> ").lower()) not in {'y','n'}:
        print("Err. I don't understand.")
        print("Would you like to do it again? (Y|N)")
    return ans == 'y'

def single_round():

    user_choice = get_option()
    message = get_message()
    shift = get_shift()

    if user_choice == 'encode':
        cipher = encode.encrypt(message,shift)
        print(f"Here's the encoded result: {cipher}")
    else:
        original = decode.decrypt(message,shift)
        print(f"Here's the decoded result: {original}")


def loop():
    welcome()
    playing = True
    while playing:
        single_round()
        playing = again()

if __name__ == "__main__":
    loop()
