import unittest
import guess


class TestGuessGame(unittest.TestCase):

    # test generate number is work
    def test_generate_number(self):
        test_param_one = 1
        test_param_two = 3
        result = guess.generate_number(test_param_one, test_param_two)

        self.assertEqual(result, int)

    # should return int (get user input function )
    def test_get_user_input_str_err(self):
        result = guess.get_user_input()
        self.assertIsInstance(result, int)


if __name__ == "__main__":
    unittest.main()
