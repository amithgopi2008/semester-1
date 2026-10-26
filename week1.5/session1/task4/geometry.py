# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""
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
    
class Circle:

# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle

    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius**2)

    def perimeter(self):
        return math.pi * 2 * self.radius



# Don't add any testing code to this file!
