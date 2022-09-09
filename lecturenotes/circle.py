from math import pi
from shape import Shape


class Circle(Shape):
    def __init__(self, x=0, y=0, radius=1):
        super().__init__(x,y)
        self.radius = radius

    def area(self):
        return self.radius ** 2 * pi

    def __str__(self): # method overriding (overriding parent's __str__())
        return super().__str__() + f"Shape = Circle, radius = {self.radius}"