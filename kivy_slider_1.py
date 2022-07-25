import japanize_kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('kivy_slider_1.kv')
Window.size = (200, 200)


class KivySlider(BoxLayout):
    def on_slider_move(self, instance, value):
        print('スライダーの値は %.2f です。' % instance.value)


class ExampleApp(App):
    def build(self):
        self.title = 'Slider'
        return KivySlider()


if __name__ == '__main__':
    ExampleApp().run()
