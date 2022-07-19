import os
os.environ["KIVY_VIDEO"] = "ffpyplayer"

import japanize_kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('kivy_videoplayer_1.kv')
#Window.size = (270, 480)


class KivyVideoPlayer(BoxLayout):
    pass

class ExampleApp(App):
    def build(self):
        self.title = 'Video'
        return KivyVideoPlayer()


if __name__ == '__main__':
    ExampleApp().run()
