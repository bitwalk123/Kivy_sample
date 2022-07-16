import japanize_kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('kivy_checkbox_group_1.kv')
Window.size = (200, 200)


class KivyCheckBox(BoxLayout):
    def on_checkbox_changed(self, instance, value):
        print('チェックボックス %s は %d です。' % (instance, value))


class ExampleApp(App):
    def build(self):
        self.title = 'CheckBoxes (group)'
        return KivyCheckBox()


if __name__ == '__main__':
    ExampleApp().run()
