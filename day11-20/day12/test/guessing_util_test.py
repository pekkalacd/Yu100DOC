"""
This module tests the functions contained in guessing_utils.py.
That module is also used inside of game_utils.py for the any_game function, heavily.

note:

    to run go to project dir 'day12'
    then do
    python -m test.guessing_util_test


"""

import unittest
import unittest.mock
import io
import code.guessing_utils as utils

class TestingGuessingUtils(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, func, mock_stdout, args: tuple=(), expected: str=""):
        func(*args)
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_too_low(self):
        self.assert_stdout(utils.too_low, expected="Too low!\nGuess again.\n")

    def test_too_high(self):
        self.assert_stdout(utils.too_high, expected="Too high!\nGuess again.\n")

    def test_secret(self):
        self.assertIsInstance(utils.secret_number(),int)

    def test_win_msg(self):
        msg="You got the number in 5 attempts with 5 to spare!\n"
        self.assert_stdout(utils.win_msg, args=(10,5), expected=msg)

    def test_lose_msg(self):
        msg="You exhausted all 10 attempts to no avail. You lose!\n"
        self.assert_stdout(utils.lose_msg, args=(10,), expected=msg)

    def test_attempts_remaining(self):
        msg="You have 8 attempts remaining.\n"
        self.assert_stdout(utils.attempts_remaining, args=(8,),expected=msg)

if __name__ == "__main__":
    unittest.main()
