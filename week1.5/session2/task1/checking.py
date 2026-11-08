import math


class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x, y):
        """
        Creates a Point, given x & y coordinates.
        """
        if not isinstance(x, (int, float)):
            raise TypeError(f"x must be int or float, got {type(x).__name__}")
        if not isinstance(y, (int, float)):
            raise TypeError(f"y must be int or float, got {type(y).__name__}")

        self.x = x
        self.y = y

    def distance(self):
        """
        Returns distance of this Point from the origin.
        """
        return math.hypot(self.x, self.y)

    def distance_to(self, p):
        """
        Returns distance of this Point from the specified Point.
        """
        return math.hypot(self.x - p.x, self.y - p.y)



p = Point("two", "one")
print(p.distance())