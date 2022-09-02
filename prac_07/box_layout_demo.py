from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Main program - Kivy app to greet user."""
    def build(self):
        """Construct main app."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Function greet user with their input name."""
        print("test")
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def handle_clear(self):
        """Function helps to clear the system."""
        self.root.ids.input_name.text = " "
        self.root.ids.output_label.text = " "


BoxLayoutDemo().run()
