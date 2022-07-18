import japanize_kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('kivy_textinput_1.kv')
Window.size = (200, 200)


class KivyTextInput(BoxLayout):
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
