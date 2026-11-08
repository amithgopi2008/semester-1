import math
from shapes import Shape          
from point import Point           


class Circle(Shape):
    """
    A circle with a radius, position and colour.
    """

    def __init__(self, radius, position, colour="red"):
        """
        Creates a Circle with the given radius, position and colour.

        Raises:
            TypeError: if radius is not int or float.
            ValueError: if radius is not greater than zero.
        """
        super().__init__(colour, position)   
        self.set_radius(radius)              

    def set_radius(self, radius):
        """
        Sets the radius of this Circle.

        Raises:
            TypeError: if radius is not int or float.
            ValueError: if radius is not greater than zero.
        """
        if not isinstance(radius, (int, float)) or isinstance(radius, bool):
            raise TypeError(f"radius must be int or float, got {type(radius).__name__}")
        if radius <= 0:
            raise ValueError(f"radius must be greater than zero, got {radius}")
        self.radius = radius

    def __str__(self):
        """
        Returns a string like 'red circle, radius 2.5, at (0.0, 0.0)'.
        """
        return f"{self.colour} circle, radius {self.radius}, at {self.position}"

    def area(self):
        """
        Returns the area of this Circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Returns the perimeter (circumference) of this Circle.
        """
        return 2 * math.pi * self.radius