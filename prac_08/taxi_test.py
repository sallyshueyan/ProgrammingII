from prac_08.taxi import Taxi


def main():
    # Create a new taxi with name "Prius 1", 100 units of fuel and price of $1.23/km
    taxi = Taxi("Prius 1", 100)
    # Drive the taxi 40 km
    actual_distance_driven = taxi.drive(40)
    print(f"Taxi drove for {actual_distance_driven}km")
    # Print the taxi's details and the current fare
    print(taxi)
    print(f"Current fare: ${taxi.get_fare():.2f}")
    # Restart the meter (start a new fare) and then drive the car 100 km
    taxi.start_fare()
    actual_distance_driven = taxi.drive(100)
    print(f"Tried driving 100km, but taxi drove for {actual_distance_driven}km")
    # Print the details and the current fare
    print(taxi)
    print(f"Current fare: ${taxi.get_fare():.2f}")


main()
