class Rectangle:
    """A class representing a rectangle."""

    def __init__(self, width, height):
        """Initialize a rectangle with a width and height."""
        if type(width) is not int or type(height) is not int:
            raise TypeError("Width and height must be integers.")

        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive.")

        self.width = width
        self.height = height

    def is_square(self):
        """Check whether the rectangle is a square."""
        return self.width == self.height

    def area(self):
        """Calculate and return the rectangle's area."""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the rectangle's perimeter."""
        return 2 * (self.width + self.height)