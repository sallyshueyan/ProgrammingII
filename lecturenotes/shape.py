class Shape:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, x_amount, y_amount):
        self.x += x_amount
        self.y += y_amount

    def __str__(self):
        return f"Shape at ({self.x}, {self.y})"
