import unittest
from tax import calc_tax

class TestTax(unittest.TestCase):

    def test_tax_cal_with_ten_percent(self):
        self.assertEqual(10,calc_tax(100,0.10))

    def test_tax_cal_with_ten_fourtheen_almost(self):
        self.assertAlmostEqual(14,calc_tax(100, 0.14))

    def test_tax_cal_with_incorrect_amount_type_should_raise_error(self):
        self.assertRaises(TypeError,calc_tax,'ten',0.23)

    def test_tax_cal_with_incorrect_tax_rate_type_should_raise_error(self):
        self.assertRaises(TypeError,calc_tax,10,'0.23')

    def test_tax_cal_with_incorrect_tax_rate_type_should__error(self):
        self.assertRaises(ValueError, calc_tax, 10, 0.0)
        self.assertRaises(ValueError, calc_tax, 10, 1)

    def test_tax_cal_with_incorrect_negative_amount__error(self):
        self.assertRaises(ValueError, calc_tax, -5, 0.2)

