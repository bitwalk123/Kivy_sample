import sys

import kivy
import japanize_kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout

Builder.load_file('kivy_relativelayout_1.kv')
Window.size = (200, 200)


class KivyRelativeLayout(RelativeLayout):
    pass


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
