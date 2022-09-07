from shape import Shape


class Rectangle(Shape):
    def __init__(self, x=0, y=0, width=1, height=1):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
