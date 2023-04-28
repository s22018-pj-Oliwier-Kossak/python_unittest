import unittest


def rectangle_area(height, width):
    """the fucntion which return area of rectnagle"""
    if not (isinstance(width, (float, int)) and isinstance(height, (float, int))):
        raise TypeError("width and height must be a number")
    if width < 0 or height < 0:
        raise ValueError("width and height must be greater than 0")
    return height * width


class TestArea(unittest.TestCase):

    def test_rectnagle_area(self):
        self.assertEqual(rectangle_area(4, 5), 20)

    def test_rectnagle_area_incorrect_type_should_raise_error(self):
        self.assertRaises(TypeError,rectangle_area,'4',10)
        self.assertRaises(TypeError, rectangle_area, 1.2, '10')

    def test_rectnagle_area_negative_value_should_raise_error(self):
        self.assertRaises(ValueError,rectangle_area,-5,10)
        self.assertRaises(ValueError, rectangle_area, 1.2, -10)


if __name__ == '__main__':
    unittest.main(verbosity=2)
