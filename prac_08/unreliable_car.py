from prac_08.car import Car


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        self.name = name
        self.fuel = fuel
        self.reliability = reliability
