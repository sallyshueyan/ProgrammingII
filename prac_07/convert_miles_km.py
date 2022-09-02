from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class CovertMilesKm(App):
    """Main program - Kivy app to convert miles to kilometers."""

    def build(self):
        """Construct main app."""
        self.title = "Covert Miles to Kilometers"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_calculate(self):
        """Calculate miles to kilometers."""
        value = self.handle_input_validity()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_input_validity(self):
        """Check validity of input."""
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0

    def handle_increment(self, change):
        """Function pass a value."""
        value = self.handle_input_validity() + change
        self.root.ids.input_number.text = str(value)
        self.handle_calculate()


if __name__ == '__main__':
    """Activate the program"""
    convert_miles_km_window = CovertMilesKm()
    convert_miles_km_window.run()
