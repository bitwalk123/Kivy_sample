import japanize_kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('kivy_boxlayout_1.kv')
Window.size = (200, 200)


class KivyBoxLayout(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'

    def on_button_pressed(self, instance):
        print('ボタン %s がクリックされました。' % instance.text)


class ExampleApp(App):
    def build(self):
        self.title = 'BoxLayout'
        return KivyBoxLayout()


if __name__ == '__main__':
    ExampleApp().run()
