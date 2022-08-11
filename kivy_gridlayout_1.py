import japanize_kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout

Builder.load_file('kivy_gridlayout_1.kv')
Window.size = (200, 200)


class KivyGridLayout(GridLayout):
    def on_button_pressed(self, instance):
        print('ボタン %s がクリックされました。' % instance.text)


class ExampleApp(App):
    def build(self):
        self.title = 'GridLayout'
        return KivyGridLayout()


if __name__ == '__main__':
    ExampleApp().run()
