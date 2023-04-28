import unittest


def setUpModule():
    print("set up module")


def tearDownModule():
    print("tearing down module")


class TestClass1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(f"setting up class {cls.__name__}")

    @classmethod
    def tearDownClass(cls):
        print("tear down class")

    def test_case_1(self):
        self.assertEqual('John Smith'.split(), ['John', 'Smith'])


class TestClass2(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual('John Smith'.split(), ['John', 'Smith'])


class TestClass3(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual('John Smith'.split(), ['John', 'Smith'])
