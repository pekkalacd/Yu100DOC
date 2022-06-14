"""
Part of day8 project Caesar Cipher

This module is responsible for decrypting the cipher
"""

import cipher_utils as utils

def decrypt(msg: str, shift: int) -> str:
    """
    decrypts a caesar cipher message with the specified
    shift amount and returns original message as a string
    """
    orig = ''
    for c in msg:
        idx = utils.look_up[c]
        orig += utils.lower[(idx-shift)%26]
    return orig
