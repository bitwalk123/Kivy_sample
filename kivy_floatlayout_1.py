import sys

import kivy
import japanize_kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

Builder.load_file('kivy_floatlayout_1.kv')
Window.size = (200, 200)


class KivyFloatLayout(FloatLayout):
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
