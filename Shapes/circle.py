from math import pi
from Shapes.shape import Shape

class Circle(Shape):
    def __init__(self, x=0, y=0, radius=1):
         self.x = x
         self.y = y
         self.radius = radius
    def area(self):
        return self.radius ** 2 * pi
