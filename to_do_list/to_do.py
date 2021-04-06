from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.layout import Layout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle
from kivy.uix.popup import Popup


class welcome_page(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.rows = 4
        self.add_widget(Label(text='welcome to '))
        self.add_widget(Label(text='To-Do Quick Access'))
        self.add_widget(Label(text='username'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='Stay Beautiful'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        self.b1 = Button(
            text = 'click this !',
            background_color = (0,23,63,1),
            color = (0,0,0,1),
            size_hint = (0.1,0.1)

            )
        self.add_widget(self.b1)
        self.size_hint = (0.5, 0.5)
        self.pos = (150, 150)

class to_do_listApp(App):
    def build(self):
        return welcome_page()
to_do_listApp().run()
