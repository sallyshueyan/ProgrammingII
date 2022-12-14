from prac_08.car import Car
from random import randint


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        """Construct main function."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Generate random number and return distance drive."""
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0

        distance_drive = super().drive(distance)
        return distance_drive
