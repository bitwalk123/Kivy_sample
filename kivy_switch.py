import japanize_kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.switch import Switch

Window.size = (200, 200)


class KivySwitch(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'
        self.init_ui()

    def init_ui(self):
        sw = Switch(active=True)
        sw.bind(active=self.on_swiped)
        self.add_widget(sw)

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
