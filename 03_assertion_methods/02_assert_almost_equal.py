import unittest

class TestClass(unittest.TestCase):

    def test_case_1(self):
        self.assertAlmostEqual(0.2+0.3,0.5)

    def test_case_1(self):
        self.assertAlmostEqual(0.1234567,0.1234567)

    def test_case_1(self):
        self.assertAlmostEqual(0.12345678,0.12345679)