from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty


class ButtonEventDemo(App):
    message = StringProperty()

    def build(self):
        self.title = "Button Event Demo"
        self.root = Builder.load_file("button_event.kv")
        return self.root

    def press_button(self):
        self.message = self.root.ids.user_input.text


if __name__ == '__main__':
    button_event_demo_window = ButtonEventDemo()
    button_event_demo_window.run()
