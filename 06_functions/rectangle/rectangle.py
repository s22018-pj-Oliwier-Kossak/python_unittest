def rectangle_area(height, width):
    """the fucntion which return area of rectnagle"""

    if not (isinstance(width, (float, int)) and isinstance(height, (float, int))):
        raise TypeError("width and height must be a number")

    if width < 0 or height < 0:
        raise ValueError("width and height must be greater than 0")

    return height * width
