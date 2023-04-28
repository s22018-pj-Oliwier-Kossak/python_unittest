import unittest


class TestClass(unittest.TestCase):

    def test_case_01(self):
        self.assertTrue(isinstance('asw', str))

    def test_case_02(self):
        self.assertTrue(isinstance('asw', int))

    def test_case_03(self):
        self.assertFalse(isinstance('asw', int))

    def test_case_04(self):
        self.assertFalse(isinstance('asw', str))
