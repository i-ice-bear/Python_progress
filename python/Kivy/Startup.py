from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button


class TestApp(App):
    def build(self):
        btn = Button(text="Push Me !",
                     font_size="20sp",
                     background_color=(1, 1, 1, 1),
                     color=(1, 1, 1, 1),
                     size=(12, 12),
                     size_hint=(.2, .2),
                     pos=(300, 250))
        btn.bind(on_press=self.callback)
        return btn

    def callback(self, event):
        print("button pressed")
        print('Yoooo !!!!!!!!!!!')


TestApp().run()
