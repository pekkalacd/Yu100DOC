"""
Utility module for the decrypt and encrypt modules for day8 caesar cipher

This module contains the lookup dictionary for the lowercase ascii letters.
Used for speed
"""

import string 


# dictionary for speedy look ups for indices
look_up: dict = dict(zip(string.ascii_lowercase, range(26)))

# string for index comparisons
lower: str = ''.join(look_up.keys())
