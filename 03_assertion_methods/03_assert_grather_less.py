import unittest

class TestClass(unittest.TestCase):

    def test_case_1(self):
        self.assertGreater(3,2)

    def test_case_2(self):
        self.assertGreaterEqual(3,2)

    def test_case_3(self):
        self.assertGreaterEqual(2,2)

    def test_case_4(self):
        self.assertLess(2,5)

    def test_case_5(self):
        self.assertLess(2,2)