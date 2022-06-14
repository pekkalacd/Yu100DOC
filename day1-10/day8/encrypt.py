"""
Part of the day8 exercise for Caesar Cipher

This module is responsible for creating the encryption mechanism
"""

import cipher_utils as utils 

def encrypt(msg: str, shift: int) -> str:
    """
    performs caesar cipher encryption on the given msg
    with the specified shift amount and returns the encrypted string
    """
    cipher = ''
    for c in msg:
        idx = utils.look_up[c]
        cipher += utils.lower[(idx+shift)%26]
    return cipher

