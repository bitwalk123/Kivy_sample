import japanize_kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout

Window.size = (200, 200)


class KivyStackLayout(StackLayout):
    def __init__(self):
        super().__init__()
        self.orientation = 'lr-tb'
        #self.orientation = 'rl-bt'
        #self.orientation = 'tb-lr'
        self.init_ui()

    def init_ui(self):
        for i in range(10):
            btn = Button(text=chr(i + 65), width=(i + 1) * 10, size_hint=(None, 0.2))
            btn.bind(on_press=self.on_button_pressed)
            self.add_widget(btn)

    def on_button_pressed(self, instance):
        print('ボタン %s がクリックされました。' % instance.text)


class ExampleApp(App):
    def build(self):
        self.title = 'StackLayout'
        return KivyStackLayout()


if __name__ == '__main__':
    ExampleApp().run()
