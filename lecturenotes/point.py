import math


class Point:

    def __init__(self, x=0.0, y=0.0):
        """Initialise a point with x and y coordinates."""
        self.x = x
        self.y = y

    def distance(self, other):
        """Get the distance between self and another Point."""
        x_diff = self.x - other.x  # (x1 — x2)
        y_diff = self.y - other.y  # (y1 — y2)
        return math.sqrt(x_diff ** 2 + y_diff ** 2)

    def __str__(self):
        """Print a Point as a coordinate pair."""
        return f"({self.x:.2f}, {self.y:.2f})"

    def __repr__(self):
        """Print a Point as a coordinate pair."""
        return f"({self.x:.2f}, {self.y:.2f})"


if __name__ == "__main__": # test if the current file is running
    point1 = Point(5, 9)
    point2 = Point(23, 50)
    # for example, we should be able to call the print function on it
    print(point1.distance(point2))
