import unittest
import sys

sys.path.append("C:\\Users\\PC\\PycharmProjects\\python_unittest\\07_classes\\01_project")
from calculator.calc_math import SimpleCalculator




class TestSimpleCalculatorAdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("set up")
        cls.calc = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add(3, 4), 7)

    def test_add_incorrect_type(self):
        self.assertEqual(self.calc.add(3, '4'), -1)

    @classmethod
    def tearDownClass(cls) :
        print("tearing down ")
        del cls.calc


class TestSimpleCalculatorSub(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("set up sub")
        cls.calc = SimpleCalculator()

    def test_sub(self):
        self.assertEqual(self.calc.sub(3, 4), -1)

    def test_sub_incorrect_type(self):
        self.assertEqual(self.calc.sub(3, '3'), -1)


