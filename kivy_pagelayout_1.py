import japanize_kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.pagelayout import PageLayout

Builder.load_file('kivy_pagelayout_1.kv')
Window.size = (200, 200)


class KivyPageLayout(PageLayout):
    pass

class ExampleApp(App):
    def build(self):
        self.title = 'PageLayout'
        return KivyPageLayout()


if __name__ == '__main__':
    ExampleApp().run()
