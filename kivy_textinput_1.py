import japanize_kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

Builder.load_file('kivy_textinput_1.kv')
Window.size = (200, 200)


class KivyTextInput(BoxLayout):
    pass

class ExampleApp(App):
    def build(self):
        self.title = 'TextInputs'
        return KivyTextInput()


if __name__ == '__main__':
    ExampleApp().run()
