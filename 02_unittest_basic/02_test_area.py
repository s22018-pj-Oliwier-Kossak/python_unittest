import unittest


def rectangle_area(height, width):
    """the fucntion which return area of rectnagle"""
    if not (isinstance(width, (float, int)) and isinstance(height, (float, int))):
        raise TypeError("width and height must be a number")
    if width < 0 or height < 0:
        raise ValueError("width and height must be greater than 0")
    return height * width


class TestArea(unittest.TestCase):

    def test_rectnagle_area_01(self):
        self.assertEqual(rectangle_area(4, 5), 20)

    def test_rectnagle_area_02(self):
        self.assertEqual(rectangle_area(4, 5), 21)

    def test_rectnagle_area_03(self):
        raise AssertionError('Error message')

    def test_rectnagle_area_04(self):
        raise TypeError('Error message')


if __name__ == '__main__':
    unittest.main(verbosity=2)
