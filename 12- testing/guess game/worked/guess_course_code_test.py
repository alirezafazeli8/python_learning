import unittest
import guess_course_code


class TestGuess(unittest.TestCase):
    def test_input(self):
        guess = 1
        answer = 1
        result = guess_course_code.run_guess(guess, answer)
        self.assertTrue(result)

    # test incorrect number
    def test_incorrect_number(self):
        guess = 0
        answer = 1
        result = guess_course_code.run_guess(guess, answer)
        self.assertFalse(result)

    def test_string_input(self):
        result = guess_course_code.run_guess("11", 4)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
