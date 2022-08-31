from kivy.app import App
from kivy.lang import Builder


class HelloKv(App):
    def build(self):
        self.title = "Hello World Kv!"
        self.root = Builder.load_file("widget.kv")
        return self.root


if __name__ == '__main__':
    # same as HelloWord().run()
    hello_window = HelloKv()
    hello_window.run()
