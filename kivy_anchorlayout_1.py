import japanize_kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout

Builder.load_file('kivy_anchorlayout_1.kv')
Window.size = (200, 200)


class KivyAnchorLayout(AnchorLayout):
    def on_button_pressed(self, instance):
        print('%s がクリックされました。' % instance.text)


class ExampleApp(App):
    def build(self):
        self.title = 'AnchorLayout'
        return KivyAnchorLayout()


if __name__ == '__main__':
    ExampleApp().run()
