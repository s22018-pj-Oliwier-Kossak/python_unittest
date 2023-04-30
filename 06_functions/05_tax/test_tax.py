import unittest
from tax import calc_tax


class TestTax(unittest.TestCase):
    def test_calc_tax_fourthy_years(self):
        self.assertAlmostEqual(calc_tax(1000, 0.2, 40),200)

    def test_calc_tax_eighteen_years(self):
        self.assertAlmostEqual(calc_tax(10000, 0.2, 18), 5000)

    def test_calc_tax_sixty_five_years(self):
        self.assertAlmostEqual(calc_tax(10000, 0.2, 65), 2000)

    def test_calc_tax_sixty_six_years(self):
        self.assertAlmostEqual(calc_tax(10000, 0.2, 66), 8000)

    def test_calc_tax_incorrect_age_type_error(self):
        self.assertRaises(TypeError, calc_tax, 10, 0.2, "10")

    def test_calc_tax_negative_age_value_error(self):
        self.assertRaises(ValueError, calc_tax, 10, 0.2, -10)
