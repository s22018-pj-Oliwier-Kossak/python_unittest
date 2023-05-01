import unittest
import sys
from parameterized import parameterized
sys.path.append(r"C:\Users\PC\PycharmProjects\python_unittest\09_parametrized_tests\01_project")
from calculator.calc_math import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self) :
        self.calc = SimpleCalculator()

    @parameterized.expand([
        ("positive",1,2,3),
        ("negative",-5,1,-4),
        ("error",-3,-5,-2),

    ])
    def test_add(self,name,x,y,result):
        self.assertEqual(self.calc.add(x,y),result)