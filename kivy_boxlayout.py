import japanize_kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

Window.size = (200, 200)


class KivyBoxLayout(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'
        self.init_ui()

    def init_ui(self):
        btn_a = Button(text='A', size_hint=(1, .2))
        btn_a.bind(on_press=self.on_button_pressed)
        self.add_widget(btn_a)
        btn_b = Button(text='B', size_hint=(1, .3))
        btn_b.bind(on_press=self.on_button_pressed)
        self.add_widget(btn_b)
        layout = BoxLayout(orientation='horizontal', size_hint=(1, .5))
        self.add_widget(layout)
        btn_c = Button(text='C', size_hint=(.2, 1))
        btn_c.bind(on_press=self.on_button_pressed)
        layout.add_widget(btn_c)
        btn_d = Button(text='D', size_hint=(.3, 1))
        btn_d.bind(on_press=self.on_button_pressed)
        layout.add_widget(btn_d)
        btn_e = Button(text='E', size_hint=(.5, 1))
        btn_e.bind(on_press=self.on_button_pressed)
        layout.add_widget(btn_e)

    def on_button_pressed(self, instance):
        print('ボタン %s がクリックされました。' % instance.text)


class ExampleApp(App):
    def build(self):
        self.title = 'BoxLayout'
        return KivyBoxLayout()


if __name__ == '__main__':
    ExampleApp().run()
