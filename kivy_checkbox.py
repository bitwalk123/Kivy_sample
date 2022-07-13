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
        chb_a = CheckBox()
        chb_a.bind(active=self.on_checkbox_active)
        self.add_widget(chb_a)
        chb_b = CheckBox()
        chb_b.bind(active=self.on_checkbox_active)
        self.add_widget(chb_b)
        chb_c = CheckBox()
        chb_c.bind(active=self.on_checkbox_active)
        self.add_widget(chb_c)

    def on_checkbox_active(self, checkbox, value):
        if value:
            print('The checkbox', checkbox, 'is active')
        else:
            print('The checkbox', checkbox, 'is inactive')


class ExampleApp(App):
    def build(self):
        self.title = 'CheckBoxes'
        return KivyCheckBox()


if __name__ == '__main__':
    ExampleApp().run()
