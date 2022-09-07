from prac_08.unreliable_car import UnreliableCar


def main():
    reliable_car = UnreliableCar("Car 1", 100, 99)
    unreliable_car = UnreliableCar("Car 2", 100, 1)

    for i in range(1, 15):
        print(f"Drive for {i}km:")
        print(f"{reliable_car.name:5} drove {reliable_car.drive(i):2}km")
        print(f"{unreliable_car.name:5} drove {unreliable_car.drive(i):2}km")

    print(reliable_car)
    print(unreliable_car)


main()
