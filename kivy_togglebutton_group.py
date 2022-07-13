import japanize_kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton

Window.size = (200, 200)


class KivyToggleButton(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'
        self.init_ui()

    def init_ui(self):
        tgb_a = ToggleButton(text='トグルボタンＡ', group='tgb')
        tgb_a.bind(on_press=self.on_togglebutton_pressed)
        self.add_widget(tgb_a)
        tgb_b = ToggleButton(text='トグルボタンＢ', group='tgb')
        tgb_b.bind(on_press=self.on_togglebutton_pressed)
        self.add_widget(tgb_b)
        tgb_c = ToggleButton(text='トグルボタンＣ', group='tgb')
        tgb_c.bind(on_press=self.on_togglebutton_pressed)
        self.add_widget(tgb_c)

    def on_togglebutton_pressed(self, instance):
        print('%s がクリックされて %s になりました。' % (instance.text, instance.state))


class ExampleApp(App):
    def build(self):
        self.title = 'ToggleButtons (group)'
        return KivyToggleButton()


if __name__ == '__main__':
    ExampleApp().run()
