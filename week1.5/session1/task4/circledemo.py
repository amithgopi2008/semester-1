# Week 1.5, Session 1: Task 4

# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py
from geometry import Point, Circle
# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
#  - Creates a Circle object, using the Point object and a value for radius
#  - Displays the area of the circle
#  - Displays the perimeter of the circle

x = float(input("Enter x_coordinate for the centre: "))
y = float(input("Enter y_coordinate for the centre: "))

centre = Point(x,y)

radius = float(input("Enter the radius for the cirlce: "))

circle1 = Circle(centre, radius)
print(circle1.area())
print(circle1.perimeter())