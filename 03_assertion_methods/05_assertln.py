import unittest


class TestClass(unittest.TestCase):

    def test_case_1(self):
        self.assertIn("@", "1234@mail.com")

    def test_case_2(self):
        numbers = [1, 2, 3, 4]
        self.assertIn(1, numbers)

    def test_case_3(self):
        numbers = [1, 2, 3, 4]
        self.assertIn(11, numbers)

    def test_case_4(self):
        dict = {"kawa": "1", "lody": 2}
        self.assertIn("kawa", dict)

    def test_case_5(self):
        dict = {"kawa": "1", "lody": 2}
        self.assertNotIn("kawa", dict)
