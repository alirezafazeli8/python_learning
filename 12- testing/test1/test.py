import unittest
import main


# class TestMain(unittest.TestCase):
#     def test_do_stuff(self):
#         test_param = 8
#         result = main.do_stuff(test_param)
#         self.assertEqual(result, 64)

# def test_do_stuff2(self):
# test_param = "a"
# result = main.do_stuff(test_param)
# self.assertEqual(result, test_param)
# self.assertRaises(AssertionError, main.do_stuff, "dasd")


# unittest.main()


# class TestStuff(unittest.TestCase):
#     def test_number(self):
#         result = main.do_stuff(2)
#         self.assertEqual(result, 4)

#     def test_negative(self):
#         result = main.do_stuff(-2)
#         self.assertTrue(result)
#         # self.assertEqual(result, -(2**2))

#     def test_zero(self):
#         result = main.do_stuff(0)
#         self.assertTrue(result)
#         # self.assertEqual(result, 0**2)


# class TestStuff2(unittest.TestCase):
#     def test_type(self):
#         result = "a"
#         self.assertRaises(TypeError, main.do_stuff_2, result)

#     def test_instance(self):
#         self.assertIsInstance("a", str)


# unittest.main()


class TestMain(unittest.TestCase):

    def setUp(self):
        print("SetUp Method is running ...")

    def test_do_stuff(self):
        test_param = None
        result = main.do_stuff(test_param)

        self.assertEqual(result, "Pleas Enter Number")

    def test_empty_str(self):
        test_param = ""
        result = main.do_stuff(test_param)

        self.assertEqual(result, "Pleas Enter Number")

    def test_zero(self):
        """
        Test is Good
        """
        test_param = 0
        result = main.do_stuff(test_param)

        self.assertEqual(result, "Pleas Enter Number")

    def tearDown(self):
        print("Close()")


if __name__ == "__main__":
    unittest.main()

unittest.main()
