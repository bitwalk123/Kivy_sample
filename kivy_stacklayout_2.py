import japanize_kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.stacklayout import StackLayout

Builder.load_file('kivy_stacklayout_2.kv')
Window.size = (200, 200)


class KivyStackLayout(StackLayout):
    def on_button_pressed(self, instance):
        print('ボタン %s がクリックされました。' % instance.text)


class ExampleApp(App):
    def build(self):
        self.title = 'StackLayout'
        return KivyStackLayout()


if __name__ == '__main__':
    ExampleApp().run()
