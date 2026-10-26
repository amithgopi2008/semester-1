# Week 1.5, Session 1: Task 3
import math
class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    

    # Add distance() method here

    def distance(self):
        return math.hypot(self.x_coordinate, self.y_coordinate)
    # Add distance_to() method here

    def distance_to(self, point):
        distance1 = math.hypot(self.x_coordinate, self.y_coordinate)
        distance2 = math.hypot(point.x_coordinate, point.y_coordinate)

        return (distance2-distance1)
    

    # (This will need a parameter representing another point)



# Finally, add code here to demonstrate use of Point
p = Point(3.5,2.5)
p2 = Point(4.5,3.8)
print(p.distance())

print(p.distance_to(p2))