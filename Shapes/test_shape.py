from rectangle import Rectangle
from circle import Circle

rectangle = Rectangle(0, 0, 3, 2)
rectangle.move(5, 15)
print(rectangle)  # displays "Shape at (5, 15)"
print(rectangle.area())  # displays 6 from 3*2

circle = Circle(1, 1, 5)  # at point (1,1) radius of 5 units
circle.move(3, 3)
print(circle)
print(circle.area())