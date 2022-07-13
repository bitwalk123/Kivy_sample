import japanize_kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('kivy_togglebutton_1.kv')
Window.size = (200, 200)


class KivyToggleButton(BoxLayout):
    def on_togglebutton_pressed(self, instance):
        print('%s がクリックされて %s になりました。' % (instance.text, instance.state))


class ExampleApp(App):
    def build(self):
        self.title = 'ToggleButtons'
        return KivyToggleButton()


if __name__ == '__main__':
    ExampleApp().run()
