import japanize_kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('kivy_label_1.kv')
Window.size = (200, 200)


class KivyLabel(BoxLayout):
    pass


class ExampleApp(App):
    def build(self):
        self.title = 'Label'
        return KivyLabel()


if __name__ == '__main__':
    ExampleApp().run()
