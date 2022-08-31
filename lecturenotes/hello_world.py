from kivy.app import App
from kivy.app import Widget


class HelloWorld(App):
    def build(self):
        self.title = "My First Kivy World - Hello World"
        self.root = Widget()
        return self.root


if __name__ == '__main__':
    # same as HelloWord().run()
    hello_window = HelloWorld()
    hello_window.run()
