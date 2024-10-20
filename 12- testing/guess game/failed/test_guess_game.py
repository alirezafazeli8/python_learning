# guess game
import guess_game
from guess_game import get_input_user, generate_random_num

# unit test
import unittest
from unittest.mock import patch


class TestGuessGame(unittest.TestCase):

    @patch("sys.argv", ["guess_game", 1, 2])
    def test_process_args_success(self):
        arg1, arg2 = get_input_user()
        self.assertEqual(arg1, 1)
        self.assertEqual(arg2, 2)

    def test_random_number(self):
        result = generate_random_num(2, 4)
        self.assertIsInstance(result, int)


unittest.main()
