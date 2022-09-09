from prac_08.sliver_service_taxi import SilverServiceTaxi


def main():
    """Create a new taxi with name, units of fuel and fare."""
    taxi = SilverServiceTaxi("Hummer", 100, 4)
    taxi.drive(20)
    print(taxi)
    print(f"Total fare: ${taxi.get_fare()}")


main()