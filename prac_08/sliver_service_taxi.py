from prac_08.taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = fanciness * self.price_per_km

    def calculate_fare(self):
        return super().get_fare() + self.flagfall

    def __str__(self):
        return f"{super().__str__()} plus flagfall of {self.flagfall}"