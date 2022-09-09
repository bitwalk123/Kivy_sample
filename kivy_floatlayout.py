import sys

import kivy
import japanize_kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

Window.size = (200, 200)


class KivyFloatLayout(FloatLayout):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        btn_a = Button(
            text='ボタンＡ',
            size_hint=(.4, .3),
            pos_hint={'x':.1, 'y':.6}
        )
        btn_a.bind(on_press=self.on_button_pressed)
        self.add_widget(btn_a)
        btn_b = Button(
            text='ボタンＢ',
            size_hint=(.4, .3),
            pos_hint={'x':.5, 'y':.1}
        )
        btn_b.bind(on_press=self.on_button_pressed)
        self.add_widget(btn_b)

    def on_button_pressed(self, instance):
        print('%s がクリックされました。' % instance.text)


class ExampleApp(App):
    def build(self):
        self.title = 'FloatLayout'
        return KivyFloatLayout()


if __name__ == '__main__':
    # version information
    print(sys.version)
    print(kivy.__version__)
    #
    ExampleApp().run()
