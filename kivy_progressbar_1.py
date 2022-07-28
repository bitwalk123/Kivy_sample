import threading
import time

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('kivy_progressbar_1.kv')
Window.size = (200, 200)


def counter(progress):
    for c in range(100):
        time.sleep(0.1)
        progress.value = c


class KivyProgressBar(BoxLayout):
    pbar = ObjectProperty(None)

    def demo(self, instance):
        threading.Thread(target=counter, args=(self.pbar,), daemon=True).start()


class ExampleApp(App):
    def build(self):
        self.title = 'ProgressBar'
        return KivyProgressBar()


if __name__ == '__main__':
    ExampleApp().run()
