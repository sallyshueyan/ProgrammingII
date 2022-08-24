from point import Point


def main():
    points = []
    for i in range(3):
        print(f"Point {i+1}")
        print("*" * 15)
        x_coordinate = float(input("X? "))
        y_coordinate = float(input("Y? "))
        new_point = Point(x_coordinate, y_coordinate)
        points.append(new_point)

    print(points)



if __name__ == '__main__':
    main()
