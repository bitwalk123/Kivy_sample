import sys

import kivy
import japanize_kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

Builder.load_file('kivy_relativelayout_1.kv')
Window.size = (200, 200)


class KivyRelativeLayout(FloatLayout):
    def on_button_pressed(self, instance):
        print('%s がクリックされました。' % instance.text)


class ExampleApp(App):
    def build(self):
        self.title = 'RelativeLayout'
        return KivyRelativeLayout()


if __name__ == '__main__':
    # version information
    print(sys.version)
    print(kivy.__version__)
    #
    ExampleApp().run()