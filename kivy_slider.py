import japanize_kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider

Window.size = (200, 200)


class KivySlider(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'
        self.init_ui()

    def init_ui(self):
        sld = Slider(min=0, max=100, step=1, value=0)
        #sld.bind(on_touch_move=self.on_slider_move)
        #sld.fbind('value', self.on_slider_move)
        sld.bind(value=self.on_slider_move)
        self.add_widget(sld)

    def on_slider_move(self, instance, value):
        print('スライダーの値は %.2f です。' % instance.value)


class ExampleApp(App):
    def build(self):
        self.title = 'Slider'
        return KivySlider()


if __name__ == '__main__':
    ExampleApp().run()
