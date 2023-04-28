import unittest


class TestClass(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual('aws'.upper(), "AWS")

    def test_case_2(self):
        self.assertEqual('aws'.upper(), "AWs")

    def test_case_3(self):
        self.assertEqual('1,2,3'.split(','), [1,'2','3'])

    def test_case_4(self):
        self.assertEqual({1,4},{4,1})
