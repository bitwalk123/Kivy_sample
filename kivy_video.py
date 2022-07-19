import os
os.environ["KIVY_VIDEO"] = "ffpyplayer"

import japanize_kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.video import Video

#Window.size = (270, 480)


class KivyVideo(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'
        self.init_ui()

    def init_ui(self):
        vdo = Video(source='sample.mp4', play=True)
        self.add_widget(vdo)


class ExampleApp(App):
    def build(self):
        self.title = 'Video'
        return KivyVideo()


if __name__ == '__main__':
    ExampleApp().run()
