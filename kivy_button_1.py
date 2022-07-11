import japanize_kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('kivy_button_1.kv')
Window.size = (200, 200)


class KivyButton(BoxLayout):
    def on_button_pressed(self, instance):
        print('%s がクリックされました。' % instance.text)


class TestApp(App):
    def build(self):
        self.title = 'Buttons'
        return KivyButton()


if __name__ == '__main__':
    TestApp().run()
