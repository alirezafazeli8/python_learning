import unittest
import main


# class TestMain(unittest.TestCase):
#     def test_do_stuff(self):
#         test_param = 8
#         result = main.do_stuff(test_param)
#         self.assertEqual(result, 13)

#     def test_do_stuff2(self):
#         test_param = "a"
#         result = main.do_stuff(test_param)
#         # self.assertEqual(result, test_param)
#         self.assertTrue(isinstance(result, Error))


# unittest.main()


class TestStuff(unittest.TestCase):
    def test_number(self):
        result = main.do_stuff(2)
        self.assertEqual(result, 4)

    def test_negative(self):
        result = main.do_stuff(-2)
        self.assertTrue(result)
        # self.assertEqual(result, -(2**2))

    def test_zero(self):
        result = main.do_stuff(0)
        self.assertTrue(result)
        # self.assertEqual(result, 0**2)


class TestStuff2(unittest.TestCase):
    def test_type(self):
        result = "a"
        self.assertRaises(TypeError, main.do_stuff_2, result)


unittest.main()
