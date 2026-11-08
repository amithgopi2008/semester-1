import math


class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x: float, y: float) -> None:
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x
        self.y = y

    def distance(self) -> float:
        """
        Returns distance of this Point from the origin.
        """
        return math.hypot(self.x, self.y)

    def distance_to(self, p: "Point") -> float:
        """
        Returns distance of this Point from the specified Point.
        """
        return math.hypot(self.x - p.x, self.y - p.y)



p = Point("two", "one")
print(p.distance())