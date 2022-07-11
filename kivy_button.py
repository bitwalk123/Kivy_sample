import japanize_kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

# Reference:
# https://note.com/npaka/n/nc18a554cc336

Window.size = (200, 200)


class KivyButton(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation='vertical'
        self.init_ui()

    def init_ui(self):
        btn_a = Button(text='ボタンＡ')
        btn_a.bind(on_press=self.on_button_pressed)
        self.add_widget(btn_a)
        btn_b = Button(text='ボタンＢ')
        btn_b.bind(on_press=self.on_button_pressed)
        self.add_widget(btn_b)
        btn_c = Button(text='ボタンＣ')
        btn_c.bind(on_press=self.on_button_pressed)
        self.add_widget(btn_c)

    def on_button_pressed(self, instance):
        print('%s がクリックされました。' % instance.text)


class ExampleApp(App):
    def build(self):
        self.title = 'Button'
        return KivyButton()


if __name__ == '__main__':
    ExampleApp().run()
