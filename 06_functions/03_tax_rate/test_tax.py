import unittest
from tax import cal_rate

class TestTax(unittest.TestCase):

    def test_tax_cal_with_ten_percent(self):
        self.assertEqual(10,cal_rate(100,10))

    def test_tax_cal_with_fourteen_percent(self):
        self.assertAlmostEqual(14, cal_rate(100, 14))

    def test_tax_cal_with_ten_percent_wiht_almost_equal(self):
        self.assertAlmostEqual(14, cal_rate(100, 14))