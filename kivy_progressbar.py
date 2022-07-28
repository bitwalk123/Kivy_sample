import threading
import time

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar

Window.size = (200, 200)


def counter(progress):
    for c in range(100):
        time.sleep(0.1)
        progress.value = c


class KivyProgressBar(BoxLayout):
    pbar: ProgressBar = None

    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'
        self.init_ui()

    def init_ui(self):
        self.pbar = ProgressBar(max=100)
        self.add_widget(self.pbar)
        btn = Button(text='START')
        btn.bind(on_press=self.demo)
        self.add_widget(btn)

    def demo(self, instance):
        threading.Thread(target=counter, args=(self.pbar,), daemon=True).start()


class ExampleApp(App):
    def build(self):
        self.title = 'ProgressBar'
        return KivyProgressBar()


if __name__ == '__main__':
    ExampleApp().run()
