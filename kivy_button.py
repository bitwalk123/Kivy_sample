from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


# Reference:
# https://kivy.org/doc/stable/api-kivy.uix.button.html
class KivyButton(BoxLayout):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        btn = Button(text='Hello, World!')
        btn.bind(on_press=self.on_button_pressed)
        self.add_widget(btn)

    def on_button_pressed(self, instance):
        print('The button <%s> is being pressed' % instance.text)


class ExampleApp(App):
    def build(self):
        self.title = 'HelloWorld'
        return KivyButton()


if __name__ == '__main__':
    ExampleApp().run()
