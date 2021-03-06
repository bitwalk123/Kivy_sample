import japanize_kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

Window.size = (200, 200)


class KivyImage(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'
        self.init_ui()

    def init_ui(self):
        img = Image(source='sample.jpg')
        self.add_widget(img)


class ExampleApp(App):
    def build(self):
        self.title = 'Image'
        return KivyImage()


if __name__ == '__main__':
    ExampleApp().run()
