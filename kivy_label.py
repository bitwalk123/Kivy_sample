import japanize_kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

Window.size = (200, 200)


class KivyLabel(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'
        self.init_ui()

    def init_ui(self):
        lbl = Label(text='文字列を表示するラベル')
        self.add_widget(lbl)


class ExampleApp(App):
    def build(self):
        self.title = 'Label'
        return KivyLabel()


if __name__ == '__main__':
    ExampleApp().run()
