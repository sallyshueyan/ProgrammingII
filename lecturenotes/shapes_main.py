from rectangle import Rectangle
from circle import Circle


def main():
    rectangle = Rectangle(0,0,3,2)
    rectangle.move(5, 15)  # move() comes from the Shape - inherited
    print(rectangle)  # __str__() comes from the Shape - inherited
    print(rectangle.area)  # area() is from Reactangle

    print()

    circle = Circle(1, 1, 5)  # at point (1,1) radius of 5 units
    circle.move(3, 3)
    print(circle)
    print(circle.area())

    rectangle_two = Rectangle(1, 20, 30, 12)
    rectangle_three = Rectangle(4, 10, 5, 9)
    circle_two = Circle(11, 8, 23)

    shapes = [circle, rectangle_two, rectangle, circle, rectangle_three]
    for shape in shapes:
        print(shape)
main()
