import kivy

kivy.require('1.11.1')  # 版数を指定することもできます

from kivy.app import App
from kivy.uix.button import Button


class HelloApp(App):
    def build(self):
        button = Button(text="Hello World!")
        button.bind(on_press=self.say_hello)
        return button

    def say_hello(self, button):
        print("Hello World!")


if __name__ == '__main__':
    HelloApp().run()
