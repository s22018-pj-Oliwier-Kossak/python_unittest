import unittest
from rectangle import rectangle_area, rectangle_perimeter


class TestArea(unittest.TestCase):

    def test_rectnagle_area_01(self):
        self.assertEqual(rectangle_area(4, 5), 20)

    def test_rectnagle_area_02(self):
        self.assertEqual(rectangle_area(4, 5), 21)

    def test_rectnagle_area_03(self):
        raise AssertionError('Error message')

class TestPerimeter(unittest.TestCase):

    def test_rectnagle_perimeter_01(self):
        self.assertEqual(rectangle_perimeter(4, 5), 18)

    def test_rectnagle_perimeter_02(self):
        self.assertEqual(rectangle_perimeter(4, 5), 21)

    def test_rectnagle_perimeter_03(self):
        raise AssertionError('Error message')



