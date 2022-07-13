import japanize_kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox

Window.size = (200, 200)


class KivyCheckBox(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'
        self.init_ui()

    def init_ui(self):
        chb_a = CheckBox(group='chb')
        chb_a.bind(active=self.on_checkbox_changed)
        self.add_widget(chb_a)
        chb_b = CheckBox(group='chb')
        chb_b.bind(active=self.on_checkbox_changed)
        self.add_widget(chb_b)
        chb_c = CheckBox(group='chb')
        chb_c.bind(active=self.on_checkbox_changed)
        self.add_widget(chb_c)

    def on_checkbox_changed(self, instance, value):
        print('The checkbox is %s, %d' % (instance, value))


class ExampleApp(App):
    def build(self):
        self.title = 'CheckBoxes (group)'
        return KivyCheckBox()


if __name__ == '__main__':
    ExampleApp().run()
