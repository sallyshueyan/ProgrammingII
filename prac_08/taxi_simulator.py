from prac_08.car import Car
from prac_08.taxi import Taxi
from prac_08.sliver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi will calculate the fare based on the user's input distance and type of taxi car."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_fare = 0
    print("Let's drive!")
    print(MENU)
    user_choice = input(">>> ").lower()
    while user_choice != "q":
        if user_choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
            except ValueError:
                print("Invalid taxi choice")
        elif user_choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                drive_distance = float(input("Drive how far? "))
                current_taxi.drive(drive_distance)
                trip_fare = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_fare}")
                total_fare = total_fare + trip_fare
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(total_fare))
        print(MENU)
        user_choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_fare}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display all available taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def run_tests():
    """Function Tests the usability of Car and Taxi classes."""
    car = Car("Mazda", 200)
    car.drive(50)
    print(f"fuel = {car.fuel}")
    print(f"odo  = {car.odometer}")
    car.drive(100)
    print(f"fuel = {car.fuel}")
    print(f"odo  = {car.odometer}")
    print(car)

    distance = float(input("Drive how far? "))
    while distance > 0:
        distance_travelled = car.drive(distance)
        print(f"{car} travelled {distance_travelled}")
        distance = int(input("Drive how far? "))

    taxi = Taxi("Prius 1", 100)
    print(taxi)
    taxi.drive(35)
    print(f"Taxi fare: {taxi.get_fare()}")
    print(f"odo  = {taxi.odometer}")
    print(f"fuel = {taxi.fuel}")

    silver_taxi = SilverServiceTaxi("Hummer", 100, 4)
    silver_taxi.drive(20)
    print(silver_taxi)
    print(f"Total fare: ${silver_taxi.get_fare()}")


main()
