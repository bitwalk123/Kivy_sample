import japanize_kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

Window.size = (200, 200)


class KivyBoxLayout(GridLayout):
    def __init__(self):
        super().__init__()
        self.cols = 3
        self.init_ui()

    def init_ui(self):
        btn_a = Button(text='A')
        btn_a.bind(on_press=self.on_button_pressed)
        self.add_widget(btn_a)
        btn_b = Button(text='B')
        btn_b.bind(on_press=self.on_button_pressed)
        self.add_widget(btn_b)
        btn_c = Button(text='C')
        btn_c.bind(on_press=self.on_button_pressed)
        self.add_widget(btn_c)
        btn_d = Button(text='D')
        btn_d.bind(on_press=self.on_button_pressed)
        self.add_widget(btn_d)
        btn_e = Button(text='E')
        btn_e.bind(on_press=self.on_button_pressed)
        self.add_widget(btn_e)
        btn_f = Button(text='F')
        btn_f.bind(on_press=self.on_button_pressed)
        self.add_widget(btn_f)
        btn_g = Button(text='G')
        btn_g.bind(on_press=self.on_button_pressed)
        self.add_widget(btn_g)

    def on_button_pressed(self, instance):
        print('ボタン %s がクリックされました。' % instance.text)


class ExampleApp(App):
    def build(self):
        self.title = 'GridLayout'
        return KivyBoxLayout()


if __name__ == '__main__':
    ExampleApp().run()
