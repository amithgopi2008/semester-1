from shapes import Circle
from point import Point

# Create a Circle and print it
c = Circle(2.5, Point(0.0, 0.0))
print(c)                              # red circle, radius 2.5, at (0.0, 0.0)

# Area and perimeter, each to 3 decimal places
print(f"Area = {c.area():.3f}")       # Area = 19.635
print(f"Perimeter = {c.perimeter():.3f}")  # Perimeter = 15.708

# Move the circle (inherited method from Shape)
print("Moving the circle...")
c.move_to(Point(1.6, 3.2))            # or whatever Shape's move method is called
print(c)                              # red circle, radius 2.5, at (1.6, 3.2)

# Change the colour (inherited method from Shape)
print("Changing the circle's colour...")
c.set_colour("green")                 # or whatever Shape's colour setter is called
print(c)                              # green circle, radius 2.5, at (1.6, 3.2)