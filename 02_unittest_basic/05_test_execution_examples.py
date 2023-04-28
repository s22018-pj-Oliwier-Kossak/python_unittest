import unittest


class TestClass1(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual("John Smith".split(), ['John', 'Smith'])

    def test_case_2(self):
        self.assertTrue('apple'.islower())


class TestClass2(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual("1.2".split('.'), ['1', '2'])


class TestClass3(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual("#".join(["1", "2"]), '1#2')
