import japanize_kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.pagelayout import PageLayout

Window.size = (200, 200)


class KivyPageLayout(PageLayout):
    def __init__(self):
        super().__init__()
        self.border = 10
        self.init_ui()

    def init_ui(self):
        img_1 = Image(source='image_1.jpg')
        self.add_widget(img_1)
        img_2 = Image(source='image_2.jpg')
        self.add_widget(img_2)
        img_3 = Image(source='image_3.jpg')
        self.add_widget(img_3)


class ExampleApp(App):
    def build(self):
        self.title = 'PageLayout'
        return KivyPageLayout()


if __name__ == '__main__':
    ExampleApp().run()
