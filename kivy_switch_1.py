import japanize_kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('kivy_switch_1.kv')
Window.size = (200, 200)


class KivySwitch(BoxLayout):
    def on_swiped(self, instance, value):
        status = 'オフ'
        if value:
            status = 'オン'

        print('スイッチが%sになりました。' % status)


class ExampleApp(App):
    def build(self):
        self.title = 'Switch'
        return KivySwitch()


if __name__ == '__main__':
    ExampleApp().run()
