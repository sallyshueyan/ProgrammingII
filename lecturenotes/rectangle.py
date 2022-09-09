from shape import Shape


class Rectangle(Shape):
    def __init__(self, x=0, y=0, width=1, height=1):
        super().__init__(x, y) # parent constructor
        self.width = width # new attribute
        self.height = height # new attribute

    def area(self):
        return self.width * self.height

    def __str__(self): # method overriding (overriding parent's __str__())
        return super().__str__() + f"Shape = Rectangle, width = {self.width}, height = {self.height}"