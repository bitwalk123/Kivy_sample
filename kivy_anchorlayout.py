import sys

import kivy
import japanize_kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button

Window.size = (200, 200)


class KivyAnchorLayout(AnchorLayout):
    def __init__(self):
        super().__init__()
        self.anchor_x = 'right'
        self.anchor_y = 'bottom'
        self.init_ui()

    def init_ui(self):
        btn_a = Button(text='ボタンＡ', size_hint=(.67, .67))
        btn_a.bind(on_press=self.on_button_pressed)
        self.add_widget(btn_a)
        btn_b = Button(text='ボタンＢ', size_hint=(.33, .33))
        btn_b.bind(on_press=self.on_button_pressed)
        self.add_widget(btn_b)

    def on_button_pressed(self, instance):
        print('%s がクリックされました。' % instance.text)


class ExampleApp(App):
    def build(self):
        self.title = 'AnchorLayout'
        return KivyAnchorLayout()


if __name__ == '__main__':
    # version information
    print(sys.version)
    print(kivy.__version__)
    #
    ExampleApp().run()
