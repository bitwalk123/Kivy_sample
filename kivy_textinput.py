import japanize_kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

Window.size = (200, 200)


class KivyTextInput(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'
        self.init_ui()

    def init_ui(self):
        txt1 = TextInput()
        self.add_widget(txt1)
        txt2 = TextInput(multiline=False)
        self.add_widget(txt2)


class ExampleApp(App):
    def build(self):
        self.title = 'TextInputs'
        return KivyTextInput()


if __name__ == '__main__':
    ExampleApp().run()
