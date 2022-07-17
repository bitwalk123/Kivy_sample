import japanize_kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

Window.size = (200, 200)


class KivyTextInput(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'
        self.init_ui()

    def init_ui(self):
        txt_a = TextInput(size_hint=(1, .8))
        txt_a.bind(
            focus=self.on_focus,
            text=self.on_text,
        )
        self.add_widget(txt_a)
        txt_b = TextInput(multiline=False, size_hint=(1, .2))
        txt_b.bind(
            focus=self.on_focus,
            on_text_validate=self.on_enter,
            text=self.on_text,
        )
        self.add_widget(txt_b)

    def on_focus(self, instance, value):
        if value:
            print('%s がフォーカスされました。' % instance)
        else:
            print('%s のフォーカスが外れました。' % instance)

    def on_enter(self, instance):
        print('%s で改行キーが押されました。' % instance)

    def on_text(self, instance, value):
        print('ウィジェット %s の入力:\n%s' % (instance, value))


class ExampleApp(App):
    def build(self):
        self.title = 'TextInputs'
        return KivyTextInput()


if __name__ == '__main__':
    ExampleApp().run()
